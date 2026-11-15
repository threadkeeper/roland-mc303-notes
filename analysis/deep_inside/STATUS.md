# Deep Inside — Persistent Review Status

The reviewed guide is [`../../deep_inside_instructions.md`](../../deep_inside_instructions.md); the detailed audit is [`../../raw.md`](../../raw.md). No audio was heard here or verified on a physical MC-303.

## Completed

- SCNet four-stem separation and MDX23C six-lane DrumSep completed on CPU.
- All six DrumSep candidate CSVs are now retained, including the low-energy tom/ride/crash lanes. Their quality warnings are in `data/drum_quality.json`.
- Corrected the skipped opening bar: phase 0, first downbeat `0.032 s`, 123.62 BPM. There are 202 complete bars and a 0.467-second partial analysis bar 203; the recipe is 202 bars.
- Checked G1/B1 bass alternation with independent YIN; preserved two-bar cells, eight-bar ending changes and held roots.
- Replaced the B1-for-G1 shortcut with a +5-semitone recording / -5 Part Transpose route. Keys use +2 / -2 to fit candidate voicings on the pads.
- Restored intro/body vocal-proxy coverage, corrected Part 2 input-quantize instructions and U37's 10-bar recording length.
- Updated raw analysis, sound-bank guidance, effects/automation caveats and README. Jonty's U41–U45/S-2 work is unchanged.
- Regenerated current data with the revised `analyze.py`; recorded input/model/config hashes and library versions in `data/provenance.json`.

## Resume Without Confusing Old and New Data

`data/grid.json` is authoritative. `data/review_evidence.json` deliberately retains the **pre-correction** grid and old guide coverage to explain the faults; it is not a second current bar map.

Run `analyze.py all --stems-dir <SCNet folder> --drums-dir <DrumSep folder> --output-dir <new folder> --downbeat-phase 0`. Libraries/backend and separator checkpoints are described in raw.md and provenance.json. The original MP3 and audio stems are not stored in GitHub and would have to be supplied or separated again after a fresh environment.

## Still Unverified

Exact mastering/mix identity; piano versus organ and chord voicings; vocal melody; open/closed hat identities and ghost-hit timing; sound settings and physical-unit button/display behaviour. Low-energy percussion candidates are not proof of absence. Closest vocal likeness needs authorised external sample playback: the MC-303 cannot import that sample.
