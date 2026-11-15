import argparse
import csv
import json
import math
import warnings
from pathlib import Path

import librosa
import numpy as np
import soundfile as sf


SR = 22050
HOP = 256
NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
LANES = ["kick", "snare", "toms", "hh", "ride", "crash"]


def nname(midi):
    midi = int(round(midi))
    return NAMES[midi % 12] + str(midi // 12 - 1)


def load(path, sr=SR):
    y, original_sr = sf.read(path, always_2d=True)
    return librosa.resample(y.mean(axis=1), orig_sr=original_sr, target_sr=sr).astype(np.float32)


def stem_path(folder, name):
    paths = sorted(folder.glob(name + ".*"))
    if len(paths) != 1:
        raise FileNotFoundError(f"Expected exactly one {name} stem in {folder}; found {len(paths)}")
    return paths[0]


def db(y):
    if y.size == 0:
        raise ValueError("Cannot measure an empty audio interval")
    return float(20 * np.log10(np.sqrt(np.mean(y ** 2)) + 1e-9))


def build_grid(bpm, beat_offset, duration, phase):
    if not all(math.isfinite(v) for v in (bpm, beat_offset, duration)) or bpm <= 0 or duration <= 0:
        raise ValueError("Tempo and duration must be finite and positive")
    if phase not in range(4):
        raise ValueError("Downbeat phase must be 0, 1, 2 or 3")
    period = 60 / bpm
    bar_s = 4 * period
    origin = beat_offset % period + phase * period
    if origin >= duration:
        raise ValueError("The selected downbeat falls outside the audio")
    length = (duration - origin) / bar_s
    if math.isclose(length, round(length), abs_tol=1e-9, rel_tol=0):
        length = float(round(length))
    complete = math.floor(length)
    count = math.ceil(length)
    boundaries = origin + np.arange(count + 1) * bar_s
    boundaries[-1] = duration
    grid = {
        "bpm": round(float(bpm), 3),
        "beat_s": float(period),
        "bar_s": float(bar_s),
        "first_bar_start_s": float(origin),
        "n_bars": count,
        "complete_bars": complete,
        "partial_final_bar_s": float((length - complete) * bar_s),
        "duration_s": float(duration),
        "downbeat_phase": phase,
        "downbeat_basis": "Opening phrase boundaries and clap backbeat; phase is selected, not inferred from a four-on-the-floor kick.",
    }
    return grid, boundaries


def fit_grid(drums, phase):
    if db(drums) < -60:
        raise ValueError("The drum stem is too quiet to fit a tempo")
    duration = len(drums) / SR
    envelope = librosa.onset.onset_strength(y=drums, sr=SR, hop_length=HOP)
    times = librosa.frames_to_time(np.arange(len(envelope)), sr=SR, hop_length=HOP)
    best = (-math.inf, 0.0, 0.0)
    for bpm in np.arange(118, 130, 0.02):
        period = 60 / bpm
        for offset in np.arange(0, period, 0.01):
            beats = np.arange(offset, duration, period)
            score = float(np.interp(beats, times, envelope).mean())
            if score > best[0]:
                best = (score, float(bpm), float(offset))
    _, bpm, offset = best
    period = 60 / bpm
    offsets = np.arange(offset - 0.01, offset + 0.01, 0.002)
    offset = max(offsets, key=lambda o: np.interp(np.arange(o, duration, period), times, envelope).mean())
    return build_grid(bpm, float(offset), duration, phase)


def to_pos(time, grid):
    step_s = grid["bar_s"] / 16
    position = (time - grid["first_bar_start_s"]) / step_s
    nearest = math.floor(position + 0.5)
    bar, step = divmod(nearest, 16)
    return bar + 1, step + 1, (position - nearest) * step_s * 1000


def write_csv(path, header, rows):
    with path.open("w", newline="") as output:
        writer = csv.writer(output, lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def measure_levels(stems, output, grid, boundaries):
    names = ["drums", "bass", "other", "vocals"]
    audio = {name: load(stem_path(stems, name)) for name in names}
    if any(abs(len(y) / SR - grid["duration_s"]) > 0.01 for y in audio.values()):
        raise ValueError("SCNet stem durations differ by more than 10 ms")
    rows = []
    for index, (start, end) in enumerate(zip(boundaries[:-1], boundaries[1:])):
        a, b = int(start * SR), min(len(audio["drums"]), int(end * SR))
        rows.append(
            [index + 1, round(float(start), 4), round(float(end), 4), round(float(end - start), 4),
             int(index < grid["complete_bars"])]
            + [round(db(audio[name][a:b]), 2) for name in names]
        )
    write_csv(
        output / "stem_levels_per_bar.csv",
        ["bar", "start_s", "end_s", "duration_s", "complete", *[name + "_db" for name in names]],
        rows,
    )


def extract_notes(stems, output, grid):
    from basic_pitch.inference import Model, predict
    import basic_pitch

    model_path = Path(basic_pitch.__file__).parent / "saved_models/icassp_2022/nmp.onnx"
    model = Model(model_path)
    configs = {
        "bass": dict(minimum_frequency=30, maximum_frequency=400, onset_threshold=0.4,
                     frame_threshold=0.25, minimum_note_length=60),
        "other": dict(minimum_frequency=100, maximum_frequency=2500, onset_threshold=0.5,
                      frame_threshold=0.3, minimum_note_length=80),
        "vocals": dict(minimum_frequency=100, maximum_frequency=1200, onset_threshold=0.5,
                       frame_threshold=0.3, minimum_note_length=100),
    }
    for stem, settings in configs.items():
        _, _, events = predict(stem_path(stems, stem), model, **settings)
        rows = []
        for start, end, pitch, amplitude, _bends in sorted(events):
            bar, step, deviation = to_pos(start, grid)
            rows.append([
                bar, step, max(1, round((end - start) / (grid["bar_s"] / 16))),
                int(pitch), nname(pitch), round(float(amplitude), 3),
                round(float(start), 4), round(float(end - start), 4), round(float(deviation), 2),
            ])
        write_csv(
            output / f"notes_{stem}.csv",
            ["bar", "step", "len_steps", "midi", "note", "model_amplitude_0_1", "start_s", "len_s", "timing_dev_ms"],
            rows,
        )
        print(stem, len(rows), "note candidates", flush=True)


def extract_drums(folder, output, grid, drum_level):
    grids = {}
    quality = {}
    for lane in LANES:
        y = load(stem_path(folder, lane), 44100)
        if abs(len(y) / 44100 - grid["duration_s"]) > 0.01:
            raise ValueError(f"{lane} duration differs from the drum stem by more than 10 ms")
        level = db(y)
        difference = level - drum_level
        quality[lane] = {
            "mono_rms_dbfs": round(level, 2),
            "rms_relative_to_drums_db": round(difference, 2),
            "low_energy_lane": difference < -25,
            "caution": "Relative onset strength is not detection confidence. Low-energy lanes may be bleed; hh combines open and closed hats.",
        }
        if difference < -25:
            warnings.warn(f"{lane} is {difference:.1f} dB below drums; keep candidates, but do not infer a busy percussion part")
        envelope = librosa.onset.onset_strength(y=y, sr=44100, hop_length=256, aggregate=np.max)
        peaks = librosa.onset.onset_detect(
            onset_envelope=envelope, sr=44100, hop_length=256, backtrack=False,
            delta=0.0, wait=6, pre_avg=4, post_avg=4, pre_max=4, post_max=4,
        )
        reference = float(np.percentile(envelope[peaks], 95)) if peaks.size else 0.0
        hits = []
        pattern = np.zeros((grid["n_bars"], 16))
        if reference <= 0:
            warnings.warn(f"No positive onsets detected in {lane}")
        else:
            for peak in peaks:
                strength = float(envelope[peak])
                if strength <= 0.2 * reference:
                    continue
                time = float(librosa.frames_to_time(peak, sr=44100, hop_length=256))
                bar, step, deviation = to_pos(time, grid)
                if 1 <= bar <= grid["n_bars"]:
                    relative = min(strength / reference, 1.5)
                    hits.append([bar, step, round(relative, 3), round(deviation, 2), round(time, 4)])
                    pattern[bar - 1, step - 1] = max(pattern[bar - 1, step - 1], relative)
        write_csv(
            output / f"drums_{lane}.csv",
            ["bar", "step", "strength_rel", "timing_dev_ms", "start_s"], hits,
        )
        quality[lane]["candidate_count"] = len(hits)
        grids[lane] = pattern.round(3).tolist()
        print(lane, len(hits), "onset candidates", flush=True)
    (output / "drum_lane_grids.json").write_text(json.dumps(grids) + "\n")
    (output / "drum_quality.json").write_text(json.dumps(quality, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Analyse the supplied Deep Inside stems; no audio is exported.")
    parser.add_argument("mode", nargs="?", default="all", choices=["all", "levels", "notes", "drums"])
    parser.add_argument("--stems-dir", required=True, type=Path)
    parser.add_argument("--drums-dir", type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--downbeat-phase", type=int, choices=range(4), default=0,
                        help="Phase 0 preserves this upload's opening bar. Do not transfer it blindly to another mix.")
    args = parser.parse_args()
    if args.mode in ("all", "drums") and args.drums_dir is None:
        parser.error("--drums-dir is required for all/drums mode")
    drums = load(stem_path(args.stems_dir, "drums"))
    grid, boundaries = fit_grid(drums, args.downbeat_phase)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "grid.json").write_text(json.dumps(grid, indent=2) + "\n")
    print(grid, flush=True)
    if args.mode in ("all", "levels"):
        measure_levels(args.stems_dir, args.output_dir, grid, boundaries)
    if args.mode in ("all", "notes"):
        extract_notes(args.stems_dir, args.output_dir, grid)
    if args.mode in ("all", "drums"):
        extract_drums(args.drums_dir, args.output_dir, grid, db(drums))


if __name__ == "__main__":
    main()
