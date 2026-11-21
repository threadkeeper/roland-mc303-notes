# Deep Inside · MC-303 · V2

**Empty patterns → drums → keys → voice → bass → finished Song**

`U31`–`U36`: 32 bars each. `U37`: 10 bars.
Song `S-3`: 202 bars at `123.6` BPM, about **6:32**.

This is an MC-303 interpretation, not an exact recreation. Part 2 uses a voice Tone instead of the sampled words.

> **Verification note:** Nothing here has been tested on a physical MC-303. The button routines follow the Owner's Manual and [record_cheat.md](./record_cheat.md). The notes and bar ranges follow [the original instructions](./deep_inside_instructions.md); their analysis is not a verified transcription. Transpose's Pad `6` shortcut is *(unconfirmed)*: check the command before executing it.

Read downwards. All the instructions needed for this build are here. **Bars on a pass card mean bars inside that pattern**, not bars counted from the start of the Song.

## Phase 1: Reserve Seven Empty Patterns

1. Press **`[STOP]`**.
2. Press **`[PLAY MODE]`** until **PATTERN** is lit.
3. Turn **`[PTN SET]`**, **`[RPS SET]`**, **`[ARPEGGIO ON]`**, **`[TRANSPOSE]`** and **`[FUNC]`** off if lit/blinking.
4. Press **`SELECT [<] / [>]`** until **PTN/SONG** is lit.
5. Turn **`[VALUE]`** through `u31`–`u37`. A lowercase `u` means empty. **Do not overwrite a pattern you want to keep.** This build leaves `U01`, `U02`, `U41`–`U45`, `S-1` and `S-2` alone.
6. Check `S-3` too: press **`[PLAY MODE]`** until SONG is lit, select **PTN/SONG**, then turn **`[VALUE]`** to `S-3`. `NEXT = ---` means empty. If it contains a song you want, stop here and choose other slots before following this recipe.
7. Return to **PATTERN** mode.
8. Note your current Pad Velocity: hold **`[SHIFT]`**, press Pad **`[16]`**, press **`SELECT [>]` seven times**, write down the `PuL` value, then press **`[EXIT]`**.
9. Note free memory: hold **`[SHIFT]`**, press Pad **`[16]`**, press **`SELECT [>]` eight times**, write down the remaining %, then press **`[EXIT]`**.

**Only if a reserved pattern contains disposable data**, clear it before continuing:

- Stopped in PATTERN mode, select that pattern and check its number.
- Hold **`[SHIFT] + [FUNC]`**, press Pad **`[4]`** (Delete Measure).
- Press the PART buttons so **all eight Parts, R and 1–7, are selected**.
- Turn **`[VALUE]`** to data type **`ALL`**, then press **`[ENTER]`**.
- Leave the first bar at **`1`**, then press **`[ENTER]`**.
- Turn **`[VALUE]`** to measure count **`ALL`**.
- Press **`[ENTER]`** for `SUrE`, then **`[ENTER]`** again.
- Check the pattern now shows a lowercase `u`. Repeat only for disposable reserved slots.

## Phase 2: Set Up Each Pattern

Do steps **10–19 for `U31`, then repeat for `U32` through `U37`**. Starting each from empty avoids bringing old notes or knob automation into this track.

10. Select the empty pattern: **SELECT → PTN/SONG → `[VALUE]`**.
11. Press **`[PART SELECT]`** so it lights steadily. Set these four sounds, one Part at a time:
    - Press **`PART [R]`** → SELECT to **TONE** → `[VALUE]` to **`d07`** (House).
    - Press **`PART [1]`** → SELECT to **TONE** → `[VALUE]` to **`t10-02`** (bright piano).
    - Press **`PART [2]`** → SELECT to **TONE** → `[VALUE]` to **`t07-05`** (auh).
    - Press **`PART [3]`** → SELECT to **TONE** → `[VALUE]` to **`t02-11`** (house bass).
12. Set a plain starting sound on **each of Parts 1, 2 and 3**. Select the Part, then set the following. To read an exact knob value, hold **`[SHIFT] + [FUNC]` while turning it**.
    - `[FUNC]` dark: **CUTOFF `0`**, **RESONANCE `0`**.
    - `[FUNC]` dark, `[ENVELOPE]` dark: ENVELOPE knob → **ATTACK `0`**.
    - `[FUNC]` dark, `[ENVELOPE]` lit: ENVELOPE knob → **DECAY `0`**.
    - `[FUNC]` dark, `[LFO]` dark: LFO knob → **RATE `0`**.
    - `[FUNC]` dark, `[LFO]` lit: LFO knob → **MOD `0`**.
    - `[FUNC]` blinking: ENVELOPE knob → **RELEASE `0`**; RESONANCE knob → **PAN `0`**; LFO knob → **PORTA TIME `0`**.
    - `[FUNC]` blinking: CUTOFF knob → **LEVEL `100`**.
    - Return `[FUNC]` to **dark**.
13. Select **Part R**, then set **LEVEL `100`** with `[FUNC]` blinking and the CUTOFF/LEVEL knob. Return `[FUNC]` to dark.
14. Keep this build dry:
    - Hold **`[SHIFT]`**, press Pad **`[6]`** (Delay/Reverb Part level).
    - Press **`PART [R]`**, turn `[VALUE]` to **`0`**. Repeat for **Parts 1, 2 and 3**, then `[EXIT]`.
    - Hold **`[SHIFT]`**, press Pad **`[8]`** (Flanger/Chorus Part level).
    - Set **R, 1, 2 and 3** to **`0`** in the same way, then `[EXIT]`.
15. SELECT to **TEMPO**. Turn **`[VALUE]`** to **`123.6`**. Hold `[SHIFT]` while turning for whole-BPM changes; release it for tenths. **Do not change patterns yet.**
16. Press **`[REC]`** once. It blinks. Use **SELECT and `[VALUE]`** to set:
    - **`bEt` = `4-4`**
    - **`LGH` = `32`** for `U31`–`U36`; **`10` for `U37`**
    - **`Cnt` = `1`**
    - **`LoP` = `on`**
