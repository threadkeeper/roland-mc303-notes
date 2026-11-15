# Jonty's First Track — a "Deep Inside"-Style Build on the Roland MC-303 (124 BPM · 5 × 32 Bars · `U41`–`U45`)

A complete plan and pass grid for a ~5-minute deep-house track: your hook (keys `1 · 11 · 16 · 11`, timing `1 5 9 11 13`) with a free-style layer and a deep bass, laid down **synths first, then drums**, over five 32-bar patterns arranged after Hardrive's *Deep Inside*. It builds on [record_cheat.md](./record_cheat.md): Sections 4–6 hold the recording routines this sheet points to, and Section 7 covers copying, pasting and wiping individual Parts. Written to be read on a phone.

> **Verification note:** Nothing here has been run on a physical MC-303. Key sequences come from [record_cheat.md](./record_cheat.md), which is cross-checked against the 1996 Owner's Manual. The facts about the record (versions, lengths, tempo, key) come from Discogs and key/BPM databases (§2). **I couldn't find a trustworthy bar-by-bar breakdown of the record**, so the entry bars in §3 are a model of the usual shape of an early-'90s New York house 12-inch, not a transcription. Anything marked *(unconfirmed)* is a best guess.

---

## 1. Read This First

### 1.1 Pattern Numbers

The MC-303 has **50** User Patterns, `U01`–`U50` (manual p.13; Sweetwater says the same), so there is no pattern 90–99. Your "90 onwards" is mapped to the top of the bank: **slot = your number − 49**.

| Your number | 90 | 91 | 92 | 93 | 94 | 95–99 |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: |
| MC-303 pattern | `U41` | `U42` | `U43` | `U44` | `U45` | `U46`–`U50` (spare) |

That keeps the build clear of `U01`/`U02` and Song `S-1` (Sections 5–6). **Every slot you use must be empty or disposable**: Pattern Copy overwrites without asking.

### 1.2 What Is Assumed

| Item | Setting | Notes |
| :--- | :--- | :--- |
| Tempo | **`124.0`** BPM | 1 bar = 1.935 s, so five 32-bar patterns = 160 bars = **5:10** |
| Key | B minor | Your pads at `OCTAVE 0`: `1` = B3, `11` = A4, `16` = D5 (pad 2 = C4, so note = 58 + pad) |
| The hook | Keys `1 · 11 · 16 · 11` = **one pad per bar** (a 4-bar cell that repeats). Timing `1 5 9 11 13` = the **five hits in every bar** | Count it **1 · 2 · 3 & · 4**. *If you actually play one pad per hit, change only the Hook and Bass rows in §5.* |
| Parts | `R` drums · `1` hook · `2` free-style · `3` bass | Tones in §1.3 |
| Song | **`S-2`**, so `S-1` stays as it is | |

### 1.3 Parts & Tones

| Part | Job | Tone *(suggestions, any will do)* |
| :-: | :--- | :--- |
| `R` | Drums | `d07` House (already on `U02` from Section 6) |
| `1` | **Hook**: your tune | Keep `t01-15` (Tri Lead 1), or `t10-02` (bright piano) for a closer *Deep Inside* feel |
| `2` | **Free-style**: stands in for the "deep inside" vocal | `t07-08` (auh auh), or `t10-09` (clav.) for a funkier line |
| `3` | **Bass**: the hook's pads two octaves down | `t02-11` (house bass) |

Tone names are from [sample_bank.md](./sample_bank.md).

### 1.4 While Your Buttons Are Still Faulty

If `[SHIFT]`, `OCTAVE [+]` and `SELECT [<]` are still faulty ([repair.md](./repair.md)):

