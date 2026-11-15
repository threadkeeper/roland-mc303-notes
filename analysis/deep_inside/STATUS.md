# Deep Inside (Hardrive, 2015 remix) – work status

Checkpoint so the work can be resumed. Nothing here was heard; all values come from stem separation plus signal analysis, so treat them as approximate.

## Pipeline (all CPU, temporary files in /tmp, no audio is committed)
1. SCNet 4-stem (ZFTurbo/Music-Source-Separation-Training, `scnet_checkpoint_musdb18.ckpt` from release v1.0.6, `--model_type scnet --force_cpu`, `num_overlap: 1`) → drums, bass, other, vocals.
2. DrumSep on the drums stem: MDX23C `aufr33-jarredou_DrumSep_model_mdx23c_ep_141_sdr_10.8059` (mirror: github.com/openmirlab/mdxnet-infer, release `weights-drumsep-v1`; `--model_type mdx23c`, `num_overlap: 2`, ~25 min) → kick, snare, toms, hh, ride, crash.
3. `analyze.py` (this folder) → `grid.json`, `stem_levels_per_bar.csv`, `notes_{bass,other,vocals}.csv`, `drums_<lane>.csv`, `drum_lane_grids.json`. Note extraction uses basic-pitch 0.4.0 with its bundled ONNX model (needs onnxruntime, resampy, mir_eval).

## Findings so far
- 123.62 BPM, bar = 1.941 s, 4/4, about 202 bars, ~392.7 s.
- Downbeat: the kick plays every beat, so the first fit was a beat out. The clap/snare backbeat and the bass phrase start show that bar 1 starts at about 1.973 s (one beat later than the first estimate). Bar numbers in older `raw.md` are therefore about a beat early; the regenerated data fixes this.
- DrumSep lane quality: **kick is clean** (`X...X...X...X...`). Snare/clap and hats are usable (open hat on 3/7/11/15 after the downbeat fix). **Toms, ride and crash fire on nearly every step = separation noise, do not use.**
- Arrangement (older bar numbers, ±1): intro 1–8 no kick, kick in at 9, bass in at 25, drop 57–64, bass out 89–96, breakdown 129–136, bass loudest 153–168, outro 193–202 vocal only.
- Key unresolved: B minor and E minor both fit the bass.

## To do
- Push regenerated `data/` (after the downbeat fix) into this folder.
- Write the MC-303 recreation guide in `record_cheat.md` pass-grid style (U41–U47, pass lists, pad grid, referencing the Jonty/record_cheat routines instead of repeating them).
- Update `raw.md` and `README.md`.