17. Press **`PART [R]`**, then **`[PLAY]`**. After the four count-in clicks, **play nothing and turn no knobs** for the whole pattern. Watch `NEXT` for the bar.
18. After bar **32** (or **10** in `U37`), press **`[STOP]`** in the blank Loop Rest bar. This establishes the length without adding notes.
19. Save the sounds and tempo: hold **`[SHIFT] + [FUNC]`**, press Pad **`[15]`** (`SUrE`), then press **`[ENTER]`**. Now repeat steps 10–19 for the next reserved pattern.

**Checkpoint:** all seven patterns have their sounds saved. `U31`–`U36` are 32 bars; `U37` is 10. They have no notes yet. Do not chain the Song until recording is finished.

## Phase 3: Set the Click and Recording Grid

20. Stopped, hold **`[SHIFT]`**, press Pad **`[16]`**, press **`SELECT [>]` five times** to Metronome Mode, turn **`[VALUE]`** to **`rEC`**, then **`[EXIT]`**. If you cannot hear the click while recording, **`[FUNC] + [SCALE/MEASURE]`** toggles it.
21. Hold **`[SHIFT]`**, press Pad **`[2]`** (Grid resolution), turn **`[VALUE]`** to **`16`**, then **`[EXIT]`**.
22. With **`[FUNC]` dark**, turn **TIMING fully clockwise** (100%).
23. Hold **`[SHIFT]`**, press **`[PART SELECT / QUANTIZE SELECT]`**. Make **only R, 1 and 3 selected**; Part 2 must be off. Press **`[PART SELECT]`** to return to steady lighting. Exiting this selection view is *(unconfirmed)*; if it still blinks, press `[EXIT]`.

**Counting the taps:** one bar has sixteen steps. These are timing positions, **not sixteen different pads to press** in realtime recording.

```text
Step  1e&a 2e&a 3e&a 4e&a
Beat  1    2    3    4
```

Step **1** = beat 1, **5** = beat 2, **9** = beat 3, **13** = beat 4.

**Reading the pass grids:** each row is a **pad number**; each group of four columns is one beat. `X` = press that pad, `.` = do not press it. Aligned `X`s on different rows mean **press those pads together**. Repeat the displayed bar across the stated bar range only. All unlisted bars are silent for that pass.

## Phase 4: The Realtime Pass Routine

Repeat **A–H for every realtime pass card** in Phases 5, 6 and 7. The bass has its own step-entry routine in Phase 8.

**A. Select the pattern**

- Press `[STOP]`. Check **PATTERN** is lit.
- SELECT to **PTN/SONG**, turn `[VALUE]` to the card's pattern.
- Press **`[SHIFT] + [BWD]`** to return to the beginning.

**B. Select the Part**

- Press **`[PART SELECT]`** (steady), then the card's **PART button**.
- `[PTN SET]`, `[RPS SET]`, `[ARPEGGIO ON]`, `[TRANSPOSE]` and `[FUNC]` must be dark.

**C. Set the octave**

- Press **`OCTAVE [-] / [+]`** until the display shows the card's octave.
- At **`0`**, neither octave LED is lit.
- Tap the listed pads to check the sounds **before recording**.

**D. Set Pad Velocity**

- Hold **`[SHIFT]`**, press Pad **`[16]`**.
- Press **`SELECT [>]` seven times** to `PuL`.
- Turn **`[VALUE]`** to the card's velocity, then **`[EXIT]`**.

**E. Arm recording**

- Press **`[REC]` once**: REC blinks.
- If you see **`SnG / CLr`**, press **`[EXIT]`**, not ENTER. Return to PATTERN mode and select the correct pattern.
- Check **`bEt 4-4`**, **`LGH 32`** (**`10` for `U37`**), **`Cnt 1`**, **`LoP on`** with SELECT and `[VALUE]`.
- Press the card's **PART button again** to choose the Recording Part.
- For **keys or drums**, press **`[QUANTIZE]`** until **GRID** lights.
- For **voice**, press **`[QUANTIZE]`** until **GRID, GROOVE and SHUFFLE are all dark**. Merely excluding Part 2 in step 23 is not enough during recording.

**F. Record**

- Press **`[PLAY]`**. Wait for the **four count-in clicks**.
- Watch `NEXT` for the bar. Play **only the pads, steps and bars on the card**.
- Stay silent in every unlisted bar. **Hands off the knobs.**
- Already recorded Parts play along; **do not play their notes again**.

**G. Stop**

- Let the entire pattern finish, even if your last notes were earlier.
- Press **`[STOP]`** in the blank Loop Rest bar after bar **32**, or **10 for `U37`**.
- Do not let it loop into bar 1: another take adds notes on top.

**H. Listen**

- Press **`[SHIFT] + [BWD]`**, then **`[PLAY]`** to check the pass.
- Press **`[STOP]`** before the next card.
- **Do not run Setup Write after each pass.** Your starting sounds are already saved.

## Phase 5: Record the Drums First · Part R

Use realtime routine **A–H**. Finish **all Part R passes before recording the keys or voice**, so the drums play along as your rhythm guide. The intentional drum gaps stay empty; use the metronome there.

All cards use **`d07`**, **`OCTAVE -2`**, **GRID on**, **`LGH 32`**. Pad **`2`** = kick, **`5`** = clap, **`12`** = open hat.

### Main Kick and Clap

**Pass 1 · `U31` · Part `R` · `OCTAVE -2` · Velocity `110`**

```text
U31 · R · OCT -2
Bars 1-8
Pad  1e&a 2e&a 3e&a 4e&a
05   .... X... .... X...

Bars 9-32
Pad  1e&a 2e&a 3e&a 4e&a
02   X... X... X... X...
05   .... X... .... X...
```