- **Every copy, wipe and Edit Quantize starts with `[SHIFT] + [FUNC]`.** Put SHIFT on a pedal first (repair.md §3.4).
- **`OCTAVE` can only go down.** Both grids are ordered so it never rises *within* a phase. It has to climb from `-2` back to `0` **once**, between Phase B and Phase C (step 16). If `[+]` is still dead then, power-cycle first (whether that resets the octave is *unconfirmed*, repair.md §3.5) and re-check the quantize aim and Pad Velocity afterwards.
- **`TEMPO` is left of `PTN/SONG`, so `SELECT [>]` can't reach it.** Use tap tempo (repair.md §3.1). A beat or two either side of 124 breaks nothing (each BPM moves the end of the track by about 2.5 s).

---

## 2. How This Lines Up with *Deep Inside*

### 2.1 What Is Verified

| Fact | Value | Source |
| :--- | :--- | :--- |
| Release | Hardrive (Louie Vega), *Deep Inside* EP, Strictly Rhythm **SR EP2**, 30 June 1993 | Discogs |
| Versions | **A1** *Deep Inside* **6:28** · **B3** *Deep Inside (The Dub)* **5:14** | Discogs |
| Tempo | **124 BPM** for both (entered by Discogs contributors; the record doesn't print a BPM) | Discogs notes, diggerdigger |
| Key | **B minor** (10A), a machine estimate, so check it by ear | diggerdigger (ReccoBeats) |
| Vocal | Barbara Tucker's *Beautiful People*: the track is "substantially based off of samples" from it | Insomniac |

### 2.2 What I Couldn't Verify

**Where each element enters and leaves.** Nothing I could reach publishes a bar-by-bar breakdown, and the breakdowns I found contradict each other (one puts the first vocal at 0:02, another at about 2:53), so I haven't used any of their timestamps. The descriptions of the track agree on its **sound**: a deep bassline, a recurring piano riff, layered percussion (claps, hats) and the sampled "deep inside" vocal hook. *(Those are descriptions, not primary sources.)*

### 2.3 How the Build Maps onto It

| In the record | In this build |
| :--- | :--- |
| 124 BPM, B minor | `124.0` BPM, and your pads sit in B minor |
| The Dub's 5:14 | 5 × 32 bars = 160 bars = **5:10** (the Original's 6:28 is about 200 bars: see §7) |
| Drum-led DJ intro | `U41`: kick from bar 1, a new layer every 8 bars |
| Deep bassline | Part 3: the hook's pads two octaves down, on the off-beats |
| Piano riff | Part 1: your hook (use `t10-02` if you want the piano sound) |
| "Deep inside" vocal hook | Part 2 free-style on a voice Tone: a stand-in, because the MC-303 can't play the sample |
| Break, peak, DJ outro | `U43` break, `U44` peak, `U45` groove into a stripped outro |

**To pin it to the record:** play the record next to the grid, note the clock where each element enters, convert it with the clock table in §3 (one 8-bar phrase = 15.5 s) and change the bar range in that element's rows in §5. Each change is one range in one row.

---

## 3. The Arrangement (Song `S-2`: `U41 → U42 → U43 → U44 → U45`)

| Song bars | Pattern (your no.) | Clock | Section | What enters (bar in the pattern) and what leaves |
| :--- | :-: | :-: | :--- | :--- |
| 1–32 | `U41` (90) | 0:00 | **Intro**: drum-led | Kick `1` · closed hat `9` · clap + open hat `17` · tambourine + hook teaser `25` |
| 33–64 | `U42` (91) | 1:02 | **Groove 1**: the bass drops | Crash, bass + hook `1` · congas `9` · ride `17` · free-style `25` |
| 65–96 | `U43` (92) | 2:04 | **Break**: hook + free-style lead | Drops to congas, hook + free-style · tambourine `9` · bass + closed hat `17` · kick, clap + open hat `25` |
| 97–128 | `U44` (93) | 3:06 | **Peak** | Crash `1` · everything · the kick gets the step-`11` hit · free-style `9–16` and `25–32` |
| 129–160 | `U45` (94) | 4:08 | **Groove 2, then outro** | Crash `1` · free-style `1–8` · hook, bass, congas, tambourine + ride out at `17` · clap + open hat out at `25` · last 8 bars: kick + closed hat |

