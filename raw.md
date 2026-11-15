# Hardrive — Deep Inside: Reviewed Stem Analysis

**Uploaded MP3 · 392.668 s · approximately 123.62 BPM · 202 complete bars plus a partial tail**

This is the evidence behind [deep_inside_instructions.md](./deep_inside_instructions.md). The review corrected the opening-bar alignment, bass phrase, vocal coverage and hardware workflow. [Jonty's track](./jonty_first_track.md) remains a separate, intentionally original *Deep Inside*-style composition.

> **No listening or hardware verification:** all audio work was local signal analysis. Two pitch algorithms agreeing on the same separated bass is stronger evidence than one algorithm, but they still share the separator's errors. No audio, vocal samples, model weights or protected recordings are committed.

## 1. Source Identity

The uploaded `0008_-_Deep_Inside.mp3` is 44.1 kHz stereo, 320 kbps, 392.6684807 s. Mutagen reads:

```text
Title:     Deep Inside
Artist:    Hardrive
Album:     Deep Inside (Remixes)
Track:     3/8
Year:      2015
Copyright: (c) 2015 Strictly Rhythm Records
```

**Correction:** a remixes album does not make every included track a remix. The eight-track release's third entry is unnamed *Deep Inside*, consistent with the original being reissued. The tags do not identify a remixer or prove a particular mastering. Do not label this upload a confirmed "2015 remix", nor claim a fingerprint match to the 1993 vinyl.

The release listing is indexed on [Apple Music](https://music.apple.com/jp/album/deep-inside-remixes/986139771); the original EP is documented by [Discogs](https://www.discogs.com/release/20174-Hardrive-Deep-Inside). [Insomniac](https://www.insomniac.com/music/from-the-crate-hardrive-deep-inside/) describes the Barbara Tucker *Beautiful People* sample. These establish release/sample context, not the instrument patches or an exact score.

## 2. Pipeline & Persistent Outputs

SCNet four-stem separation (`drums`, `bass`, `other`, `vocals`) was followed by MDX23C DrumSep on the drum stem (`kick`, `snare`, `toms`, `hh`, `ride`, `crash`). Both used CPU and reduced overlap for speed. Basic Pitch's bundled ONNX model produced note candidates. The review independently checked bass pitch using YIN, section levels, kick-clock regression and original-mix low-band transients.

All persistent measurements are in [`analysis/deep_inside/data/`](./analysis/deep_inside/data/):

| File | Meaning |
|---|---|
| `grid.json` | Current tempo, earliest selected downbeat, complete/partial bar counts |
| `stem_levels_per_bar.csv` | Mono RMS dBFS, actual interval bounds and complete-bar flag |
| `notes_bass.csv`, `notes_other.csv`, `notes_vocals.csv` | Raw candidate notes, real timestamps/durations, nearest grid position and deviation |
| `drums_<lane>.csv` | All six lanes' permissive onset candidates, including unreliable lanes |
| `drum_lane_grids.json` | Six `203 × 16` arrays of relative candidate strengths |
| `drum_quality.json` | Lane energy relative to drums; warnings against noise-normalised false certainty |
| `provenance.json` | Input hash, model/config hashes, toolkit revision and library versions |
| `review_evidence.json` | Pre-correction audit, independent YIN checks and evidence for the changes |

`review_evidence.json` explicitly labels its old `saved_grid` as the **faulty baseline**; use `grid.json` for current coordinates. Keeping rejected candidates allows future checking instead of silently losing the DrumSep results.

**Column correction:** `model_amplitude_0_1` replaces the misleading `velocity_0_1`. Basic Pitch averages neural frame activations; this is **not recovered MIDI velocity, acoustic loudness or calibrated confidence**. Likewise, `strength_rel` is onset strength relative to a lane's 95th-percentile peak, not probability that the named instrument played.

## 3. Timing Review

The constant-tempo comb fit gives **123.62 BPM**, beat `0.485358 s`, bar `1.941433 s`. A linear check of retained kick timestamps gives about `123.624 BPM`, median absolute residual `2.2 ms`, 95th percentile `5.9 ms`. This supports the steady clock; it does not make every extracted onset accurate.

The earlier `1.488 s` offset put the clap on the wrong beats. Adding a beat corrected the phase but produced `1.973 s`, **skipping one complete opening bar**. Phase must wrap to the earliest occurrence, not keep advancing the start.

**Current bar 1: `0.032 s`, phase `0`.** The original mix's low-frequency transients begin around `15.6 s`, agreeing with the kick entering after eight bars; bass onset around `46.6 s` agrees with bar 25. The first vocal note candidate at `0.546 s` is now **bar 1, step 5**, not the old bar 0.

```text
t(bar) = 0.032 + (bar − 1) × 240/123.62
```

There are **202 complete intervals**, ending around `392.20 s`, plus `0.467 s` of partial bar 203. The CSV bounds clip that last interval to the actual audio end, avoiding fabricated complete bars or empty RMS measurements. The MC-303 recipe uses 202 bars and omits the extra fraction of trailing audio.

## 4. Reviewed Arrangement & Levels

These are mean **per-bar mono RMS dBFS**, not mixer fader settings. Low-level tails/bleed can survive an element's musical exit.

| Bars | Start | Drums | Bass | Other | Vocals |
|---|---|---:|---:|---:|---:|
| 1–8 | 0:00.0 | -21.3 | -58.1 | -37.7 | -17.9 |
| 9–24 | 0:15.6 | -13.6 | -58.0 | -26.3 | -23.3 |
| 25–32 | 0:46.6 | -13.7 | -17.2 | -26.0 | -23.0 |
| 33–56 | 1:02.2 | -13.8 | -17.2 | -23.9 | -22.8 |
| 57–64 | 1:48.8 | -21.5 | -17.9 | -23.5 | -17.8 |
| 65–88 | 2:04.3 | -13.8 | -17.2 | -24.7 | -23.1 |
| 89–96 | 2:50.9 | -17.0 | -55.1 | -26.5 | -25.1 |
| 97–104 | 3:06.4 | -14.0 | -17.3 | -24.4 | -25.5 |
| 105–112 | 3:21.9 | -13.5 | -17.0 | -26.9 | -60.6 |
| 113–128 | 3:37.5 | -14.0 | -16.9 | -25.7 | -24.3 |
| 129–136 | 4:08.5 | -20.9 | -53.4 | -22.2 | -18.3 |
| 137–152 | 4:24.1 | -13.8 | -17.2 | -24.9 | -23.2 |
| 153–160 | 4:55.1 | -17.1 | -15.2 | -33.5 | -60.9 |
| 161–168 | 5:10.7 | -15.5 | -15.6 | -45.8 | -61.9 |
| 169–176 | 5:26.2 | -13.5 | -36.8 | -51.4 | -56.8 |
| 177–184 | 5:41.7 | -13.4 | -61.8 | -34.0 | -30.1 |
| 185–192 | 5:57.3 | -21.3 | -56.4 | -30.1 | -16.8 |
| 193–200 | 6:12.8 | -59.0 | -67.1 | -43.7 | -15.5 |
| 201–202 | 6:28.3 | -75.6 | -75.1 | -74.2 | -56.2 |

The core guide uses kick `9–56`, `65–128`, `137–184`, with weaker `89–96` / `153–160` and medium `161–168`. Kick is absent in the main drops and from 185. Bass plays `25–88`, `97–128`, `137–172`; levels in 89/173 can include transition tails. Keys appear within bar 6, carry through the main body, thin out around 153–157, then return as late stabs around 181.

**Vocal correction:** the old recipe left most of the intro/main body silent. At a -35 dBFS gate the review finds activity across `1–104`, `113–152`, `179–200`, plus one questionable isolated bar at 169. Energy alone is not vocal identification, but strong pitch candidates and the large contrast against `105–112` / `153–176` support much wider coverage. The revised guide follows those main ranges and excludes the isolated bar.

## 5. Bass: Stronger Evidence, Actual Low Register

Basic Pitch and independent YIN checks in bars `25–32`, `97–104` and `153–160` agree on a **two-bar alternating G1/B1 foundation**. G1 is a sustained part of the main riff, not just an intro/fill artifact. The previous one-bar B-only replacement changed a defining pitch.

| Bar type | Simplified onset pitches |
|---|---|
| A-G | G1 at 1; G2 at 8 and 11; D2 at 13; E2 around 14 |
| A-D | G1 at 1; G2 at 8; D2 around 11; E2 around 14 |
| B | B1 at 1; E2 at 8; F#2 around 10–11; E2 at 14 |

A/B alternate; the A ending switches every eight bars. From bar 25, the observed sequence is G-ending `25–32`, D-ending `33–40`, G-ending `41–48`, D-ending `49–56`, then continues through the active ranges. The guide's `A-end` grid preserves that larger phrase. Minor passing/retrigger candidates remain in the raw CSV, not promoted automatically into the recipe.

**Gates matter:** roots last roughly five to six sixteenths in many candidate events. A sustained pitch occupying six cells is not six attacks. Transition timing differs by up to a sixteenth between algorithms, so the guide gives practical gates and nearest onsets rather than pretending to have an exact MIDI score.

**Hardware correction:** G1 is below the pads at octave -2, but not impossible on the instrument. Recording the whole bass five semitones up puts every needed pitch on pads `2–14` at -2; a Part 3 Transpose of -5 restores the real register. This avoids the faulty octave-up button and avoids substituting B1. The tonal centre remains unresolved; preserving pitches is safer than arbitrarily shifting the bass to match a key database.

## 6. Keys, Voice & Drum Uncertainty

The "other" stem is not an isolated piano. Strong simultaneous candidates include A#3/F4 and A3/D4/F#4; the latter sometimes includes A4. These justify auditioning paired/stacked voicings instead of the old invented A4/A#4/G4 lead. They **do not prove chord names or instrument identity**. The historical `Dmaj7/Gm7/A7` template labels and assertions that G mainly came from fills are withdrawn.

Vocal candidates cluster around A4/A#4/B4 with occasional neighbouring pitches. Formants, harmonics, pitch bends and separator leakage can all mislead the transcription. An "auh" part is only a rhythm/register proxy; no lyrics or exact vocal melody were established.

| DrumSep lane | Current treatment |
|---|---|
| Kick | Strong periodic evidence for four-on-the-floor; preserve weak beats rather than delete 2/4 |
| Snare | Usable backbeat proxy, not a verified clap/snare split; ghosts may include echo/bleed |
| `hh` | Usable combined hat timing; open/closed identification remains approximate |
| Toms, ride, crash | About 35–41 dB below drums overall; dense relative peaks are not a trustworthy part |

The permissive detector produces 1,709 kick, 2,380 snare, 4,958 tom, 5,269 hh, 5,965 ride and 5,793 crash candidates. **Counts above the number of grid cells do not by themselves prove noise:** multiple peaks can fall in one cell. The serious problem is lane-by-lane normalisation without an absolute energy/confidence check, which can make a nearly silent lane look busy.

Consequently the noisy lanes are retained and flagged, not asserted absent and not filled with generic drum patterns. Intro/break/outro hats are much weaker than the full-groove hats, so they are no longer mandatory everywhere. Closed hats on every even step and a crash on every return were genre guesses, not measurements.

The audit also finds a small fraction of full-scale samples in exported WAV stems. This is another reason not to turn stem levels or neural amplitudes directly into "original" velocities. Faster separation preserved useful structure, but **lower audio quality can damage pitch, onset and dynamic measurements too**.

## 7. MC-303 Corrections & Likeness Limits

The corrected instructions preserve the compact **Pass · pattern · octave · velocity**, then **pad · steps · bars** layout of [record_cheat.md](./record_cheat.md).

**Verified workflow corrections:** `LGH` accepts 1–32 bars, including ten; already recorded 32-bar patterns need Delete Measure to shorten. The U37 pass must explicitly override the reused `LGH 32` routine. Part 2 recording must turn Play Quantize off because recording targets the Recording Part, regardless of the usual quantize aim. Setup copies must not retain unrelated notes/Modify data or the template lead's unwanted modulation. Song uses `U31–U37`, never nonexistent U51–U57.

**Bank/feature improvements:** actual low bass register and longer gates; audition house/101/sine bass without changing the phrase; piano versus percussive organ for the same candidate voicings; simpler `auh` versus `auh auh` with articulation checked by ear; dry low end with modest keys/voice sends; a deliberate keys LEVEL fade; safe Part Copy for repeated cells. Patch names do not establish sonic identity without listening.

The Delay/Reverb processor requires choosing one main algorithm; its TIME 0–127 is not milliseconds. Part R panel modifications affect the kit, so a "kick-only" filter sweep cannot be promised there. There is no user-sample import, modern sidechain compressor or arbitrary plug-in chain. Internal polyphony is 28 voices; layered piano/voice patches and long releases can consume multiple voices per note.

**Ceiling:** structure and bass likeness can improve substantially on the MC-303 alone. Exact vocal likeness cannot be achieved with its fixed factory voice bank. A piano/organ/bass patch match, precise ghost timing, swing and final balance still require comparison by ear on the device; no similarity score is claimed.

## 8. Reproduce & Resume

[`analysis/deep_inside/analyze.py`](./analysis/deep_inside/analyze.py) accepts explicit directories and exports no audio:

```bash
python analyze.py all \
  --stems-dir /path/to/scnet/deep_inside \
  --drums-dir /path/to/drumsep/drums \
  --output-dir /path/to/review-data \
  --downbeat-phase 0
```

Use `levels`, `notes` or `drums` instead of `all` for a narrower pass. Missing/ambiguous stems and incompatible durations fail explicitly. Phase 0 is specific to this upload; do not transfer it blindly to another mix.

The tested environment used numpy/librosa/soundfile/scipy, Basic Pitch 0.4.0 with onnxruntime, plus resampy, pretty_midi, mido and mir_eval. TensorFlow/CoreML/TFLite were not used; their optional-backend warnings are expected. Exact installed versions and model/config hashes are in `provenance.json`. The ONNX-only installation bypassed Basic Pitch's TensorFlow dependency, so the manifest describes a working environment, not a claim that every optional package requirement was installed.

Separation: [Music-Source-Separation-Training](https://github.com/ZFTurbo/Music-Source-Separation-Training), SCNet v1.0.6 checkpoint with overlap 1; MDX23C DrumSep mirror in [openmirlab/mdxnet-infer](https://github.com/openmirlab/mdxnet-infer/releases/tag/weights-drumsep-v1), overlap 2. Its six outputs are drum categories, not a universal split of every song instrument.

Earlier online-listening attempts were blocked; this review again found browser/DNS restrictions for direct media/manual/catalogue fetches. Indexed catalogue/manual references were used alongside existing manual-cross-checked repository notes. [Sweetwater's pattern-length instructions](https://www.sweetwater.com/sweetcare/articles/roland-mc-303-pattern-length-creating-pattern-less-than/) corroborate LGH; the [Roland manual](https://archive.org/details/synthmanual-roland-mc-303-owners-manual) is the hardware reference, especially pp.20, 30–35, 46–53, 61–66 and 92–93. No inaccessible audio was claimed heard.