**Pass 2 · `U32` · Part `R` · `OCTAVE -2` · Velocity `110`**

```text
U32 · R · OCT -2
Bars 1-24
Pad  1e&a 2e&a 3e&a 4e&a
02   X... X... X... X...
05   .... X... .... X...

Bars 25-32
Pad  1e&a 2e&a 3e&a 4e&a
05   .... X... .... X...
```

**Pass 3 · `U33` · Part `R` · `OCTAVE -2` · Velocity `110`**

```text
U33 · R · OCT -2
Bars 1-24
Pad  1e&a 2e&a 3e&a 4e&a
02   X... X... X... X...
05   .... X... .... X...

Bars 25-32
Pad  1e&a 2e&a 3e&a 4e&a
05   .... X... .... X...
```

**Pass 4 · `U34` · Part `R` · `OCTAVE -2` · Velocity `110`**

```text
U34 · R · OCT -2
Bars 1-32
Pad  1e&a 2e&a 3e&a 4e&a
02   X... X... X... X...
05   .... X... .... X...
```

**Pass 5 · `U35` · Part `R` · `OCTAVE -2` · Velocity `110`**

```text
U35 · R · OCT -2
Bars 1-8
Pad  1e&a 2e&a 3e&a 4e&a
05   .... X... .... X...

Bars 9-24
Pad  1e&a 2e&a 3e&a 4e&a
02   X... X... X... X...
05   .... X... .... X...

Bars 25-32
Pad  1e&a 2e&a 3e&a 4e&a
05   .... X... .... X...
```

**Pass 6 · `U36` · Part `R` · `OCTAVE -2` · Velocity `110`**

```text
U36 · R · OCT -2
Bars 1-8 and 25-32
Pad  1e&a 2e&a 3e&a 4e&a
05   .... X... .... X...

Bars 9-24
Pad  1e&a 2e&a 3e&a 4e&a
02   X... X... X... X...
05   .... X... .... X...
```

### Hats

**Pass 7 · `U31` · Part `R` · `OCTAVE -2` · Velocity `80`**

```text
U31 · R · OCT -2
Bars 9-32
Pad  1e&a 2e&a 3e&a 4e&a
12   .... ..X. .... ..X.
```

**Pass 8 · `U32` · Part `R` · `OCTAVE -2` · Velocity `80`**

```text
U32 · R · OCT -2
Bars 1-24
Pad  1e&a 2e&a 3e&a 4e&a
12   ..X. ..X. ..X. ..X.
```

**Pass 9 · `U33` · Part `R` · `OCTAVE -2` · Velocity `80`**

```text
U33 · R · OCT -2
Bars 1-24
Pad  1e&a 2e&a 3e&a 4e&a
12   ..X. ..X. ..X. ..X.
```

**Pass 10 · `U34` · Part `R` · `OCTAVE -2` · Velocity `80`**

```text
U34 · R · OCT -2
Bars 1-32
Pad  1e&a 2e&a 3e&a 4e&a
12   ..X. ..X. ..X. ..X.
```

**Pass 11 · `U35` · Part `R` · `OCTAVE -2` · Velocity `80`**

```text
U35 · R · OCT -2
Bars 9-24
Pad  1e&a 2e&a 3e&a 4e&a
12   ..X. ..X. ..X. ..X.
```

**Pass 12 · `U36` · Part `R` · `OCTAVE -2` · Velocity `80`**

```text
U36 · R · OCT -2
Bars 9-24
Pad  1e&a 2e&a 3e&a 4e&a
12   ..X. ..X. ..X. ..X.
```

**Pass 13 · `U36` · Part `R` · `OCTAVE -2` · Velocity `60`**

```text
U36 · R · OCT -2
Bars 1-8
Pad  1e&a 2e&a 3e&a 4e&a
12   .... ..X. .... ..X.
```

### Quieter Kick Sections

These add hits only in bars left empty by the main kick passes.

**Pass 14 · `U33` · Part `R` · `OCTAVE -2` · Velocity `80`**

```text
U33 · R · OCT -2
Bars 25-32
Pad  1e&a 2e&a 3e&a 4e&a
02   X... .... .... ....
```

**Pass 15 · `U35` · Part `R` · `OCTAVE -2` · Velocity `80`**

```text
U35 · R · OCT -2
Bars 25-32
Pad  1e&a 2e&a 3e&a 4e&a
02   X... .... .... ....
```

**Pass 16 · `U33` · Part `R` · `OCTAVE -2` · Velocity `45`**

```text
U33 · R · OCT -2
Bars 25-32
Pad  1e&a 2e&a 3e&a 4e&a
02   .... X... X... X...
```

**Pass 17 · `U35` · Part `R` · `OCTAVE -2` · Velocity `45`**

```text
U35 · R · OCT -2
Bars 25-32
Pad  1e&a 2e&a 3e&a 4e&a
02   .... X... X... X...
```

**Pass 18 · `U36` · Part `R` · `OCTAVE -2` · Velocity `90`**

```text
U36 · R · OCT -2
Bars 1-8
Pad  1e&a 2e&a 3e&a 4e&a
02   X... X... X... X...
```

**`U37` · Part R:** no drums in bars `1–10`; no pass to record.

## Phase 6: Record the Keys · Part 1

Use routine **A–H**. Press pads with aligned `X`s **together** as a chord. Release the first chord after about **three sixteenth steps**; tap later stabs short. These voicings are a playable approximation.

**Pass 19 · `U31` · Part `1` · `OCTAVE 0` · Velocity `90`**

```text
U31 · Part 1 · OCT 0
Bars 1-5: silent

Bar 6 only
Pad  1e&a 2e&a 3e&a 4e&a
13   .... .... .... X...

Bars 7-32
Pad  1e&a 2e&a 3e&a 4e&a
13   X... X... .... X...
```

**Pass 20 · `U32` · Part `1` · `OCTAVE 0` · Velocity `90`**