| Clock at bar… | 1 | 9 | 17 | 25 |
| :--- | :-: | :-: | :-: | :-: |
| `U41` | 0:00 | 0:15 | 0:31 | 0:46 |
| `U42` | 1:02 | 1:17 | 1:33 | 1:48 |
| `U43` | 2:04 | 2:19 | 2:35 | 2:50 |
| `U44` | 3:06 | 3:21 | 3:37 | 3:52 |
| `U45` | 4:08 | 4:23 | 4:39 | 4:54 |

The track ends at **5:10**.

```text
Song bar   1       |33      |65      |97      |129
Pattern    U41     |U42     |U43     |U44     |U45
Kick       ########|########|......##|########|########
Clap       ....####|########|......##|########|######..
Closed hat ..######|########|....####|########|########
Open hat   ....####|########|......##|########|######..
Tambourine ......##|########|..######|########|####....
Congas     ........|..######|########|########|####....
Ride       ........|....####|........|########|####....
Crash      ........|*.......|........|*.......|*.......
Bass       ........|########|....####|########|####....
Hook       ......##|########|########|########|####....
Free-style ........|......##|########|..##..##|##......
```

`#` plays · `.` silent · `*` one bar (the crash) · one column = 4 bars.

---

## 4. Cheat Card: The Groove on One Page

**The hook and bass cell** (one pad per bar; the cell restarts every 4 bars, so every pass starts on pad `1`):

```text
Bar        1               2               3               4               then repeat
Pad        1  (B3)         11 (A4)         16 (D5)         11 (A4)
Hits       1 5 9 11 13     1 5 9 11 13     1 5 9 11 13     1 5 9 11 13
Count      1 2 3 & 4       1 2 3 & 4       1 2 3 & 4       1 2 3 & 4
```

**One bar, step by step** (`X` = tap):

```text
Step       1 e & a 2 e & a 3 e & a 4 e & a
Hook       X . . . X . . . X . X . X . . .
Bass       . . X . . . X . . . X . . . X .
Kick       X . . . X . . . X . . . X . . .
Kick (U44) X . . . X . . . X . X . X . . .
Clap       . . . . X . . . . . . . X . . .
Closed hat . X . X . X . X . X . X . X . X
Open hat   . . X . . . X . . . X . . . X .
Tambourine . . . . X . . . . . . . X . . .
Ride       . . X . . . X . . . X . . . X .
Lo conga   . . . X . . . . . . X . . . . .
Hi conga   . . . . . . . X . . . . . X . .
```

The hook and the kick land together on the beats, and the hook, bass, open hat and (in `U44`) kick all hit step `11`: the "and" of beat 3 is the funk push.

**Synth pads** (`note = 58 + 12 × shift + pad`, manual p.20):

| Part | `OCTAVE` | Pads | Notes |
| :--- | :-: | :--- | :--- |
| `1` Hook | `0` | `1 · 11 · 16 · 11` | B3 · A4 · D5 · A4 |
| `2` Free-style | `0` | `1 4 6 8 11 13 16` | B3 D4 E4 F#4 A4 B4 D5 (B minor pentatonic) |
| `3` Bass | `-2` | `1 · 11 · 16 · 11` | B1 · A2 · D3 · A2 |

**Drum pads, octaves and notes** are the cheat card in [record_cheat.md §6.2](./record_cheat.md) (Rhythm Set `d07`). The shaker isn't used here, because it needs `OCTAVE +1`.

---

## 5. Build It

### Phase A: Make the Five Patterns (Copy, Wipe, Set Up, Fan Out)
> Only **copies** are wiped here. `U01`, `U02` and `S-1` are only ever read. The key sequences are in record_cheat.md, Section 7 (Phases 10–11, steps 56–65).

