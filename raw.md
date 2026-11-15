# Hardrive — Deep Inside (2015 remix file): Stem-Separated Analysis

**An uploaded 6:32.7 MP3 · ~123.6 BPM · 202 bars · split into drums / bass / other / vocals and measured per bar**

A bar-by-bar map of the uploaded file, built by separating it into four stems with an open-source model and analysing each stem. It is meant to sit beside [jonty_first_track.md](./jonty_first_track.md), whose arrangement (§3) was a *model* of a house 12-inch. This file replaces that guess with **measured** entry/exit bars, the bass riff and a drum grid, for this particular file.

**Jump to:** [Method](#1-method) · [What is verified](#2-what-is-verified-and-what-is-not) · [Arrangement](#3-the-arrangement-measured) · [Cheat card](#4-cheat-card-the-groove-on-one-page) · [Per-stem data](#5-per-stem-data) · [Mapping to Jonty's build](#6-using-this-with-jontys-build) · [Access log](#7-access-log) · [Sources](#8-sources)

> **Verification note:** Nothing here was *listened to*; this session has no audio playback. Every figure is machine-derived from the MP3 (ID3 tags, stem separation, signal analysis). The separation model is a small, fast one, so stems contain **bleed** (e.g. vocal energy in the intro may include drum or sample leakage). Treat bar numbers as accurate to about a bar, and treat anything marked *(low confidence)* as a hint, not a fact. **Instrument identities and lyrics are not determined.**

---

## 1. Method

1. **File and tags** read with mutagen / frame parsing.
2. **Stem separation** with **SCNet** (musdb18 4-stem checkpoint, ~42 MB) from the open-source [Music-Source-Separation-Training](https://github.com/ZFTurbo/Music-Source-Separation-Training) toolkit, run on CPU (about 4 minutes). It gives `drums`, `bass`, `other`, `vocals`. A larger 4-stem model (SubRoformer) was started first but was dropped as too slow on 2 CPU cores (~1 h ETA); speed was chosen over audio quality because only structure and data were needed.
3. **Tempo grid:** the drum stem's onset envelope is correlated against a beat comb over 118–130 BPM and fine offsets. Downbeat = the beat phase (of 4) with the most sub-120 Hz drum energy. The kick lands exactly on 1·5·9·13 of every 16th grid, which supports the fit.
4. **Per bar and per stem:** RMS level; "active" = within ~12 dB (vocals ~15 dB) of the stem's own 90th-percentile level. Bass pitch by pYIN (note per 16th). "Other" stem harmony by chroma + chord-template matching. Vocal pitch by pYIN. Drums by band-limited onsets on a 16-step grid (kick 30–120 Hz, snare/clap 150–2500 Hz, hat 6–16 kHz).
5. **Libraries used:** PyTorch, librosa, soundfile, mutagen, numpy/scipy (in throwaway virtual environments, since deleted).

---

## 2. What Is Verified, and What Is Not

### 2.1 From the file itself

- **File:** `0008_-_Deep_Inside.mp3`, MPEG-1 Layer III, 44.1 kHz stereo, 320 kbps, 15,776,748 bytes, **392.67 s**.
- **Tags:** Title `Deep Inside` · Artist `Hardrive` · Album **`Deep Inside (Remixes)`** · track 3/8 · Dance/Electronic · © 2015 Strictly Rhythm Records.
- **Therefore:** this is a track from a **2015 remixes release**, not the 1993 Original (6:28) or Dub (5:14) described in [jonty_first_track.md](./jonty_first_track.md) §2. Which remix it is is **not stated** in the tags.

### 2.2 Measured

- **Tempo:** **123.62 BPM**, constant-tempo fit (1 bar = **1.941 s**). Bar 1 starts at **0:01.49**. The audio ends at **202 bars**.
- **Bass key centre:** the bass stem is strongly **E minor / B minor family** (best key match E minor r≈0.90; B minor r≈0.51). The riff's long held note is **B**, with **E** and **F#** around it (§4). That fits **B minor** (as the repository notes state) but is equally consistent with E minor; I can't separate them from the bass alone.
- **Arrangement:** entry and exit bars per stem (§3).

### 2.3 Not verified

- **Chords *(low confidence)*:** the "other" stem is a mixed bed (keys, stabs, vocal chops, FX), and the template matcher returned an alternating `Dmaj7 / Gm7` pattern that does **not** line up with the bass notes (E, B, F#). I don't trust those chord names; the pitch-class spread of the other stem is nearly flat. Use the bass riff for harmony, not the chord labels.
- **Vocals *(low confidence)*:** pitched content sits mostly on **A, A#, B and C** (range G#3–C5, median A#4). I did not transcribe words.
- **What each stem actually contains** (piano? organ? which samples?) was not identified.

---

## 3. The Arrangement (Measured)

Clock = 0:01.49 + (bar − 1) × 1.941 s. "Bars" count from the first downbeat of the file.

**Bars 1–8 · 0:01 · Intro, no kick**
- Clap/snare and hat only (no kick); vocal-stem energy present from bar 1 *(may be sample bleed)*
- "Other" bed enters at bar 6

**Bars 9–24 · 0:17 · Kick in**
- Four-on-the-floor kick from bar 9
- Hat pattern thin; no bass yet (bass-stem level ≈ −55 dB = silence)

**Bars 25–56 · 0:48 · Bass drops, groove 1**
- Bass riff enters at bar 25 and stays, constant level
- Bar 33: busier hats (extra offbeat open-hat hits); "other" chords continue

**Bars 57–64 · 1:50 · Drum drop, vocal feature**
- Kick and most hats gone; clap on 1 and 3 only
- Vocal stem at its loudest of the first half; bass keeps playing

**Bars 65–88 · 2:06 · Full groove 2**
- Kick back at bar 65; full drums + bass

**Bars 89–96 · 2:52 · Break without bass**
- Bass stem silent (a few isolated low hits only); kick weakened to bar-1 hit plus ghost 2·3·4
- Drums and "other" continue

**Bars 97–128 · 3:08 · Full groove 3**
- Bass and kick back; vocal stem drops out around bars 105–112 (instrumental stretch)

**Bars 129–136 · 4:10 · Main breakdown**
- No kick, no bass, light hats; vocal stem loud (≈ −19 dB). Biggest drop in the file

**Bars 137–152 · 4:26 · Full groove 4**
- Everything back

**Bars 153–168 · 4:57 · Bass-forward**
- Bass at its loudest (−15 dB); "other" bed falls away; kick softens at 153–160

**Bars 169–184 · 5:28 · Bass out, vocal returns**
- Bass drops to near-silence at bar 169; kick continues; a repeating "other" stab *(A7-ish, low confidence)* appears from bar ~180; vocals return around bar 177

**Bars 185–192 · 5:59 · Drums strip**
- Kick gone; clap/hat only; stabs continue

**Bars 193–202 · 6:14 · Vocal outro**
- Drums, bass and other all out; vocal stem alone until the final silence at ~6:29 (bars 201–202)

### Active bar ranges (per stem, 1-based)

- **Drums:** 1–191
- **Bass:** 24–88 · 96–128 · 136–172
- **Other:** 6–156 · short stabs 180–192
- **Vocals (gated):** 1–34 · 38–72 · 78–88 · 90–103 · 112–152 · 179–200

Gaps in the vocal ranges are partly gating on a noisy stem. Re-check them by ear before relying on exact bars.

---

## 4. Cheat Card: The Groove on One Page

Sixteenth-note grid, 4 beats per bar, written `1 e & a 2 e & a 3 e & a 4 e & a`. `X` = strong hit, `x` = weaker hit, `.` = none (averaged over each 8-bar block).

**Kick (bars 9–152, main body):** `X...X...X...X...` — four on the floor.

**Clap/snare (typical full groove, bars 25–88):** `x...x...X..x.x..` — a clap on 3, softer on 1 and 2, plus off-beat ghosts around "4 e".

**Closed/open hat (bars 33–88):** `..X...X.x.XX.XX.` — hats on the "&" of 1, the "&" of 2, and a busy run through beat 3 and into 4. *(Band-energy split, so open-hat vs closed-hat isn't separated.)*

**Bass riff (one bar, repeated, bars 25–152):**

```
beat 1     beat 2     beat 3     beat 4
D# E E E | B  B  B  B | B  B  B  E | E  F# F# F#
```

- Reads as: chromatic lead-in **D#→E** on beat 1, a long **B** through beats 2–3, then **E** and **F#** on beat 4.
- Notes sit in the **B1–F#2** range (MIDI ~35–42, ≈ 62–92 Hz). Occasional variants: **C** or **A#** passing notes on beat 3, **D** or **D#** on the first sixteenth.
- Bars 89–96 use a different short fill (G1 · G1 · G#1 · B1 → G2 · F2 · D2) before the riff returns.

**Vocal (low confidence):** mostly A / A# / B / C around A#4 (written pitch range G#3–C5).

---

## 5. Per-Stem Data

### 5.1 Level per 8 bars (mean dB per stem)

| Bars | Clock | Drums | Bass | Other | Vocals |
|---|---|---|---|---|---|
| 1–8 | 0:01 | −20.7 | −57.7 | −37.0 | −18.7 |
| 9–16 | 0:17 | −13.7 | −59.1 | −26.8 | −23.4 |
| 17–24 | 0:33 | −13.6 | −54.1 | −25.6 | −23.2 |
| 25–32 | 0:48 | −13.8 | −17.2 | −26.3 | −22.6 |
| 33–40 | 1:04 | −13.6 | −17.4 | −22.9 | −27.4 |
| 41–48 | 1:19 | −13.8 | −17.2 | −24.6 | −23.6 |
| 49–56 | 1:35 | −14.3 | −17.1 | −24.4 | −22.9 |
| 57–64 | 1:50 | −21.1 | −17.5 | −23.7 | −18.2 |
| 65–72 | 2:06 | −13.8 | −17.1 | −26.8 | −22.3 |
| 73–80 | 2:21 | −13.7 | −17.2 | −22.8 | −29.1 |
| 81–88 | 2:37 | −13.8 | −17.8 | −25.6 | −24.5 |
| 89–96 | 2:52 | −17.1 | −56.1 | −26.1 | −25.5 |
| 97–104 | 3:08 | −13.9 | −17.2 | −24.5 | −28.9 |
| 105–112 | 3:23 | −13.5 | −17.0 | −27.6 | −56.9 |
| 113–120 | 3:39 | −13.6 | −17.1 | −25.7 | −24.4 |
| 121–128 | 3:55 | −14.8 | −17.5 | −24.3 | −23.7 |
| 129–136 | 4:10 | −20.4 | −50.2 | −22.4 | −19.0 |
| 137–144 | 4:26 | −13.8 | −17.2 | −24.5 | −23.6 |
| 145–152 | 4:41 | −13.9 | −17.2 | −25.5 | −23.1 |
| 153–160 | 4:57 | −17.7 | −14.9 | −35.6 | −62.7 |
| 161–168 | 5:12 | −14.9 | −15.9 | −45.0 | −59.6 |
| 169–176 | 5:28 | −13.5 | −41.8 | −52.6 | −56.9 |
| 177–184 | 5:43 | −13.9 | −61.0 | −32.9 | −28.2 |
| 185–192 | 5:59 | −22.0 | −56.4 | −33.6 | −16.6 |
| 193–200 | 6:14 | −63.8 | −69.7 | −48.6 | −16.4 |
| 201–202 | 6:30 | −76.8 | −75.3 | −75.8 | −72.4 |

A stem is treated as "absent" below about −45 dB.

### 5.2 Bass

- **Pitch classes (share of voiced frames):** G 0.27 · E 0.24 · B 0.19 · F# 0.11 · D 0.07; everything else ≤ 0.02. The G share comes mostly from the short high notes in the intro and bar 89–96 fill, not the main riff, so don't read it as a G root.
- **Range:** about MIDI 31–67 overall; the riff itself is B1–F#2.
- **Key candidates (Krumhansl-Schmuckler on the bass pitch classes):** E minor 0.90 · G major 0.68 · B minor 0.51.

### 5.3 "Other" stem

- **Pitch classes:** nearly flat (every class 5–11%), so the key cannot be read from it. Best key match was D major (0.64) then B minor (0.48), which is weak.
- **Chord labels:** an alternating two-bar pattern labelled `Dmaj7 / Gm7` for bars 17–112 and 137–160 (low confidence, see §2.3), with `Amaj7 / A7 / F#m7 / Gm7`-type labels in bars 1–16 and 113–136 and an `A7` stab bed in bars 177–192.

### 5.4 Vocals

- **Pitch classes:** A 0.32 · A# 0.22 · B 0.22 · C 0.09 · G# 0.06.
- **Range:** G#3 – C5 (5th–95th percentile), median A#4.

### 5.5 Drums (16-step grids per 8-bar block, kick · clap/snare · hat)

| Bars | Kick | Snare/clap | Hat |
|---|---|---|---|
| 1–8 | `................` | `X.......X..x....` | `X...x...X..x....` |
| 9–16 | `X...X...X...X...` | `X...x...X..xxx..` | `........x.xx.X..` |
| 25–32 | `X...X...X...X...` | `x...x...X..x.x..` | `........x.xx.X..` |
| 33–40 | `X...X...X...X...` | `x...X...X..x.x..` | `..x...X.x.X..XX.` |
| 57–64 | `................` | `X.......X..x....` | `x.......X..x....` |
| 65–72 | `X...X...X...X...` | `x...x...X..x.x..` | `..X...X.x.XX.XX.` |
| 89–96 | `X...x...x...X...` | `x.......X..x....` | `x.x...x.x.x..xx.` |
| 113–120 | `X...X...X...X...` | `........x..x.x..` | `..xx..x...X..XX.` |
| 129–136 | `................` | `X.......X..X....` | `x.......x..x....` |
| 153–160 | `X...X...x...x...` | `x.......X..x....` | `........x..x....` |
| 169–176 | `X...X...X...X...` | `...........x.X..` | `..x...x...x..Xx.` |
| 185–192 | `................` | `X.......X..x....` | `x.......x..x....` |
| 193–202 | `................` | `................` | `................` |

Snare/clap and hat patterns here are band-energy proxies from a low-quality stem, so the exact placement of ghost hits is approximate.

---

## 6. Using This With Jonty's Build

[jonty_first_track.md](./jonty_first_track.md) uses five 32-bar patterns (160 bars). This file is **202 bars**, so it does not fit neatly; to line the two up:

- **Intro, drum-led (bars 1–24):** matches Jonty's `U41` idea, except here the kick enters at **bar 9** and the bass at **bar 25**.
- **Groove (bars 25–56, 65–88):** the `U42` groove, with the bass riff in §4.
- **Break (bars 57–64, 89–96, 129–136):** short 8-bar drops, not one long break; the big one (129–136) removes kick and bass entirely and features the vocal.
- **Peak / bass-forward (bars 153–168):** bass loudest, other bed leaves.
- **Outro (bars 185–202):** drums strip, then vocal alone.
- **Tempo and key:** use **124 BPM** (measured 123.6) and a **B** root for the bass; keep the repository's B minor for the hook but verify by ear.
- Entry bars in §3 can replace the "model" entry bars in Jonty's §3 if you want the build to follow this version.

---

## 7. Access Log

- **Earlier attempts to listen online** (YouTube, SoundCloud, Bandcamp, Spotify) failed with `ERR_BLOCKED_BY_CLIENT`; web-fetch of SoundCloud, Bandcamp and Insomniac failed on DNS.
- **Model weights:** Meta, Hugging Face and Zenodo hosts were unreachable from this environment, so the weights were taken from the GitHub release assets of the Music-Source-Separation-Training repository. DrumSep (kick/snare/cymbals/toms splitting) was available but not run.
- **Not stored:** the separated stems and analysis JSON were temporary and have been deleted.

## 8. Sources

- File tags and audio: the uploaded `0008_-_Deep_Inside.mp3`.
- [Music-Source-Separation-Training](https://github.com/ZFTurbo/Music-Source-Separation-Training) (SCNet checkpoint, release v.1.0.6; SubRoformer v1.0.23).
- Release facts about the 1993 record (Discogs: https://www.discogs.com/release/20174-Hardrive-Deep-Inside · diggerdigger: https://diggerdigger.com/track/hardrive-deep-inside/ · Insomniac: https://www.insomniac.com/music/from-the-crate-hardrive-deep-inside/), as quoted in [jonty_first_track.md](https://github.com/threadkeeper/roland-mc303-notes/blob/119af77c63ad53365b90d77796e8ecc48cb478b/jonty_first_track.md). The vocal reportedly samples Barbara Tucker's "Beautiful People".