```text
U32 · Part 1 · OCT 0
Odd bars 1,3,...,31
Pad  1e&a 2e&a 3e&a 4e&a
02   X... ..X. .... ....
09   X... ..X. .... ....

Even bars 2,4,...,32
Pad  1e&a 2e&a 3e&a 4e&a
01   X... .... .... ....
06   X... .... .... ....
10   X..X .... X... X...
```

**Pass 21 · `U33` · Part `1` · `OCTAVE 0` · Velocity `90`**

```text
U33 · Part 1 · OCT 0
Odd bars 1,3,...,31
Pad  1e&a 2e&a 3e&a 4e&a
02   X... ..X. .... ....
09   X... ..X. .... ....

Even bars 2,4,...,32
Pad  1e&a 2e&a 3e&a 4e&a
01   X... .... .... ....
06   X... .... .... ....
10   X..X .... X... X...
```

**Pass 22 · `U34` · Part `1` · `OCTAVE 0` · Velocity `90`**

```text
U34 · Part 1 · OCT 0
Odd bars 1,3,...,31
Pad  1e&a 2e&a 3e&a 4e&a
02   X... ..X. .... ....
09   X... ..X. .... ....

Even bars 2,4,...,32
Pad  1e&a 2e&a 3e&a 4e&a
01   X... .... .... ....
06   X... .... .... ....
10   X..X .... X... X...
```

**Pass 23 · `U35` · Part `1` · `OCTAVE 0` · Velocity `90`**

```text
U35 · Part 1 · OCT 0
Odd bars 1,3,...,27
Pad  1e&a 2e&a 3e&a 4e&a
02   X... ..X. .... ....
09   X... ..X. .... ....

Even bars 2,4,...,28
Pad  1e&a 2e&a 3e&a 4e&a
01   X... .... .... ....
06   X... .... .... ....
10   X..X .... X... X...

Bars 29-32: silent
```

**Pass 24 · `U36` · Part `1` · `OCTAVE 0` · Velocity `90`**

```text
U36 · Part 1 · OCT 0
Bars 1-20: silent

Bars 21-32
Pad  1e&a 2e&a 3e&a 4e&a
13   X... X... .... X...
```

**`U37` · Part 1:** no keys in bars `1–10`; no pass to record.

24. **Lower the recorded keys by two semitones, once per pattern:**
    - Stopped in PATTERN mode, select **`U31`**.
    - Hold **`[SHIFT] + [FUNC]`**, press Pad **`[6]`**. This Transpose shortcut is *(unconfirmed)*. **If the command is not Transpose, press `[EXIT]`; do not execute a different edit.**
    - Select **only `PART [1]`**, turn **`[VALUE]`** to **`-2`**. Do not select a note range with the keyboard pads.
    - Press **`[ENTER]`** for the confirmation, then **`[ENTER]`** again.
    - Repeat for **`U32`, `U33`, `U34`, `U35` and `U36`**.
    - Tick off each pattern as you go. **Do not repeat this edit when listening again.**

The single pad-13 line now sounds **A4**. The odd-bar chord is **A#3 + F4**; the even-bar chord is **A3 + D4 + F#4**.

## Phase 7: Record the Voice · Part 2

Use routine **A–H**, with **Quantize completely OFF**. Tap short syllables, releasing after roughly one or two sixteenth steps. **No transpose on Part 2.**

**Pass 25 · `U31` · Part `2` · `OCTAVE 0` · Velocity `90`**

```text
U31 · Part 2 · OCT 0
Bar 1 only
Pad  1e&a 2e&a 3e&a 4e&a
11   .... X... .... X...
12   .... .... X... ....

Bars 2-24
Pad  1e&a 2e&a 3e&a 4e&a
11   X... X... .... X...
12   .... .... X... ....

Bars 25-32
Pad  1e&a 2e&a 3e&a 4e&a
13   X... .... .... X...
12   .... .... X... ....
```

**Pass 26 · `U32` · Part `2` · `OCTAVE 0` · Velocity `90`**

```text
U32 · Part 2 · OCT 0
Bars 1-24
Pad  1e&a 2e&a 3e&a 4e&a
13   X... .... .... X...
12   .... .... X... ....
```

**Pass 27 · `U33` · Part `2` · `OCTAVE 0` · Velocity `90`**

```text
U33 · Part 2 · OCT 0
Bars 1-32
Pad  1e&a 2e&a 3e&a 4e&a
13   X... .... .... X...
12   .... .... X... ....
```

**Pass 28 · `U34` · Part `2` · `OCTAVE 0` · Velocity `90`**

```text
U34 · Part 2 · OCT 0
Bars 1-8 and 17-32
Pad  1e&a 2e&a 3e&a 4e&a
13   X... .... .... X...
12   .... .... X... ....

Bars 9-16: silent
```

**Pass 29 · `U35` · Part `2` · `OCTAVE 0` · Velocity `90`**

```text
U35 · Part 2 · OCT 0
Bars 9-24
Pad  1e&a 2e&a 3e&a 4e&a
13   X... .... .... X...
12   .... .... X... ....
```

**Pass 30 · `U36` · Part `2` · `OCTAVE 0` · Velocity `90`**

```text
U36 · Part 2 · OCT 0
Bars 19-24
Pad  1e&a 2e&a 3e&a 4e&a
11   X... X... .... X...
12   .... .... X... ....
```

**Pass 31 · `U37` · Part `2` · `OCTAVE 0` · Velocity `90`**

```text
U37 · Part 2 · OCT 0
LGH 10
Bars 1-8
Pad  1e&a 2e&a 3e&a 4e&a
11   X... X... .... X...
12   .... .... X... ....

Bars 9-10: silent
```

Stop in the blank Loop Rest bar after **bar 10**.

**Pass 32 · `U32` · Part `2` · `OCTAVE 0` · Velocity `105`**

```text
U32 · Part 2 · OCT 0
Bars 25-32
Pad  1e&a 2e&a 3e&a 4e&a
11   X... X... .... X...
12   .... .... X... ....
```

