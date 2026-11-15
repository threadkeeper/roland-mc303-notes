# Deep Inside (Hardrive, 2015 remix) · MC-303 Instructions

A pass-grid recipe to rebuild the **uploaded 2015 remix** (6:32, ~123.6 BPM) on the MC-303, in the format of [jonty_first_track.md](./jonty_first_track.md) and [record_cheat.md](./record_cheat.md). It points at their routines instead of repeating them: **pass routine = record_cheat.md step 47 (a–h)**, setup/quantize/song = Jonty §5.

> **Honest status.** Nothing was heard and nothing was run on a hardware MC-303. Every bar, step and pad below was **measured from stem separation** (SCNet 4-stem + DrumSep, basic-pitch notes), then simplified. Raw data: [`analysis/deep_inside/`](./analysis/deep_inside/). Bars are ±1. Items marked *(approx)* are my best guess where the separator was noisy (tom/ride/crash lanes were noise and are **not used**; closed hats, crashes and the intro are assumed).

---

## 1. Facts

- **123.6 BPM**, 4/4, **202 bars**, one bar = 1.94 s. Bar `b` starts at `0:02 + (b−1) × 1.94 s`.
- **Key: unresolved.** The bass sits on B / E / F# / D (**E minor**, or B minor). The synth bed sits on A / A# / D / F# (*(approx)*). Pads below follow the measurements, so trust your ear.
- Seven 32-bar patterns. `U31`–`U37` leave Jonty's `U41`–`U45` untouched (the MC-303 only has `U01`–`U50`; any 7 free slots work). Song = **`S-3`**: `U31 → … → U37`.
- Pad → note: `note = 58 + 12 × shift + pad`. Synth Parts at `OCTAVE 0` (pad 11 = A4); bass at `OCTAVE -2` (pad 1 = B1). The bass's G1 isn't reachable at `-2`, so B1 stands in *(approx)*.
- Drum kit `d07`: Kick `2` · Clap `5` · Crash `15` · Open hat `12` · Closed hat `8`, all at `OCTAVE -2` (record_cheat.md §6.2).

---

## 2. The Arrangement

```text
Pat   U31      U32      U33      U34      U35      U36      U37
Bar   1        33       65       97       129      161      193
Clock 0:02     1:04     2:06     3:08     4:10     5:12     6:15
```

Each column = 8 bars. `#` on, `+` partly/weak, `.` off.

```text
Bar    1   |33  |65  |97  |129 |161 |193
Pat    U31 |U32 |U33 |U34 |U35 |U36 |U37
Kick   .###|###.|###+|####|.##+|+##.|.
Clap   ####|####|####|####|####|####|.
O.hat  ####|###.|####|####|.###|###.|.
C.hat  ....|###.|####|####|.###|###.|.
Crash  .#..|....|#...|#...|.#..|.#..|.
Bed    +###|####|####|####|###.|..##|.
Vox    ....|...#|....|....|###.|..##|#
Bass   ...#|####|###.|####|.###|#+..|.
```

- **1–8** clap + hat only, bed enters at 6. **9** kick in. **25** bass in.
- **57–64** drop: no kick or hats, bass continues, clap on 5 and 13, vocal stand-in loud.
- **89–96** bass out, kick weak. **129–136** breakdown: no kick, no bass, vocal.
- **153–168** kick weak, bed gone. **169–172** last bass. **177–192** bed stabs + vocal.
- **185–192** kick out. **193–200** vocal only. Silence from ~6:29.

---

## 3. Cheat Card

Steps 1–16 in a bar. `X` = hit.

```text
Step    1   5   9   13
        |   |   |   |
Kick    X...X...X...X...
Clap    ....X.......X...
O.hat   ..X...X...X...X.
C.hat   .X.X.X.X.X.X.X.X   (approx)
Crash   X...............   (approx)
```

**Bass bar** (`OCTAVE -2`, one bar repeated): keys `1 · 1 · 6 · 8 · 8 · 4 · 6 · 1` · steps `1 7 8 10 11 13 14 16`
= B1 B1 E2 F#2 F#2 D2 E2 B1.

**Bed bar** (Part 1, `OCTAVE 0`): keys `11 · 11 · 12 · 11 · 9 · 12 · 11` · steps `1 4 7 8 9 11 13`
= A4 A4 A#4 A4 G4 A#4 A4. Early bars `6–24` and the late stabs: pad `11` · steps `1 5 13` only.

**Vocal stand-in** (Part 2, `OCTAVE 0`): keys `11 · 11 · 12 · 11 · 13` · steps `1 5 9 13 14` = A4 A4 A#4 A4 B4.

---

## 4. Setup

1. **Do Jonty §5 steps 1–10** (copy a template, set Tones, write setup), with these changes:
   - Patterns `U31`–`U37`, `LGH` `32` (`U37`: `10`, *unconfirmed*; fallback: keep `32` and press `[STOP]` after bar 10 of `U37`).
   - Tempo **`123.6`** (not 124.0).
   - Tones: Part 1 `t10-02` (bed), Part 2 `t07-08` (vocal stand-in), Part 3 `t02-11` (bass).