1. Press **`[STOP]`**, then **`[PLAY MODE]`** until **`PATTERN`** is lit, and make sure **`[PTN SET]`**, **`[RPS SET]`** and **`[FUNC]`** are dark.
2. **Check the five slots are free:** `SELECT` → `PTN/SONG`, then turn **`[VALUE]`** to **`u41`**, `u42` … `u45`. Each must show a lowercase `u`. An uppercase `U` means it holds data: pick another spare slot (`U46`–`U50`), or clear it first (record_cheat.md, Section 4E, *Delete Entire User Pattern*).
3. **Note your free memory:** hold **`[SHIFT]`** and press Pad **`[16]`** → `SELECT [>]` ×8 → write the % down → **`[EXIT]`** (record_cheat.md step 46).
4. **Copy `U02` → `U41`** with Pattern Copy, **`ALL`** (record_cheat.md, Phase 10, steps 56–60). It brings `d07` on Part R, `t01-15` with its LFO set-up on Part 1, and `U02`'s starting sound. *(No `U02`? Copy any pattern that has `d07` on Part R, or set `U41` up from scratch with Section 5, Phase 1 and Section 6, Phase 6.)*
5. **Wipe Part 1 and Part R in the copy:** select **`U41`** and read `CURRENT`, then Erase with **`PART [1]` and `PART [R]` both lit**, first bar `1`, count `ALL` (record_cheat.md, Phase 11, steps 61–64). Check with **`[PART MUTE]`**: no PART button should be lit (step 65), then press **`[PART SELECT]`**. `U41` now has `U02`'s set-up and no notes.
6. **Set the tempo to `124.0`:** `SELECT` → `TEMPO`, hold **`[SHIFT]`** and turn **`[VALUE]`** (Section 5, step 8; use tap tempo if `SELECT [<]` is dead).
7. **Give Parts 2 and 3 their Tones:** press **`[PART SELECT]`** (lit) → **`PART [2]`** → `SELECT [>]` until `TONE` is lit → turn **`[VALUE]`** to **`t07-08`** (hold `[SHIFT]` to jump). Then **`PART [3]`** → **`t02-11`**. *(Optional: `PART [1]` → `t10-02`.)* Audition at the current octave, `0` (Part 3 sounds two octaves higher now than it will once you record it at `-2`). **Leave `OCTAVE` at `0`.**
8. **Pattern Setup Write** (hands off the knobs, and don't switch patterns first): hold **`[SHIFT] + [FUNC]`** and press Pad **`[15]`** (`SUrE`) → **`[ENTER]`**. This stores the Tones and `124.0` in `U41`. *(Never run it right after a knob pass: see the warning at the top of record_cheat.md, Phase 6.)*
9. **Fan the set-up out to `U42`–`U45`:** select **`U41`**, then run Pattern Copy with data type **`SETUP`** to **`U42`** (record_cheat.md, Phase 10, steps 58–59). Repeat for **`U43`**, **`U44`** and **`U45`**, re-selecting **`U41`** as the source each time and reading `CURRENT`. Each copy carries the Tones, the `d07` kit, the knob start positions, the mutes and the `124.0` tempo, and **no notes**.
10. **Spot-check `U45`:** `TEMPO` reads `124.0`, Part R shows `d07` and Part 3 shows `t02-11`. *(All five patterns stay empty until Phase B. Don't put an empty pattern into a Song.)*

---

### Phase B: Synths First (Passes 1–13)
> **How it works:** this is the pass method of record_cheat.md, Phase 8, with synths. Each pass records into **one pattern, one Part, one `OCTAVE` and one Pad Velocity**. Loop Mix adds each pass to what is already on the Part, and `LoP = on` gives you a blank 33rd bar to press `[STOP]` in. The hook goes in first, then the free-style over it, then the bass.

11. **Aim Play Quantize at Parts R, 1 and 3 only** (record_cheat.md steps 42–44): hold **`[SHIFT]`** and press **`[PART SELECT / QUANTIZE SELECT]`**, light **`PART [R]`, `[1]` and `[3]`** and no others, then press **`[PART SELECT]`**. Resolution `16`, and **`TIMING`** fully clockwise. **`PART [2]` stays dark**, so the free-style keeps your own timing. Then press **`[QUANTIZE]`** until **GRID** is lit.
12. **Note your Pad Velocity** (step 45) **and set it to `100`:** hold **`[SHIFT]`** and press Pad **`[16]`** → `SELECT [>]` ×7 (`PuL`) → **`[VALUE]`** → **`[EXIT]`**. All 13 synth passes use `100`.
13. **The pass routine** is record_cheat.md step 47 (a–h) with two changes: in (b) and (e.3) press the **row's Part** (`PART [1]`, `[2]` or `[3]`) instead of `PART [R]`, and in (c) the octave is the row's. Standby: `bEt` `4-4`, `LGH` `32`, `Cnt` `1`, `LoP` `on`. After the 4 clicks, watch `NEXT` and start tapping at the row's first bar.
14. **The 13 synth passes** *(top to bottom; change `OCTAVE` only where it differs from the row above)*:

| # | Pattern | Part | `OCTAVE` | Velocity | Tap this (pad · steps · bars) |
| :-: | :-: | :-: | :-: | :-: | :--- |
| 1 | `U41` | `1` | `0` | `100` | **Hook** · pads `1 · 11 · 16 · 11` (one per bar) · steps `1 5 9 11 13` · bars `25–32` |
| 2 | `U42` | `1` | `0` | `100` | **Hook** · pads `1 · 11 · 16 · 11` · steps `1 5 9 11 13` · bars `1–32` |
| 3 | `U43` | `1` | `0` | `100` | **Hook** · pads `1 · 11 · 16 · 11` · steps `1 5 9 11 13` · bars `1–32` |
| 4 | `U44` | `1` | `0` | `100` | **Hook** · pads `1 · 11 · 16 · 11` · steps `1 5 9 11 13` · bars `1–32` |
| 5 | `U45` | `1` | `0` | `100` | **Hook** · pads `1 · 11 · 16 · 11` · steps `1 5 9 11 13` · bars `1–16` |
| 6 | `U42` | `2` | `0` | `100` | **Free-style** · pads `1 4 6 8 11 13 16` · land on steps `3 7 15` · bars `25–32` |
| 7 | `U43` | `2` | `0` | `100` | **Free-style** · pads `1 4 6 8 11 13 16` · land on steps `3 7 15` · bars `1–32` *(the break: leave plenty of space)* |
| 8 | `U44` | `2` | `0` | `100` | **Free-style** · pads `1 4 6 8 11 13 16` · land on steps `3 7 15` · bars `9–16` and `25–32` |
| 9 | `U45` | `2` | `0` | `100` | **Free-style** · pads `1 4 6 8 11 13 16` · land on steps `3 7 15` · bars `1–8` |
| 10 | `U42` | `3` | `-2` | `100` | **Bass** · pads `1 · 11 · 16 · 11` (one per bar) · steps `3 7 11 15` · bars `1–32` |
| 11 | `U43` | `3` | `-2` | `100` | **Bass** · pads `1 · 11 · 16 · 11` · steps `3 7 11 15` · bars `17–32` |
| 12 | `U44` | `3` | `-2` | `100` | **Bass** · pads `1 · 11 · 16 · 11` · steps `3 7 11 15` · bars `1–32` |
| 13 | `U45` | `3` | `-2` | `100` | **Bass** · pads `1 · 11 · 16 · 11` · steps `3 7 11 15` · bars `1–16` |

15. **Pass tips**
    - **Count the hook 1 · 2 · 3 & · 4.** The five hits are beat 1, beat 2, beat 3, the "and" of 3, and beat 4. Change pad on each bar line: bar 1 pad `1`, bar 2 pad `11`, bar 3 pad `16`, bar 4 pad `11`, then round again. Every row starts on a bar that is a multiple of 4 plus 1, so it always starts on pad `1`.
    - **Tap short and crisp:** the length you hold a pad is the length that is recorded.
    - **Free-style:** the hook lands on `1 5 9 11 13`, so play in the gaps: land on steps `3 7 15`, drop ghost notes on the even steps, and leave whole bars empty. Pads `1 4 6 8 11 13 16` stay in B minor. Stuck? Start with pad `13` on step `3`, pad `11` on step `7` and pad `8` on step `15`, then bend it. It is recorded without the bass or drums, so keep the hook's groove in your head.
    - **Rehearse first:** press **`[REC]`** during a pass to enter rehearsal (`CURRENT` shows `rHS`), play along without recording, then press `[REC]` again to record (manual p.48).
    - **Flubbed a pass?** Wipe just that Part for the row's bars and re-tap it: record_cheat.md, Phase 11 (steps 62–64: light only that Part's button, and use the row's start bar and bar count). For one wrong note use Realtime Erase (Section 4E).
    - **Same hook or bass in several patterns?** You can record it once and paste it with Part Copy instead of re-tapping (record_cheat.md, Phase 12), for example `U42` bars `17–32` into `U41` at bar `17`. Paste only into a pattern that already holds a recorded pass, so it is already 32 bars long.

---

### Phase C: Drums (Passes 14–32)
> The drum phase is record_cheat.md, Phase 8 again with new rows. The hook and bass are already in, so you tap along to them. **Hands off the knobs.**

16. **Climb back to `OCTAVE 0`:** press **`OCTAVE [+]`** until neither LED is lit. *(`[+]` dead? Power-cycle first, see §1.4.)* Then check that **GRID** is still lit and `PART [R]` is in the quantize aim.
17. **Set Pad Velocity to `80`** (as in step 12). Rows 14–27 use `80`; rows 28–32 use `110`, so change it once, before row 28.
18. **The pass routine** is record_cheat.md step 47 (a–h) exactly as written, with `PART [R]`.
19. **The 19 drum passes** *(top to bottom; the groups are rows 14–17 at `OCTAVE 0`, 18–22 at `-1`, 23–27 and 28–32 at `-2`)*:

| # | Pattern | `OCTAVE` | Velocity | Tap this (pad · steps · bars) |
| :-: | :-: | :-: | :-: | :--- |
| 14 | `U42` | `0` | `80` | **Lo conga** pad `6` · `4 11` · bars `9–32`<br>**Hi conga** pad `5` · `8 14` · bars `9–32` |
| 15 | `U43` | `0` | `80` | **Lo conga** pad `6` · `4 11` · bars `1–32`<br>**Hi conga** pad `5` · `8 14` · bars `1–32` |
| 16 | `U44` | `0` | `80` | **Lo conga** pad `6` · `4 11` · bars `1–32`<br>**Hi conga** pad `5` · `8 14` · bars `1–32` |
| 17 | `U45` | `0` | `80` | **Lo conga** pad `6` · `4 11` · bars `1–16`<br>**Hi conga** pad `5` · `8 14` · bars `1–16` |
| 18 | `U41` | `-1` | `80` | **Tambourine** pad `8` · `5 13` · bars `25–32` |
| 19 | `U42` | `-1` | `80` | **Tambourine** pad `8` · `5 13` · bars `1–32`<br>**Ride** pad `5` · `3 7 11 15` · bars `17–32` |
| 20 | `U43` | `-1` | `80` | **Tambourine** pad `8` · `5 13` · bars `9–32` |
| 21 | `U44` | `-1` | `80` | **Tambourine** pad `8` · `5 13` · bars `1–32`<br>**Ride** pad `5` · `3 7 11 15` · bars `1–32` |
| 22 | `U45` | `-1` | `80` | **Tambourine** pad `8` · `5 13` · bars `1–16`<br>**Ride** pad `5` · `3 7 11 15` · bars `1–16` |
| 23 | `U41` | `-2` | `80` | **Closed hat** pad `8` · `2 4 6 8 10 12 14 16` · bars `9–32`<br>**Open hat** pad `12` · `3 7 11 15` · bars `17–32` |
| 24 | `U42` | `-2` | `80` | **Closed hat** pad `8` · `2 4 6 8 10 12 14 16` · bars `1–32`<br>**Open hat** pad `12` · `3 7 11 15` · bars `1–32` |
| 25 | `U43` | `-2` | `80` | **Closed hat** pad `8` · `2 4 6 8 10 12 14 16` · bars `17–32`<br>**Open hat** pad `12` · `3 7 11 15` · bars `25–32` |
| 26 | `U44` | `-2` | `80` | **Closed hat** pad `8` · `2 4 6 8 10 12 14 16` · bars `1–32`<br>**Open hat** pad `12` · `3 7 11 15` · bars `1–32` |
| 27 | `U45` | `-2` | `80` | **Closed hat** pad `8` · `2 4 6 8 10 12 14 16` · bars `1–32`<br>**Open hat** pad `12` · `3 7 11 15` · bars `1–24` |
| 28 | `U41` | `-2` | `110` | **Kick** pad `2` · `1 5 9 13` · bars `1–32`<br>**Clap** pad `5` · `5 13` · bars `17–32` |
| 29 | `U42` | `-2` | `110` | **Crash** pad `15` · step `1` · bar `1` only (together with the first kick)<br>**Kick** pad `2` · `1 5 9 13` · bars `1–32`<br>**Clap** pad `5` · `5 13` · bars `1–32` |
| 30 | `U43` | `-2` | `110` | **Kick** pad `2` · `1 5 9 13` · bars `25–32`<br>**Clap** pad `5` · `5 13` · bars `25–32` |
| 31 | `U44` | `-2` | `110` | **Crash** pad `15` · step `1` · bar `1` only<br>**Kick** pad `2` · `1 5 9 11 13` · bars `1–32` *(step `11` is the funk hit, matching the hook)*<br>**Clap** pad `5` · `5 13` · bars `1–32` |
| 32 | `U45` | `-2` | `110` | **Crash** pad `15` · step `1` · bar `1` only<br>**Kick** pad `2` · `1 5 9 13` · bars `1–32`<br>**Clap** pad `5` · `5 13` · bars `1–24` |

20. **Pass tips**
    - **Entry bars:** watch `NEXT` and use the arrangement in §3. The open hat enters at bar `17` in `U41` but at bar `1` in `U42`.
    - **Loud group last:** the kick, clap and crash (rows 28–32) are the loud group, so set Pad Velocity to `110` before row 28.
    - **Rehearse first, and redo a drum cleanly:** see the *Pass tips* and *Need to redo a drum?* in record_cheat.md, steps 47g and 48.
    - **Struggling with the fast hats?** Slow the tempo before the pass (record_cheat.md, Pass tips). Tempo changes during recording aren't recorded, and selecting the pattern again restores `124.0`.

---

### Phase D: Lock It In, Chain It, Check It
21. **Listen to each pattern** (`U41`–`U45`, `PATTERN` mode, `[PLAY]`, then `[STOP]`) and compare it with §3.
22. **Lock the grid in (Edit Quantize), once per pattern:** select the pattern (stopped) and press **`[QUANTIZE]`** until **GRID** is lit. Hold **`[SHIFT] + [FUNC]`** and press Pad **`[11]`**, light **`PART [R]`, `[1]` and `[3]`** only → **`[ENTER]`** (`SUrE`) → **`[ENTER]`** (record_cheat.md step 53). Notes already on the grid don't change. Edit Quantize switches Play Quantize off by itself, so light GRID again for the next pattern, and finish with none of GRID / GROOVE / SHUFFLE lit. *(Part 2 is never quantized.)*
23. **Optional swing** *(instead of step 22, not after it)*: as record_cheat.md step 52, but with **`PART [R]`, `[1]` and `[3]` lit together** so the three swing as one.
24. **Optional balance:** per pattern, record_cheat.md step 51 (the safe routine, `LEVEL` by ear), then Setup Write. Start with Parts 3 and R near the top and Part 2 lowest.
25. **Clean up:** record_cheat.md step 53: `OCTAVE` back to `0`, Pad Velocity back to the value you noted in step 12 above, no PART button dark in the `[RHYTHM MUTE]` / `[PART MUTE]` views, quantize off, `TEMPO` `124.0`.
26. **Chain `S-2`:** follow record_cheat.md, Section 5, Phase 5 (steps 25–31) with **`S-2`** instead of `S-1`, entering **`U41`**, **`U42`**, **`U43`**, **`U44`**, **`U45`** in turn (**`[ENTER]`** after each) and finishing with **`[STOP]`**. If `NEXT` shows a pattern name instead of `---` when you select `S-2`, it already has steps (step 26 there).
27. **Song Setup Write (`124.0`):** `SELECT` → `TEMPO` → `124.0` (as step 6), then hold **`[SHIFT] + [FUNC]`** and press Pad **`[15]`** → **`[ENTER]`**.
28. **Hear it as a song:** press **`[SHIFT] + [BWD]`**, then **`[PLAY]`**, hands off the knobs, with a stopwatch. It should run about **5:10**.
29. **Check free memory again** (step 3) and **back up** with Bulk Dump (record_cheat.md, Section 4F).

---

## 6. Quick Fixes

| Symptom | Fix |
| :--- | :--- |
| A pass sounds doubled or messy | You tapped over bars that were already recorded. Wipe that Part's bars for the row (record_cheat.md, steps 62–64) and re-tap. |
| The hook feels loose against the drums | The quantize aim missed Part 1 (step 11). Aim it again and run Edit Quantize with Parts R, 1 and 3 lit (step 22). |
| The free-style is too busy | Wipe Part 2 in that pattern (light only `PART [2]`) and retake it sparser, or remove single notes with Realtime Erase (Section 4E). |
| Pads play the wrong sounds | The `OCTAVE` or the Rhythm Set is wrong. Compare with the row and with record_cheat.md §6.2 (`d07`). |
| `S-2` stops partway through | A pattern in it has no musical data. Play each of `U41`–`U45` on its own. |
| The tempo is slightly off | Re-select the pattern (it restores `124.0`), or redo step 27 for the Song. |

---

## 7. Making It Longer

The Original is 6:28, about 200 bars at 124 BPM. The cheapest way to get closer is to **repeat `U44`** in the Song: `S-2` = `U41 U42 U43 U44 U44 U45` = 192 bars = **6:12**, with no extra recording. Clear `S-2` and chain it again as in step 26. Matching it to the second would need 8 more bars, for example an 8-bar pattern (`LGH` `8`) before the outro.

---

## Sources

- [Discogs: Hardrive – Deep Inside (Strictly Rhythm SR EP2, 1993)](https://www.discogs.com/release/20174-Hardrive-Deep-Inside): tracklist, durations and BPM notes
- [diggerdigger: Deep Inside by Hardrive](https://diggerdigger.com/track/hardrive-deep-inside/): BPM and key
- [Insomniac: Hardrive "Deep Inside"](https://www.insomniac.com/music/from-the-crate-hardrive-deep-inside/): the *Beautiful People* link and the 1995 Masters at Work remix
- [Roland MC-303 Owner's Manual (Internet Archive)](https://archive.org/details/synthmanual-roland-mc-303-owners-manual): pp.13, 16, 20, 61–63
- [Sweetwater: Roland MC-303 Copying Patterns](https://www.sweetwater.com/sweetcare/articles/roland-mc-303-copying-patterns/): 50 User locations