**Pass 33 · `U35` · Part `2` · `OCTAVE 0` · Velocity `105`**

```text
U35 · Part 2 · OCT 0
Bars 1-8
Pad  1e&a 2e&a 3e&a 4e&a
11   X... X... .... X...
12   .... .... X... ....
```

**Pass 34 · `U36` · Part `2` · `OCTAVE 0` · Velocity `105`**

```text
U36 · Part 2 · OCT 0
Bars 25-32
Pad  1e&a 2e&a 3e&a 4e&a
11   X... X... .... X...
12   .... .... X... ....
```

## Phase 8: Enter the Bass · Part 3

**Use Step Recording here, not the realtime routine.** You enter one bar at a time without racing the metronome. Ties hold the long bass notes.

For manual entry, enter **one complete 32-bar run per pattern**. Alternatively, use **Copy Instead of Re-Tapping** below: record four two-bar cells, then copy them to fill all six cards. Step Recording overwrites Part 3 from its start point forward; never restart from bar 1 over bass you want to keep. Other Parts are untouched.

**Bass grids:** `X` = enter the pad; `~` = extend it with **TIE**, not another pad press. A column containing only dots is a **REST**. Follow the button recipes below to enter the grid; do not enter each pad row as a separate pass. The grids show the **record pads before the `-5` transpose**.

25. Stopped in PATTERN mode, select the bass card's pattern. Press **`[PART SELECT]`**, then **`PART [3]`**. Turn Quantize off.
26. Set **`OCTAVE -2`**. Leave the arpeggiator, pad sets and live transpose off.
27. Press **`[REC]`** once. Check **`bEt 4-4`**, **`LGH 32`**. Press **`PART [3]`**.
28. Press **`[REC]` a second time**. STEP REC lights. Before starting input, return the position to **`1-1 / 00`** with `[VALUE]` counter-clockwise if necessary. Press **`[PLAY]`**.
29. Press **`[SCALE/MEASURE]`** until the **sixteenth-note** grid is selected.
30. Set step-entry velocity: **hold `PART [2]` and turn `[VALUE]` to `100`**, then release. These PART buttons now set note-entry properties, not the recording destination. **System Pad Velocity is not the velocity control for this mode.**
31. Set gate ratio: **hold `PART [4]` and turn `[VALUE]` to `100%`**, then release. This lets the ties make continuous held notes.
32. Follow the card below, entering one of these three bar recipes or a blank bar. Each recipe advances exactly **16 steps**:

**A-G bar · odd bars where the card says A-G**

- Press and release **Pad `2`**.
- Press **`[BWD/TIE]` five times**.
- Press **`[FWD/REST]` once**.
- Press and release **Pad `14`**.
- Press **`[BWD/TIE]` twice**.
- Press and release **Pad `14`** again.
- Press **`[BWD/TIE]` once**.
- Press and release **Pad `9`**.
- Press and release **Pad `11`**.
- Press **`[BWD/TIE]` twice**.

That gives pad `2` on step `1`, pad `14` on `8` and `11`, pad `9` on `13`, pad `11` on `14`.

**A-D bar · odd bars where the card says A-D**

- Press and release **Pad `2`**.
- Press **`[BWD/TIE]` five times**.
- Press **`[FWD/REST]` once**.
- Press and release **Pad `14`**.
- Press **`[BWD/TIE]` once**.
- Press **`[FWD/REST]` once**.
- Press and release **Pad `9`**.
- Press **`[BWD/TIE]` twice**.
- Press and release **Pad `11`**.
- Press **`[BWD/TIE]` twice**.

That gives pad `2` on step `1`, pad `14` on `8`, pad `9` on `11`, pad `11` on `14`.

**B bar · every even bar with bass**

- Press and release **Pad `6`**.
- Press **`[BWD/TIE]` five times**.
- Press **`[FWD/REST]` once**.
- Press and release **Pad `11`**.
- Press **`[BWD/TIE]` once**.
- Press **`[FWD/REST]` once**.
- Press and release **Pad `13`**.
- Press **`[BWD/TIE]` twice**.
- Press and release **Pad `11`**.
- Press **`[BWD/TIE]` twice**.

That gives pad `6` on step `1`, pad `11` on `8`, pad `13` on `11`, pad `11` on `14`.

**Blank bar**

- Press **`[FWD/REST]` sixteen times**, keeping the grid at sixteenths.
- Do not press a pad or TIE.

After each bar, check you reached the **next bar, beat 1, clock 00**. After entering bar 32, press **`[STOP]`**. Do not enter bar 33.

### The Six Bass Cards

#### Copy Instead of Re-Tapping

**Use this instead of manually entering the six complete cards.** Record **A-D + B** and **A-G + B** at velocity `100`, plus each pair at `110`: just **eight entered bars**. Copying preserves pitches, velocities and held-note durations; the two-bar pairs keep odd/even bars aligned.

**Start before step 33's `-5` transpose**, with Part 3 empty in `U31`–`U36`. The other Parts and the 32-bar lengths should already be in place. If replacing an existing bass take, use **Redo the bass** at the end of this sheet to erase only Part 3 first. Do not mix already-lowered source notes with these raised record pads.

