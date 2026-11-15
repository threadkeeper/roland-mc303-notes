# Deep Inside · MC-303 Instructions

**Hardrive · uploaded track · 123.6 BPM · 202 bars · `U31`–`U37` · Song `S-3`**

A full-song, compact pass-grid recipe, using [record_cheat.md](./record_cheat.md) step 47 instead of repeating its button instructions. [raw.md](./raw.md) explains the reviewed evidence; [`analysis/deep_inside/data/`](./analysis/deep_inside/data/) holds the measurements.

> **Read first:** this is a data-informed MC-303 interpretation, **not a verified transcription**. No audio was heard here and no physical MC-303 was tested. Tempo, section changes and the bass's G1/B1 alternation have stronger evidence than the piano voicings, vocal pitches or exact ghost hits. Sound settings and velocities below are audition starting points, not recovered settings from the record.

## 1. Source, Slots & Sound Choices

The tags say *Deep Inside (Remixes)*, 2015, track `3/8`, but the title is just *Deep Inside*. The [eight-track release](https://music.apple.com/jp/album/deep-inside-remixes/986139771) lists an unnamed *Deep Inside* in that position. This is **consistent with a reissued original**, not proof of a newly made remix or a remaster. This recipe follows the uploaded audio, whichever mastering it is.

Keep Jonty's `U41`–`U45` / `S-2` untouched. Check that **all seven `U31`–`U37` slots and `S-3` are empty or disposable** before copying. The MC-303 has `U01`–`U50`, ten Songs, eight Parts and 28-voice polyphony.

| Part | Start with | Audition alternative |
|---|---|---|
| `R` drums | `d07` House | Keep this kit for the documented pad map |
| `1` keys | `t10-02` bright piano | `t11-04` percsv organ; compare without adding another layer |
| `2` vocal proxy | `t07-05` auh | `t07-08` auh auh; check its articulation before adding repeated hits |
| `3` bass | `t02-11` house bass | `t02-08` 101 bass 1 or `t02-12` sine bass |

These are actual bank choices from [sample_bank.md](./sample_bank.md), **not identified original instruments**. The MC-303 cannot import a vocal sample: an "auh" patch cannot reproduce Barbara Tucker's words or performance. Authorised external sample playback, synchronised by MIDI, is the route to a much closer vocal; it is not required for this MC-303-only build.

**Do not force everything into B minor.** The measured G1, B1, D2, E2 and F#2 are worth keeping. The composite keys stem suggests more chromatic harmony, but its chord identity remains uncertain.

## 2. Arrangement & Clock

The reviewed first downbeat is about **0:00.032**, not 0:01.973. Clock = `0.032 + (bar − 1) × 240/123.62` seconds.

```text
Pattern  Bars       Audio clock
U31      1–32       0:00
U32      33–64      1:02
U33      65–96      2:04
U34      97–128     3:06
U35      129–160    4:09
U36      161–192    5:11
U37      193–202    6:13
```

Each symbol = eight bars: `#` on, `s` sparse, `w` weak kick, `m` medium kick, `+` part of the block, `.` off. This is the **core recipe**, not an assertion that every stem is clean.

```text
Bar    1   |33  |65
Pat    U31 |U32 |U33
Kick   .###|###.|###w
Clap   ####|####|####
Hat    .sss|###.|###.
Keys   +###|####|####
Voice  ####|####|####
Bass   ...#|####|###.
A-end  ...G|DGDG|DGD.
```

```text
Bar    97  |129 |161
Pat    U34 |U35 |U36
Kick   ####|.##w|m##.
Clap   ####|####|####
Hat    ####|.##.|s##.
Keys   ####|###+|..+#
Voice  #.##|###.|..+#
Bass   ####|.###|#+..
A-end  DGDG|.GDG|DG..
```

`A-end` selects the A bar's **G** or **D** ending (§3). `U37`: voice on local bars `1–8`; local `9–10` are empty. No new drums, keys or bass.

**Landmarks:** kick in `9`; bass in `25`; kick/hat drop `57–64` with bass continuing; bass out and kick weaker `89–96`; voice absent `105–112`; kick/bass out `129–136`; bass-forward `153–168`; last bass through about `172`; voice returns about `179`, keys stabs about `181`; kick/hats out `185`; voice-led outro `193–200`.

The stem levels suggest some transition tails beyond those ranges. Do not turn every tail into a new note. At `123.6`, 202 bars take **6:32.2**; the MP3 also has a short leading offset and about **0.47 s of partial final-bar tail**. The data includes that tail as analysis bar `203`, but the Song does not need an extra whole bar.

## 3. Cheat Card

`Step 1/5/9/13` = beats `1/2/3/4`. A hit is a note onset, **not a command to re-tap a held note on every occupied step**.

```text
Step   1e&a 2e&a 3e&a 4e&a
Kick   X... X... X... X...
Clap   .... X... .... X...
Hat    ..X. ..X. ..X. ..X.
Thin   .... ..X. .... ..X.
```

**Drums · `d07` · `OCTAVE -2`**

Kick pad `2` · clap `5` · open hat `12` · closed hat `8` · crash `15`. The separated `hh` lane does **not** distinguish open from closed hats. Open-hat assignment is an approximation; closed hats and crashes are optional, not mandatory layers.

### Bass: two bars, not one

Record **five semitones above the target at `OCTAVE -2`**, then Transpose **Part 3 by `-5` once** in each used pattern. All required pitches now fit the pads, including the real low G1, without an octave climb.

```text
Target    G1  B1  D2  E2  F#2 G2
Rec pad    2   6   9  11   13 14
```

This uses `note = 58 + 12 × octave + pad`. The pads initially sound C2 / E2 / G2 / A2 / B2 / C3; the edit restores the measured pitches.

```text
Cell  Step → record pad (gate in 16ths)
A-G    1→2(6)  8→14(3) 11→14(2)
      13→9(1) 14→11(3)
A-D    1→2(6)  8→14(2) 11→9(3)
      14→11(3)
B      1→6(6)  8→11(2) 11→13(3)
      14→11(3)
```

Play `A, B, A, B…`. Use the `A-end` row in §2 to choose A-G or A-D for each eight-bar block. B stays the same. Local odd bars are A, even bars B. Exact transitions can be a sixteenth early or late; these are simplified from onset candidates plus independent YIN pitch checks.

**Hold the root for roughly six sixteenths**, rather than tapping everything short. Step Recording 1 / ties is easier for this than realtime tapping: [record_cheat.md §4C](./record_cheat.md). It overwrites from its start point: use an empty cell or set the start to the pass's first bar, not blindly bar 1 over existing bass. Gates above are starting lengths, not exact recovered durations.

### Keys: candidate voicings, not a proven chord chart

Record Part 1 **two semitones above target at `OCTAVE 0`**, then Transpose **Part 1 by `-2` once** in each used pattern.

```text
Early/late: pad 13 · steps 1 5 13
Final pitch: A4

Keys A: pads 2+9 · steps 1 7
Final pitches: A#3 + F4
Optional pad 6 on step 1 adds D4

Keys B: pads 1+6+10 · step 1
        pad 10 · steps 4 9 13
Final pitches: A3 + D4 + F#4
```

The paired/stacked notes are stronger candidates than the old invented A4/A#4/G4 melody, but **not confirmed piano chords**. Alternate Keys A/B by local odd/even bar. Hold the first chord about `3–5` sixteenths; later stabs about `1`. Do not use a factory "organ chord" patch as though it had these known intervals.

### Voice: syllable/rhythm proxy only

Part 2 · `OCTAVE 0` · **no transpose**.

```text
Intro/break/outro:
pad 11 (A4) · steps 1 5 13
pad 12 (A#4) · step 9

Body:
pad 13 (B4) · steps 1 13
pad 12 (A#4) · step 9
```

Short `1–2`-sixteenth syllables; vary or omit a hit rather than making an uninterrupted choir. These approximate registers and rhythms, **not the sampled vocal's exact melody**. On the very first bar omit step `1`; the detected vocal starts around beat 2.

## 4. Setup & Pass Routine Overrides

Use [Jonty §5 Phase A](./jonty_first_track.md) steps `1–10`, with `U31`–`U37`, tempo `123.6` and the Tones in §1. When borrowing a template, erase **notes and Modify data on all eight Parts in the copy**, not just Parts 1/R; leave the source alone. Reset inherited synth LFO/envelope/filter offsets before the SETUP copies so the old lead's modulation is not mistaken for this track.

**Lengths:** `U31`–`U36` = `32`; **`U37` = `10`**. `LGH` supports `1–32` measures ([record_cheat.md §4A](./record_cheat.md)). If a template or pass has already made `U37` 32 bars, shorten it with **Delete Measure, all eight Parts, `PHRASE`, first bar `11`, count `22`** (§4E). This preserves the first ten bars and setup. No manual-stop workaround is needed.

Do Jonty steps `11–12`: sixteenth Grid resolution, full timing strength, note the old Pad Velocity and free memory. Then repeat **record_cheat.md step 47 (a–h)** for the numbered passes below, with these overrides:

1. Select the pass's **Part**, not always R.
2. Use `LGH 10` for **every U37 pass**; other patterns use `32`. Keep `4-4`, `Cnt 1`, `LoP on`.
3. **Part 2: skip step 47e.4 and turn Play Quantize completely off while recording.** Excluding Part 2 from the normal quantize aim is not enough: during recording quantize applies to the Recording Part. Restore Grid for Parts 1/3/R.
4. Play **only** the listed ranges; stay silent for the rest. Stop in the blank Loop Rest bar after the actual pattern length.

Passes descend `OCTAVE 0 → -2`. Faulty SHIFT/SELECT/octave controls: use [repair.md](./repair.md) / Jonty §1.4. Transpose's Pad `6` shortcut in [next_steps.md §3](./next_steps.md) is inferred: check that the menu really is Transpose before executing, and cancel if not.

## 5. Synth Passes

### Part 1 · Keys

**Pass 1 · `U31` · `OCTAVE 0` · Velocity `90`**
- Early cell · bars `6–32`; bar `6` has step `13` only.

**Pass 2 · `U32` · `OCTAVE 0` · Velocity `90`**
- Keys A/B · bars `1–32`.

**Pass 3 · `U33` · `OCTAVE 0` · Velocity `90`**
- Keys A/B · bars `1–32`.

**Pass 4 · `U34` · `OCTAVE 0` · Velocity `90`**
- Keys A/B · bars `1–32`.

**Pass 5 · `U35` · `OCTAVE 0` · Velocity `90`**
- Keys A/B · bars `1–28`; let bars `25–28` thin out.

**Pass 6 · `U36` · `OCTAVE 0` · Velocity `90`**
- Late cell · bars `21–32`.

Now Transpose **Part 1, `-2`, once in each U31–U36**. Do not transpose Parts R/2/3.

### Part 2 · Voice · Quantize OFF

**Pass 7 · `U31` · `OCTAVE 0` · Velocity `90`**
- Intro cell · bars `1–24`; body cell · bars `25–32`.

**Pass 8 · `U32` · `OCTAVE 0` · Velocity `90`**
- Body cell · bars `1–24`.

**Pass 9 · `U33` · `OCTAVE 0` · Velocity `90`**
- Body cell · bars `1–32`; keep bars `25–32` sparser.

**Pass 10 · `U34` · `OCTAVE 0` · Velocity `90`**
- Body cell · bars `1–8` and `17–32`; nothing in `9–16`.

**Pass 11 · `U35` · `OCTAVE 0` · Velocity `90`**
- Body cell · bars `9–24`.

**Pass 12 · `U36` · `OCTAVE 0` · Velocity `90`**
- Outro cell · bars `19–24`.

**Pass 13 · `U37` · `OCTAVE 0` · Velocity `90`**
- Outro cell · bars `1–8`; silent `9–10`; **LGH `10`**.

**Pass 14 · `U32` · `OCTAVE 0` · Velocity `105`**
- Break cell · bars `25–32`.

**Pass 15 · `U35` · `OCTAVE 0` · Velocity `105`**
- Break cell · bars `1–8`.

**Pass 16 · `U36` · `OCTAVE 0` · Velocity `105`**
- Outro cell · bars `25–32`.

### Part 3 · Bass · Grid ON

Use the **record pads**, not the target note names; alternate A/B and follow `A-end` in §2.

**Pass 17 · `U31` · `OCTAVE -2` · Velocity `100`**
- Bass · bars `25–32`.

**Pass 18 · `U32` · `OCTAVE -2` · Velocity `100`**
- Bass · bars `1–32`, including the drum drop.

**Pass 19 · `U33` · `OCTAVE -2` · Velocity `100`**
- Bass · bars `1–24`.

**Pass 20 · `U34` · `OCTAVE -2` · Velocity `100`**
- Bass · bars `1–32`.

**Pass 21 · `U35` · `OCTAVE -2` · Velocity `100`**
- Bass · bars `9–24`.

**Pass 22 · `U36` · `OCTAVE -2` · Velocity `100`**
- Bass · bars `9–12`.

**Pass 23 · `U35` · `OCTAVE -2` · Velocity `110`**
- Bass · bars `25–32`, the bass-forward stretch.

**Pass 24 · `U36` · `OCTAVE -2` · Velocity `110`**
- Bass · bars `1–8`.

Now Transpose **Part 3, `-5`, once in each U31–U36**. Never repeat the edit after a playback check. No transpose on drums.

## 6. Drum Passes

All on **Part R**, `d07`, `OCTAVE -2`. The core has no obligatory closed-hat, ride, tom or crash layer.

### Hats · Soft

**Pass 25 · `U31` · `OCTAVE -2` · Velocity `80`**
- Hat pad `12` · steps `7 15` · bars `9–32`.

**Pass 26 · `U32` · `OCTAVE -2` · Velocity `80`**
- Hat pad `12` · steps `3 7 11 15` · bars `1–24`.

**Pass 27 · `U33` · `OCTAVE -2` · Velocity `80`**
- Hat pad `12` · steps `3 7 11 15` · bars `1–24`.

**Pass 28 · `U34` · `OCTAVE -2` · Velocity `80`**
- Hat pad `12` · steps `3 7 11 15` · bars `1–32`.

**Pass 29 · `U35` · `OCTAVE -2` · Velocity `80`**
- Hat pad `12` · steps `3 7 11 15` · bars `9–24`.

**Pass 30 · `U36` · `OCTAVE -2` · Velocity `80`**
- Hat pad `12` · steps `3 7 11 15` · bars `9–24`.

**Pass 31 · `U36` · `OCTAVE -2` · Velocity `60`**
- Hat pad `12` · steps `7 15` · bars `1–8`.

### Main Kick & Clap · Loud

Kick pad `2` · steps `1 5 9 13`; clap pad `5` · steps `5 13`. On beats 2/4, both pads sound together.

**Pass 32 · `U31` · `OCTAVE -2` · Velocity `110`**
- Kick · bars `9–32`; clap · bars `1–32`.

**Pass 33 · `U32` · `OCTAVE -2` · Velocity `110`**
- Kick · bars `1–24`; clap · bars `1–32`.

**Pass 34 · `U33` · `OCTAVE -2` · Velocity `110`**
- Kick · bars `1–24`; clap · bars `1–32`.

**Pass 35 · `U34` · `OCTAVE -2` · Velocity `110`**
- Kick and clap · bars `1–32`.

**Pass 36 · `U35` · `OCTAVE -2` · Velocity `110`**
- Kick · bars `9–24`; clap · bars `1–32`.

**Pass 37 · `U36` · `OCTAVE -2` · Velocity `110`**
- Kick · bars `9–24`; clap · bars `1–32`.

### Weak/Medium Kick · Keep All Four Beats

These velocities approximate the change in weight; the stem data does not reveal the original drum machine's velocity or filter setting.

**Pass 38 · `U33` · `OCTAVE -2` · Velocity `80`**
- Kick pad `2` · step `1` · bars `25–32`.

**Pass 39 · `U35` · `OCTAVE -2` · Velocity `80`**
- Kick pad `2` · step `1` · bars `25–32`.

**Pass 40 · `U33` · `OCTAVE -2` · Velocity `45`**
- Kick pad `2` · steps `5 9 13` · bars `25–32`.

**Pass 41 · `U35` · `OCTAVE -2` · Velocity `45`**
- Kick pad `2` · steps `5 9 13` · bars `25–32`.

**Pass 42 · `U36` · `OCTAVE -2` · Velocity `90`**
- Kick pad `2` · steps `1 5 9 13` · bars `1–8`.

**Optional accents — audition, don't assume:** clap pad `5` on `8 10`, velocity `40`, in full grooves only; sparse closed hat pad `8` on `4 12`, velocity `40`; a quiet crash pad `15` on the first kick/return only. Split these into ordinary extra passes if wanted. Busy even-step closed hats can repeatedly choke open hats; don't add eight per bar just because a house template did.

The weak hat activity in `89–96` is omitted from the core. Add soft offbeats there only if your comparison supports them. Low-energy tom/ride/crash candidates are preserved in the data, not silently deleted, but **do not prove those instruments are absent or present**.

## 7. Shape, Copy & Finish

**Sound baseline:** start synth filter/resonance/envelope offsets at `0`, LFO MOD at `0`, centred pan and no portamento sweeps. Keep bass and drums dry. Compare the bass's held gates first; only then try a modest cutoff/decay reduction. These are rompler offsets, not measured filter frequencies.

**Space:** [next_steps.md §2](./next_steps.md) has the menus. Try Plate, overall level about `25`, Part 1 send `15`, Part 2 send `35`, Parts 3/R send `0`; Chorus off initially. These are **unverified starting values**. Delay/Reverb is one processor: choose delay **instead of** Plate if a rhythmic voice repeat is more useful. At this tempo an eighth is ~`243 ms`, a dotted eighth ~`364 ms`; the `0–127` TIME value is not a millisecond read-out.

**Automation:** if the keys should fall away more naturally, record a Part 1 LEVEL fade over `U35` bars `25–28`, then stay down through `32` (record_cheat.md Phase 4). Write the intended starting setup **before** the automation, not the faded end value afterwards. Keep drum changes in note velocities: a Part R filter/level sweep affects the kit, not just the kick.

**Less tapping:** get one A/B cell right, then use Part Copy `PHRASE` ([record_cheat.md Phase 12](./record_cheat.md)) to reuse it in empty destination ranges. Copy the correct A-G/A-D ending **before the transpose checkpoint**, then lower each Part once. If instead you copy completed, lowered notes, skip that destination's transpose and do not add raised record pads over them. Copying replaces destination data, not merges it.

**Finish:** use Jonty steps `21–29`, with these changes:

1. Edit Quantize **R/1/3 only**, Grid `16`, in `U31`–`U36`; leave Part 2 alone. Start straight rather than assuming an unmeasured 58% swing.
2. Confirm all six transposed bass Parts and keys Parts sound in their **target** registers, and `U37` really is ten bars.
3. Chain **`S-3 = U31 U32 U33 U34 U35 U36 U37`**, Song Loop off, Song Setup Write at **`123.6`**. Store deliberate Part levels/effect sends with safe Pattern Setup Write.
4. Restore Pad Velocity/quantize/mutes, check free memory, then Bulk Dump. Do not wipe the source patterns or Jonty's Song.

**If it sounds wrong:** fix a specific gate, voicing or misplaced hit in a copy. Do not randomly transpose the whole bass or replace E with F# to "find the key". A voice Tone will still sound unlike the actual sample; more choir notes cannot solve that limitation.
