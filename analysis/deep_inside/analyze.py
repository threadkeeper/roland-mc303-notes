import sys, os, json, glob, csv
import numpy as np, librosa, soundfile as sf

STEMS = '/tmp/out/deep_inside'
DRUMS = '/tmp/drout'
OUT = '/tmp/data'
os.makedirs(OUT, exist_ok=True)
SR = 22050
HOP = 256
NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def nname(m):
    m = int(round(m))
    return NAMES[m % 12] + str(m // 12 - 1)


def load(path, sr=SR):
    y, s = sf.read(path, always_2d=True)
    y = y.mean(axis=1)
    return librosa.resample(y, orig_sr=s, target_sr=sr).astype(np.float32)


def stem_path(d, name):
    return glob.glob(os.path.join(d, name + '.*'))[0]


# ------------------------------------------------------------------ grid
yd = load(stem_path(STEMS, 'drums'))
dur = len(yd) / SR
oenv = librosa.onset.onset_strength(y=yd, sr=SR, hop_length=HOP)
ft = librosa.frames_to_time(np.arange(len(oenv)), sr=SR, hop_length=HOP)
best = None
for bpm in np.arange(118, 130, 0.02):
    period = 60 / bpm
    for off in np.arange(0, period, 0.01):
        t = np.arange(off, dur, period)
        s = np.interp(t, ft, oenv).sum() / len(t)
        if best is None or s > best[0]:
            best = (s, bpm, off)
_, bpm, off = best
period = 60 / bpm
offs = np.arange(off - 0.01, off + 0.01, 0.002)
off = max(offs, key=lambda o: np.interp(np.arange(o, dur, period), ft, oenv).sum())
beats = np.arange(off % period, dur, period)
S = np.abs(librosa.stft(yd, n_fft=2048, hop_length=HOP))
fr = librosa.fft_frequencies(sr=SR, n_fft=2048)
low = S[fr < 120].sum(axis=0)
lowb = np.interp(beats, ft, low[:len(ft)])
phase = max(range(4), key=lambda p: lowb[p::4].sum())
bars_t = beats[phase::4]
bars_t = np.append(bars_t, bars_t[-1] + 4 * period)
bars_t = bars_t + period  # backbeat/bass phrasing show the true downbeat is one beat later
nb = len(bars_t) - 1
step_s = period / 4
grid = {'bpm': round(float(bpm), 3), 'beat_s': round(float(period), 4), 'bar_s': round(float(4 * period), 4),
        'first_bar_start_s': round(float(bars_t[0]), 3), 'n_bars': nb, 'duration_s': round(float(dur), 2),
        'downbeat_phase': int(phase)}
json.dump(grid, open(f'{OUT}/grid.json', 'w'), indent=1)
print(grid)


def to_pos(t):
    """time (s) -> (bar 1-based, step 1-16 float-ish, deviation ms from nearest step)."""
    x = (t - bars_t[0]) / step_s
    k = int(np.floor(x + 0.5))
    bar, step = divmod(k, 16)
    dev = (x - k) * step_s * 1000
    return bar + 1, step + 1, dev


# ------------------------------------------------------------------ levels
def db(x):
    return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9)


mode = sys.argv[1] if len(sys.argv) > 1 else 'all'

if mode in ('all', 'levels'):
    with open(f'{OUT}/stem_levels_per_bar.csv', 'w', newline='') as f:
        w = csv.writer(f)
        names = ['drums', 'bass', 'other', 'vocals']
        w.writerow(['bar', 'start_s'] + [n + '_db' for n in names])
        ys = {n: load(stem_path(STEMS, n)) for n in names}
        for i in range(nb):
            a, b = int(bars_t[i] * SR), int(bars_t[i + 1] * SR)
            w.writerow([i + 1, round(float(bars_t[i]), 2)] + [round(float(db(ys[n][a:b])), 1) for n in names])

# ------------------------------------------------------------------ notes (basic-pitch, ONNX)
if mode in ('all', 'notes'):
    from basic_pitch.inference import predict, Model
    import basic_pitch
    onnx = os.path.join(os.path.dirname(basic_pitch.__file__), 'saved_models', 'icassp_2022', 'nmp.onnx')
    model = Model(onnx)
    cfg = {'bass': dict(minimum_frequency=30, maximum_frequency=400, onset_threshold=0.4, frame_threshold=0.25, minimum_note_length=60),
           'other': dict(minimum_frequency=100, maximum_frequency=2500, onset_threshold=0.5, frame_threshold=0.3, minimum_note_length=80),
           'vocals': dict(minimum_frequency=100, maximum_frequency=1200, onset_threshold=0.5, frame_threshold=0.3, minimum_note_length=100)}
    for stem, kw in cfg.items():
        _, _, events = predict(stem_path(STEMS, stem), model, **kw)
        rows = []
        for st, en, pitch, amp, _bends in sorted(events):
            bar, step, dev = to_pos(st)
            dsteps = max(1, int(round((en - st) / step_s)))
            rows.append([bar, step, dsteps, int(pitch), nname(pitch), round(float(amp), 2), round(float(st), 3), round(float(en - st), 3)])
        with open(f'{OUT}/notes_{stem}.csv', 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['bar', 'step', 'len_steps', 'midi', 'note', 'velocity_0_1', 'start_s', 'len_s'])
            w.writerows(rows)
        print(stem, len(rows), 'notes')

# ------------------------------------------------------------------ drums per lane
if mode in ('all', 'drums'):
    lanes = ['kick', 'snare', 'toms', 'hh', 'ride', 'crash']
    res = {}
    for lane in lanes:
        paths = glob.glob(os.path.join(DRUMS, '**', lane + '.*'), recursive=True)
        if not paths:
            continue
        y = load(paths[0], 44100)
        sr = 44100
        env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=256, aggregate=np.max)
        t = librosa.frames_to_time(np.arange(len(env)), sr=sr, hop_length=256)
        pk = librosa.onset.onset_detect(onset_envelope=env, sr=sr, hop_length=256, backtrack=False, delta=0.0,
                                        wait=6, pre_avg=4, post_avg=4, pre_max=4, post_max=4)
        strengths = env[pk]
        if len(strengths) == 0:
            continue
        ref = np.percentile(strengths, 95)
        keep = strengths > 0.2 * ref
        hits = []
        for k, s in zip(pk[keep], strengths[keep]):
            bar, step, dev = to_pos(t[k])
            if 1 <= bar <= nb:
                hits.append([bar, step, round(float(min(s / ref, 1.5)), 2), round(float(dev), 1)])
        res[lane] = hits
        with open(f'{OUT}/drums_{lane}.csv', 'w', newline='') as f:
            w = csv.writer(f)
            w.writerow(['bar', 'step', 'strength_rel', 'timing_dev_ms'])
            w.writerows(hits)
        print(lane, len(hits), 'hits')
    # 16-step presence grid per bar per lane
    pat = {lane: np.zeros((nb, 16)) for lane in res}
    for lane, hits in res.items():
        for bar, step, s, dev in hits:
            pat[lane][bar - 1, step - 1] = max(pat[lane][bar - 1, step - 1], s)
    json.dump({l: p.round(2).tolist() for l, p in pat.items()}, open(f'{OUT}/drum_lane_grids.json', 'w'))