2. If `[SHIFT]`, `OCTAVE [+]` or `SELECT [<]` are faulty, use Jonty §1.4 and [repair.md](./repair.md). The passes below go **synths, then drums**, with `OCTAVE` only ever going down (`0` → `-2`).

---

## 5. Synth Passes

Pass routine: record_cheat.md step 47, with `PART [1]`/`[2]`/`[3]` instead of `PART [R]` (Jonty step 13). Pad Velocity **`100`**.

### Bed · Part `1` · `OCTAVE 0`
Keys `11 · 11 · 12 · 11 · 9 · 12 · 11` · steps `1 4 7 8 9 11 13`
- **1 · `U31`** · bars `25–32`
- **2 · `U32`** · bars `1–32`
- **3 · `U33`** · bars `1–32`
- **4 · `U34`** · bars `1–32`
- **5 · `U35`** · bars `1–24`

Early bars: pad `11` · steps `1 5 13`
- **6 · `U31`** · bars `6–24`

Late stabs: pad `11` · steps `1 5 13`
- **7 · `U36`** · bars `17–32`

### Vocal stand-in · Part `2` · `OCTAVE 0`
Keys `11 · 11 · 12 · 11 · 13` · steps `1 5 9 13 14` *(leave Part 2 unquantized)*
- **8 · `U32`** · bars `25–32`
- **9 · `U35`** · bars `1–24`
- **10 · `U36`** · bars `17–32`
- **11 · `U37`** · bars `1–8`

### Bass · Part `3` · `OCTAVE -2`
Keys `1 · 1 · 6 · 8 · 8 · 4 · 6 · 1` · steps `1 7 8 10 11 13 14 16`
- **12 · `U31`** · bars `25–32`
- **13 · `U32`** · bars `1–32`
- **14 · `U33`** · bars `1–24`
- **15 · `U34`** · bars `1–32`
- **16 · `U35`** · bars `9–32`
- **17 · `U36`** · bars `1–12`

Tips: one key per hit, change pad **inside** the bar; tap short; every pass starts on bar 1 of its range, so start the cell on its first key.

---

## 6. Drum Passes

`OCTAVE -2` for all drums. Pass routine: record_cheat.md step 47. Set Pad Velocity **`80`** for the soft group, **`110`** for the loud group (Jonty step 17 / before pass 33).

### Hats · Velocity `80`
**Open hat** pad `12` · steps `3 7 11 15`
- **18 · `U31`** · bars `1–32`
- **19 · `U32`** · bars `1–24`
- **20 · `U33`** · bars `1–32`
- **21 · `U34`** · bars `1–32`
- **22 · `U35`** · bars `9–32`
- **23 · `U36`** · bars `1–24`

**Closed hat** pad `8` · steps `2 4 6 8 10 12 14 16` *(approx)*
- **24 · `U32`** · bars `1–24`
- **25 · `U33`** · bars `1–32`
- **26 · `U34`** · bars `1–32`
- **27 · `U35`** · bars `9–32`
- **28 · `U36`** · bars `1–24`

### Weak kick · Velocity `80`
**Kick** pad `2` · steps `1 9`
- **29 · `U33`** · bars `25–32`
- **30 · `U35`** · bars `25–32`
- **31 · `U36`** · bars `1–8`

### Kick, clap & crash · Velocity `110`
**Kick** pad `2` · steps `1 5 9 13`
- **32 · `U31`** · bars `9–32`
- **33 · `U32`** · bars `1–24`
- **34 · `U33`** · bars `1–24`
- **35 · `U34`** · bars `1–32`
- **36 · `U35`** · bars `9–24`
- **37 · `U36`** · bars `9–24`

**Clap** pad `5` · steps `5 13`
- **38–43 · `U31`–`U36`** · bars `1–32` each *(one pass per pattern)*

**Crash** pad `15` · step `1` *(approx)*
- **44 · `U31`** · bar `9`
- **45 · `U33`** · bar `1`
- **46 · `U34`** · bar `1`
- **47 · `U35`** · bar `9`
- **48 · `U36`** · bar `9`

Tips: watch `NEXT`; the drop bars (`U32` 25–32, `U35` 1–8, `U36` 25–32) simply have **no kick or hats** (the clap stays). Fast hats too hard? Slow the tempo for the pass (record_cheat.md pass tips).

---

## 7. Finish

1. **Quantize (Jonty step 22)** per pattern `U31`–`U37`: Parts `R`, `1`, `3` only. Part 2 stays loose.
2. **Chain `S-3` = `U31 … U37`** (Jonty steps 23–26) and write setup at `123.6` (step 27).
3. **Hear it:** `[SHIFT] + [BWD]` then `[PLAY]`. Expect about **6:32**. Backup and clean-up: Jonty steps 28–29, record_cheat.md step 53.

## 8. Quick Fixes

- **Bass sounds off the key.** The bass key is unresolved. Try shifting the whole bass pass with Transpose (next_steps.md steps 17–18) or swap pad `1` for `13` (B2) / `6` for `8`.
- **Bed clashes with the bass.** The separator put the bed on A/D, the bass on B/E. Drop the bed's `9` and `12` pads and keep only pad `11`.
- **Too busy.** Skip the closed hats (passes 24–28) and the vocal stand-in.
- **Intro or crash placement wrong.** Change one bar range in the pass, which is all that depends on it.