> **Verification note:** Part Copy's prompts follow the Owner's Manual pp.61–62 and [record_cheat.md, Phase 12](./record_cheat.md#phase-12-paste-one-part-into-another-pattern-part-copy). Pad `2` is inferred *(unconfirmed)*. Copying into the same pattern is also *(unconfirmed)* on hardware: confirm that the current pattern is offered as the destination before executing. If either check fails, cancel with `[EXIT]` and use the manual-entry cards instead.

**The Part Copy routine · use for every copy below**

- Stopped in PATTERN mode, select the **source pattern**.
- Hold **`[SHIFT] + [FUNC]`**, press Pad **`[2]`**. Check it opens **Part Copy**; otherwise `[EXIT]`.
- Select **only `PART [3]`** as source. Turn `[VALUE]` to **`PHRASE`**, then `[ENTER]`. This keeps the destination's sound setup; do not use Pattern Copy.
- `CURRENT` blinks: set the **first source bar**, then `[ENTER]`.
- `NEXT` blinks: set the **number of bars**, not the last bar number, then `[ENTER]`.
- Set the **destination pattern**, select **only `PART [3]`** as destination, then `[ENTER]`.
- Set the **destination start bar**, then `[ENTER]`. Use the stated bar, not `END`.
- Check the destination and range before the final **`[ENTER]`** executes. `[EXIT]` cancels.
- Re-select the destination, listen, then `[STOP]`. Re-select the stated source before the next copy.

**Copies replace that range of Part 3; they do not merge it.** No undo is documented. All copies below stay within 32 bars and use `4-4`; Parts R, 1 and 2 are not copied.

**A. Build the velocity-100 master in `U32`**

- Use steps **25–31** with `U32`, `OCTAVE -2`, velocity `100` and gate `100%`.
- At **`1-1 / 00`**, enter one **A-D** bar and one **B** bar using the recipes above. At **`3-1 / 00`**, press `[STOP]`.
- Re-enter Step Recording with steps **25–31**, but in step 28 set the position to **`9-1 / 00` before `[PLAY]`**, not bar 1. Enter **A-G**, then **B**. At **`11-1 / 00`**, press `[STOP]`. Do not enter blank bars to reach bar 9.
- Now leave Step Recording. Use Part Copy for these **same-pattern copies in order**:
- `U32` source **1**, count **2** → `U32` start **3**.
- `U32` source **1**, count **4** → `U32` start **5**.
- `U32` source **9**, count **2** → `U32` start **11**.
- `U32` source **9**, count **4** → `U32` start **13**.
- `U32` source **1**, count **16** → `U32` start **17**.

`U32` now has A-D/B in `1–8` and `17–24`, and A-G/B in `9–16` and `25–32`, all at velocity `100`. **Do not transpose it yet:** it supplies the next copies.

**B. Fill `U31`, `U33` and `U34`**

- `U32` source **9**, count **8** → `U31` start **25**. Leave `U31` bars `1–24` empty.
- `U32` source **1**, count **24** → `U33` start **1**. Leave `U33` bars `25–32` empty.
- `U32` source **1**, count **32** → `U34` start **1**.

**C. Build `U35`, including its louder ending**

- In empty Part 3 of `U35`, use steps **25–31**, but set step 28's position to **`25-1 / 00` before `[PLAY]`** and step 30's velocity to **`110`**.
- Enter **A-G**, then **B**. At **`27-1 / 00`**, press `[STOP]`. Leave Step Recording before copying.
- `U35` source **25**, count **2** → `U35` start **27**.
- `U35` source **25**, count **4** → `U35` start **29**.
- `U32` source **9**, count **8** → `U35` start **9**.
- `U32` source **1**, count **8** → `U35` start **17**.

Leave `U35` bars `1–8` empty. Bars `9–24` are velocity `100`; `25–32` are `110`.

**D. Build `U36`, including its louder opening**

- In empty Part 3 of `U36`, use steps **25–31** at **`1-1 / 00`**, with step-entry velocity **`110`**.
- Enter **A-D**, then **B**. At **`3-1 / 00`**, press `[STOP]`. Leave Step Recording before copying.
- `U36` source **1**, count **2** → `U36` start **3**.
- `U36` source **1**, count **4** → `U36` start **5**.
- `U32` source **9**, count **4** → `U36` start **9**.

`U36` bars `1–8` are velocity `110`; `9–12` are `100`. Leave `13–32` empty. `U37` has no bass and needs no copy.

**Finish:** compare each pattern against its card below, including silent ranges. Then go straight to **step 33** and apply `-5` **once per pattern**. Do not also enter the six cards manually. Changing step-entry velocity after a copy does not alter pasted notes.

#### Manual Entry / Copy Check Cards

For each range: **odd bars use the named A recipe; even bars use B**. For example, bars `25–32`, A-G means `25 A-G`, `26 B`, `27 A-G`, `28 B`, continuing to `32 B`.

**Pass 35 · `U31` · Part `3` · `OCTAVE -2` · Step velocity `100`**

```text
U31 · Part 3 · OCT -2
Bars 1-24: REST

Odd 25,27,29,31: A-G
Pad  1e&a 2e&a 3e&a 4e&a
02   X~~~ ~~.. .... ....
14   .... ...X ~~X~ ....
09   .... .... .... X...
11   .... .... .... .X~~

Even 26,28,30,32: B
Pad  1e&a 2e&a 3e&a 4e&a
06   X~~~ ~~.. .... ....
11   .... ...X ~... .X~~
13   .... .... ..X~ ~...
```

**Pass 36 · `U32` · Part `3` · `OCTAVE -2` · Step velocity `100`**

```text
U32 · Part 3 · OCT -2
Odd 1-8,17-24: A-D
Pad  1e&a 2e&a 3e&a 4e&a
02   X~~~ ~~.. .... ....
14   .... ...X ~... ....
09   .... .... ..X~ ~...
11   .... .... .... .X~~

Odd 9-16,25-32: A-G
Pad  1e&a 2e&a 3e&a 4e&a
02   X~~~ ~~.. .... ....
14   .... ...X ~~X~ ....
09   .... .... .... X...
11   .... .... .... .X~~

Even 2,4,...,32: B
Pad  1e&a 2e&a 3e&a 4e&a
06   X~~~ ~~.. .... ....
11   .... ...X ~... .X~~
13   .... .... ..X~ ~...
```

**Pass 37 · `U33` · Part `3` · `OCTAVE -2` · Step velocity `100`**

```text
U33 · Part 3 · OCT -2
Odd 1-8,17-24: A-D
Pad  1e&a 2e&a 3e&a 4e&a
02   X~~~ ~~.. .... ....
14   .... ...X ~... ....
09   .... .... ..X~ ~...
11   .... .... .... .X~~

Odd 9,11,13,15: A-G
Pad  1e&a 2e&a 3e&a 4e&a
02   X~~~ ~~.. .... ....
14   .... ...X ~~X~ ....
09   .... .... .... X...
11   .... .... .... .X~~

Even 2,4,...,24: B
Pad  1e&a 2e&a 3e&a 4e&a
06   X~~~ ~~.. .... ....
11   .... ...X ~... .X~~
13   .... .... ..X~ ~...

Bars 25-32: REST
```

**Pass 38 · `U34` · Part `3` · `OCTAVE -2` · Step velocity `100`**

```text
U34 · Part 3 · OCT -2
Odd 1-8,17-24: A-D
Pad  1e&a 2e&a 3e&a 4e&a
02   X~~~ ~~.. .... ....
14   .... ...X ~... ....
09   .... .... ..X~ ~...
11   .... .... .... .X~~

Odd 9-16,25-32: A-G
Pad  1e&a 2e&a 3e&a 4e&a
02   X~~~ ~~.. .... ....
14   .... ...X ~~X~ ....
09   .... .... .... X...
11   .... .... .... .X~~

Even 2,4,...,32: B
Pad  1e&a 2e&a 3e&a 4e&a
06   X~~~ ~~.. .... ....
11   .... ...X ~... .X~~
13   .... .... ..X~ ~...
```

**Pass 39 · `U35` · Part `3` · `OCTAVE -2` · Step velocity `100`, then `110`**

- Bars **`1–8`**: blank bars.
- Bars **`9–16`**: **A-G / B**, velocity **`100`**.
- Bars **`17–24`**: **A-D / B**, velocity **`100`**.
- Before bar **25**, hold **`PART [2]`**, turn `[VALUE]` to **`110`**, then release.
- Bars **`25–32`**: **A-G / B**, velocity **`110`**.

```text
U35 · Part 3 · OCT -2
Bars 1-8: REST

Odd 9-16,25-32: A-G
Pad  1e&a 2e&a 3e&a 4e&a
02   X~~~ ~~.. .... ....
14   .... ...X ~~X~ ....
09   .... .... .... X...
11   .... .... .... .X~~

Odd 17,19,21,23: A-D
Pad  1e&a 2e&a 3e&a 4e&a
02   X~~~ ~~.. .... ....
14   .... ...X ~... ....
09   .... .... ..X~ ~...
11   .... .... .... .X~~

Even 10,12,...,32: B
Pad  1e&a 2e&a 3e&a 4e&a
06   X~~~ ~~.. .... ....
11   .... ...X ~... .X~~
13   .... .... ..X~ ~...
```

**Pass 40 · `U36` · Part `3` · `OCTAVE -2` · Step velocity `110`, then `100`**

- Before entering bar 1, hold **`PART [2]`**, turn `[VALUE]` to **`110`**, then release.
- Bars **`1–8`**: **A-D / B**, velocity **`110`**.
- Before bar **9**, hold **`PART [2]`**, turn `[VALUE]` to **`100`**, then release.
- Bars **`9–12`**: **A-G / B**, velocity **`100`**.
- Bars **`13–32`**: blank bars.

```text
U36 · Part 3 · OCT -2
Odd 1,3,5,7: A-D
Pad  1e&a 2e&a 3e&a 4e&a
02   X~~~ ~~.. .... ....
14   .... ...X ~... ....
09   .... .... ..X~ ~...
11   .... .... .... .X~~

Odd 9,11: A-G
Pad  1e&a 2e&a 3e&a 4e&a
02   X~~~ ~~.. .... ....
14   .... ...X ~~X~ ....
09   .... .... .... X...
11   .... .... .... .X~~

Even 2,4,...,12: B
Pad  1e&a 2e&a 3e&a 4e&a
06   X~~~ ~~.. .... ....
11   .... ...X ~... .X~~
13   .... .... ..X~ ~...

Bars 13-32: REST
```

**`U37` · Part 3:** no bass in bars `1–10`; no pass to record.

33. **Lower the bass by five semitones, once in each of `U31`–`U36`:**
    - Stopped, select the pattern.
    - Hold **`[SHIFT] + [FUNC]`**, press Pad **`[6]`**.
    - Check the command is **Transpose** *(shortcut unconfirmed)*; cancel with `[EXIT]` if not.
    - Select **only `PART [3]`**. Set **`[VALUE]` to `-5`**.
    - Press **`[ENTER]`**, then **`[ENTER]`** again.
    - Tick off the pattern. Never apply `-5` twice.

The recorded pads now give these final bass notes:

```text
Pad     2  6  9 11 13 14
Note   G1 B1 D2 E2 F#2 G2
```

## Phase 9: Lock Timing and Check the Patterns

34. Stopped, hold **`[SHIFT]`**, press Pad **`[2]`**, set Grid resolution to **`16`**, then `[EXIT]`. With `[FUNC]` dark, put **TIMING fully clockwise**.
35. Select **`U31`**, press **`[QUANTIZE]`** until GRID lights.
36. Hold **`[SHIFT] + [FUNC]`**, press Pad **`[11]`** (Edit Quantize).
37. Make **only Parts R, 1 and 3 selected**. **Part 2 must not be selected.**
38. Press **`[ENTER]`**, then **`[ENTER]`** again. This stores the straight-grid timing in those notes; Play Quantize switches off.
39. Repeat steps **35–38** for **`U32`–`U36`**, lighting GRID again each time. **Do not quantize `U37`**, which has only voice notes.
40. Check all Quantize LEDs are off. Listen to each pattern from the start, hands off the knobs:
    - **`U31`**: clap and voice first; keys from bar 6, kick/hats from 9, bass from 25.
    - **`U32`**: kick/hats stop after 24; bass, keys and voice continue.
    - **`U33`**: bass/hats stop after 24; quieter kick continues.
    - **`U34`**: voice silent in 9–16; other Parts continue.
    - **`U35`**: no kick, hats or bass in 1–8; keys stop after 28.
    - **`U36`**: bass stops after 12; voice returns in 19, keys in 21; kick/hats stop after 24.
    - **`U37`**: voice only in 1–8, then two empty bars. Hold **`[SCALE/MEASURE]`** to check total length **`10`**.

## Phase 10: Chain and Save Song S-3

41. Press **`[STOP]`**, then **`[PLAY MODE]`** until **SONG** is lit.
42. SELECT to **PTN/SONG**, turn **`[VALUE]`** to **`S-3`**. Check this is the empty/disposable Song reserved in Phase 1.
43. Press **`[REC]`**. If **`SnG / CLr`** appears, **`[ENTER]` clears the existing Song steps**; press it only if they are disposable. Otherwise `[EXIT]` cancels.
44. Press **`[PLAY]`**. `CURRENT` shows Song step **`1`**.
45. Enter the seven patterns in this exact order:
    - `[VALUE]` to **`U31`** → **`[ENTER]`**.
    - `[VALUE]` to **`U32`** → **`[ENTER]`**.
    - `[VALUE]` to **`U33`** → **`[ENTER]`**.
    - `[VALUE]` to **`U34`** → **`[ENTER]`**.
    - `[VALUE]` to **`U35`** → **`[ENTER]`**.
    - `[VALUE]` to **`U36`** → **`[ENTER]`**.
    - `[VALUE]` to **`U37`** → **`[ENTER]`**.
46. Press **`[STOP]`**. The Song now contains **`32 × 6 + 10 = 202` bars**.
47. SELECT to **TEMPO**, turn **`[VALUE]`** to **`123.6`**.
48. Save the Song tempo: hold **`[SHIFT] + [FUNC]`**, press Pad **`[15]`**, then **`[ENTER]`**.
49. Turn Song Loop off: hold **`[SHIFT]`**, press Pad **`[16]`**, press **`SELECT [>]` once** to the Song Loop page *(page position unconfirmed)*, set **`OFF`**, then **`[EXIT]`**. Confirm you are changing Song Loop, not another System setting.
50. Press **`[SHIFT] + [BWD]`** to return to Song step 1, then **`[PLAY]`**. Keep your hands off the knobs.

Pattern changes should occur at approximately:

```text
U31  0:00
U32  1:02
U33  2:04
U34  3:06
U35  4:09
U36  5:11
U37  6:13
End  6:32
```

51. When finished, press **`[STOP]`**. Restore your original Pad Velocity: **`[SHIFT] + Pad [16]` → SELECT `[>]` seven times → `[VALUE]` → `[EXIT]`**. Return **OCTAVE to `0`**.
52. Check free memory again: **`[SHIFT] + Pad [16]` → SELECT `[>]` eight times → `[EXIT]`**.
53. Back up if you have an external MIDI sequencer that records SysEx:
    - Connect **MC-303 MIDI OUT → sequencer MIDI IN**.
    - With playback stopped, hold **`[SHIFT] + [FUNC]`**, press Pad **`[16]`** (Bulk Dump).
    - Start recording on the external sequencer.
    - Press **`[ENTER]`** on the MC-303. At each transmission pause, press `[ENTER]` again for the next packet, until the completion display.
    - Stop and save the external recording. Restoring a dump replaces the MC-303's current User Patterns and Songs.

**Finished:** the notes and Song steps are stored as you record; Pattern Setup Write saved the sounds, and Song Setup Write saved `123.6` BPM. Do not delete `U31`–`U37`: `S-3` plays those patterns, not separate copies.

## If a Take Goes Wrong

**Do not simply replay a realtime pass: it adds duplicate notes.**

**Redo a whole keys or voice Part:**

- Stopped in PATTERN mode, select the affected pattern.
- Hold **`[SHIFT] + [FUNC]`**, press Pad **`[3]`** (Erase).
- Select **only Part 1 for keys or Part 2 for voice**.
- Set first bar **`1`** → `[ENTER]` → count **`ALL`** → `[ENTER]` → `[ENTER]`.
- This keeps the length and sound setup.
- Repeat **all cards for that Part in that pattern**.
- For re-recorded keys, apply **`-2` once** afterwards. The old lowered notes were erased.
- If you redo keys after Phase 9, run Edit Quantize again on **Part 1 only**.

**Redo one drum without clearing the rest:**

- Select the pattern, **`[PART SELECT]` → `PART [R]`**, **OCTAVE `-2`**.
- Press `[REC]`, check `LGH 32`, `Cnt 1`, `LoP on`, then `[PLAY]`.
- While recording, hold **`[SHIFT]`**, press **`[TRANSPOSE/ERASE]`**. Wait until **`ErS`** appears before touching a pad.
- Hold **only the unwanted drum's pad** (`2` kick, `5` clap or `12` hat) throughout the bars to clear. You can arm Erase in the blank Loop Rest bar, then hold the pad from bar 1 on the next loop.
- Release the pad, press **`[EXIT]`**, then `[STOP]` in the blank Loop Rest bar.
- Repeat that drum's cards for the cleared bars, **without re-tapping other drums**. If you cleared the whole kick, include its quieter passes too.
- If this is after Phase 9, run Edit Quantize again on **Part R only**.
- In Erase mode, **holding `[REC]` erases the entire Part**, not just one drum.

**Redo the bass:**

- Use Erase above with **only Part 3**, first bar `1`, count `ALL`.
- Repeat that pattern's **entire 32-bar bass card**, or rebuild it with **Copy Instead of Re-Tapping**, then apply **`-5` once**. The old lowered bass notes were erased. The copy route requires untransposed sources: if your only sources are already lowered, use manual entry rather than applying `-5` to copied lowered notes.
- A keys/bass playback check is not a reason to transpose again.
