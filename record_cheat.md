# Roland MC-303 Groovebox — Recording & Sequencing Cheat Sheet

A button-by-button reference for recording **Parts**, **Phrases (RPS)**, **Patterns**, and **Songs** on the Roland MC-303, cross-checked against the text of the official 1996 *Roland MC-303 Owner's Manual* and Roland/Sweetwater knowledge-base articles. It covers dual-function knobs, metronome/lead-in setup, deletion operations, and an end-to-end **120 BPM** workflow for permanently recording a ~2-minute (2 × 32 bars = 2:08) single-instrument track (`t01-15` / `Tri Lead 1`) with baked-in live `CUTOFF`, `RESONANCE`, `LFO`, `ENVELOPE`, and `LEVEL` tweaks that scales up to a 4-minute+ song. **Section 6** then layers a gradually building deep-house percussion part (Part R) over those same two patterns.

> **Verification note:** The manual prints its display read-outs as figures that could not be machine-read, and nothing here has been run on a physical unit. Display strings confirmed by Roland support articles: `ErS`, `SUrE`, `bEt`, `LGH`, `Cnt`, `LoP`. The rest are read from the manual's own display figures: `rHS` (rehearsal), `ntE` (Wait Note), `OCt`, `rES`, `d01` (Rhythm Set), `Mt 1`/`Mt 2`, `PuL`, `SnG`/`CLr`, `---` (empty song) and `S-1`. Anything marked *(unconfirmed)* is a best guess—check it on your MC-303.

---

## 1. MC-303 Sequencer Hierarchy & Memory Architecture

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ SONG (S-1 to S-10 | up to 999 steps per Song)                               │
│  Stores: Pattern playback order + Song Setup (Master Tempo & Global EFX)    │
│   │      *Save Song Tempo/EFX via Song Setup Write: [SHIFT]+[FUNC]+Pad[15]  │
│   │                                                                         │
│   ├─► USER PATTERNS (U01–U50; shown as lowercase u01–u50 when empty)        │
│   │    • 1–32 bars | 2/4, 3/4, or 4/4 | Notes + Realtime Knob Modify data   │
│   │    • Pattern Setup (Tones, Part levels/knobs, Mutes, Standard Tempo)    │
│   │      *MUST save Tone/Tempo/Knob init via Pattern Setup Write:           │
│   │       [SHIFT]+[FUNC]+Pad[15] → [ENTER] (otherwise lost on pattern swap) │
│   │        ├─► PART R (Drums — MIDI Ch 10, 1 of 12 Rhythm Sets)             │
│   │        └─► PARTS 1–7 (Melodic — MIDI Ch 1–7, 448 Tones, e.g. t01-15)    │
│   │                                                                         │
│   ├─► VARIATION PATTERNS (L01–Q50 | 300 slots across 6 banks)               │
│   │    • Stores Part Mute & Rhythm Mute states pointing to any Preset/User  │
│   │      Pattern (save via [SHIFT]+[FUNC]+Pad[13] → [VALUE] → [ENTER]×2)    │
│   │                                                                         │
│   └─► PRESET PATTERNS (Read-Only — copy to U01–U50 to edit)                 │
│        • A01–C33 (133 Dance Patterns) & E01–I11 (211 RPS Phrase Patterns)   │
│                                                                             │
│ PERFORMANCE SETS (30 Sets each, triggered from Keyboard Pads 1–16)          │
│  • RPS SETS (1–30): Triggers 1 isolated Part from any Pattern per Pad       │
│  • PATTERN SETS (1–30): Switches full Patterns (+ Arpeggio setup) per Pad   │
└─────────────────────────────────────────────────────────────────────────────┘
```

> **Critical MC-303 Memory Rule (No `WRITE` Button, Two Distinct Data Types):**
> 1. **Musical Data (Notes, Knob Movements, Song Steps):** Stored into memory **immediately** as you record them—there is no `[WRITE]` button for notes or song steps.
> 2. **Setup Data (Selected Tone like `t01-15`, Tempo, Initial Knob Positions, Part Mutes, EFX):** Temporary in edit buffer! If you switch patterns or power off without running **Pattern Setup Write** (**`[SHIFT] + [FUNC] + Pad [15]` → `[ENTER]`** in `PATTERN` mode) or **Song Setup Write** (**`[SHIFT] + [FUNC] + Pad [15]` → `[ENTER]`** in `SONG` mode), your Tone, Tempo, and starting knob settings will revert!

> **Other limits worth knowing:**
> - **Preset (`A–C`, `E–I`) and Variation (`L–Q`) patterns are read-only.** Trying to modify, edit, or store settings on them shows **Error 8** (per Roland support). Copy a Preset pattern to a User Pattern first (Section 4F); Variation patterns can't be copied.
> - **You may get fewer than 50 User Patterns** if they hold a lot of data, and long knob sweeps add up fast. Check free memory with **`[SHIFT] + Pad [16]`** → `SELECT [>]` ×8 (shows the remaining %); Data Thin (Section 5, Phase 4) frees space.
> - **Songs store only pattern numbers, not notes.** Editing or deleting a pattern changes every Song that uses it, and a pattern with no data halts song playback.
> - **Variation Patterns (`L–Q`) can't be registered as RPS phrases.**
> - **Back up finished work** with Bulk Dump to an external MIDI sequencer (Section 4F)—the manual warns that memory can be lost after a malfunction or repair.

---

## 2. Front Panel, Dual-Function Knobs & Display Reference

The MC-303 has a **6-character 7-segment LED display** with a **`CURRENT`** area (left) and a **`NEXT`** area (right).

| Control Group | Exact Panel Label | Function & Display Behavior |
| :--- | :--- | :--- |
| **Play Mode** | `[PLAY MODE]` | Toggles between **`SONG`** and **`PATTERN`** LEDs (`[SHIFT] + [PLAY MODE]` = Demo mode). |
| **Select Cursor** | `SELECT [<] [>]` | Moves LED across **`PTN/SONG` · `PTN SET` · `RPS SET` · `TONE` · `TEMPO`**. Inside `[REC]` standby or `[SHIFT]` menus, steps through sub-parameters (`bEt`, `LGH`, `Cnt`, `LoP`). |
| **Data Dial** | `[VALUE]` | Edits the active parameter. Hold **`[SHIFT] + [VALUE]`** to jump by 10s (or `1.0` BPM in `TEMPO`). |
| **Transport** | `[BWD/TIE]`, `[FWD/REST]`, `[REC]`, `[STOP]`, `[PLAY]` | Rewind/Fast-Forward (`[SHIFT]+[BWD]` jumps to start; `[SHIFT]+[FWD]` jumps to end). In Step Rec 1: `[BWD/TIE]` = Tie, `[FWD/REST]` = Rest. `[REC]` blinks in standby, lights solid when recording. |
| **Confirm / Cancel** | `[ENTER]`, `[EXIT]` | `[ENTER]` confirms edits/prompts (`SUrE`); `[EXIT]` cancels or backs out of menus. |
| **Modifiers** | `[SHIFT]`, `[FUNC]` | **`[SHIFT]`** + Pad `[1]–[16]` opens black-framed parameter menus.<br>**`[FUNC]`** (press so LED **blinks**) switches all dual-label knobs to their secondary function.<br>**`[SHIFT] + [FUNC]` + Pad `[1]–[16]`** opens white-framed Edit/Write commands.<br>**`[SHIFT] + [FUNC]` + turn a knob** shows that knob's value: `CURRENT` shows the parameter name (the manual's cutoff example reads `CUt`) and `NEXT` shows the number. |
| **Cutoff / Level Knob** | `CUTOFF / LEVEL` | **Same physical knob!**<br>• **`[FUNC]` LED dark:** Adjusts **`CUTOFF`** (`-50` to `+50`).<br>• **`[FUNC]` LED blinking:** Adjusts Part **`LEVEL` / Volume** (`0` to `127`). |
| **Resonance / Pan Knob** | `RESONANCE / PANPOT` | • **`[FUNC]` LED dark:** **`RESONANCE`** (`-50` to `+50`).<br>• **`[FUNC]` LED blinking:** **`PANPOT`** (`L63`–`0`–`R63`). |
| **Envelope Knob** | `ENVELOPE / RELEASE` + `[ENVELOPE]` | • **`[FUNC]` dark + `[ENVELOPE]` dark:** **`ATTACK`** (`-50` to `+50`).<br>• **`[FUNC]` dark + `[ENVELOPE]` lit:** **`DECAY`** (`-50` to `+50`).<br>• **`[FUNC]` blinking:** **`RELEASE`** (`-50` to `+50`). |
| **LFO / Porta Knob** | `LFO / PORTA TIME` + `[LFO]` | • **`[FUNC]` dark + `[LFO]` dark:** **`LFO RATE`** (`-50` to `+50`).<br>• **`[FUNC]` dark + `[LFO]` lit:** **`LFO MOD` depth** (`0` to `127`).<br>• **`[FUNC]` blinking:** **`PORTA TIME`** (`0` to `127`). |
| **Scale / Metronome** | `[SCALE / MEASURE]` | Hold while playing/stopped to view total bars (`CURRENT`) & `bar.beat` (`NEXT`). Selects step grid in Step Rec. **`[FUNC] + [SCALE/MEASURE]` toggles Metronome On/Off!** |
| **Tap / Loop Rest** | `[TAP / LOOP REST]` | Tap 3+ times for Tap Tempo. **`[SHIFT] + [TAP/LOOP REST]`** toggles Loop Rest (`LoP`) in `[REC]` standby. Hold `[TAP]` in Erase mode (`ErS`) to erase **knob tweaks only**. |
| **Part Mode & Tracks** | `[PART SELECT]`, `[PART MUTE]`, `[RHYTHM MUTE]`, `PART [R] [1]–[7]` | Make sure **`[PART SELECT]`** is lit so pressing `PART [R, 1–7]` selects the active Part (instead of muting Parts or Rhythm drum groups). |
| **Pads & Octave** | `[KEYBOARD PADS 1–16]`, `OCTAVE [-]` / `[+]` | 16-key pad keyboard (`Pad [2]` = `C4` when Octave = `0`; shift `-4` to `+4` octaves). Ensure `[PTN SET]` and `[RPS SET]` are **dark** to play notes! |
| **Transpose / Erase** | `[TRANSPOSE / ERASE]` | Live transpose (`[TRANSPOSE]` + `[VALUE]`). During recording, **`[SHIFT] + [TRANSPOSE/ERASE]`** toggles Realtime Erase (**`ErS`**). |
| **Rear Bass Boost** | `LOW BOOST` (rear) | Hardware bass-boost circuit on the audio output (not recorded in sequencer). |

> **Realtime Modify (`RTM`) Recording Rule:** All 10 parameters in the `REALTIME MODIFY` section (`CUTOFF`, `LEVEL`, `RESONANCE`, `PANPOT`, `ATTACK`, `DECAY`, `RELEASE`, `LFO RATE`, `LFO MOD`, `PORTA TIME`) are permanently recorded into a User Pattern (`U01–U50`) when moved during **Pattern Realtime Recording** (`[REC]` + `[PLAY]`). **`SONG` mode cannot record knob tweaks**—it plays back the automation recorded inside each Pattern.
>
> **Playback override:** If you move a knob (past one of its 11 switch points) while a pattern or song is playing a Part that already has recorded knob data, your knob takes priority, that Part's recorded knob data is cancelled, `REALTIME MODIFY` lights and the `PART` button blinks. The recorded data returns when you press the blinking `PART` button again, return to the start of the pattern, or switch patterns.
>
> **Shared pots *(inferred from the hardware—confirm on your unit)*:** One physical pot serves two or three parameters (`CUTOFF`/`LEVEL`; `LFO RATE`/`LFO MOD`/`PORTA TIME`; `ATTACK`/`DECAY`/`RELEASE`). The pots are not motorised, so after you toggle `[FUNC]`, `[LFO]` or `[ENVELOPE]` the newly selected parameter will most likely jump to wherever the pot is sitting as soon as you touch it. Park the pot at the value you want to start from *before* you move it—the blank `Loop Rest` bar is a good time—and hold `[SHIFT] + [FUNC]` while turning to read the exact value.

---

## 3. Recording Modes Overview

| Mode | Best For | Exact Key Sequence to Enter | How Data Is Captured |
| :--- | :--- | :--- | :--- |
| **Realtime Recording** | Live melodies, chords, arpeggios, & **recording knob sweeps (`CUTOFF`, `LEVEL`, etc.)** | `PATTERN` mode (`U01–U50`) → `[REC]` (blinks) → set `bEt/LGH/Cnt/LoP` → `PART [R/1–7]` → `[PLAY]` | **Notes:** Loop Mix (overdubs on each pass).<br>**Knobs:** Loop Replace per parameter (re-turning `CUTOFF` overwrites `CUTOFF`; turning `LEVEL` on pass 2 layers `LEVEL` alongside `CUTOFF`). |
| **Step Recording 1 (Melodic `1–7`)** | Tight 16th-note acid basslines, arpeggios, chords, ties/slides | `PATTERN` mode (`U01–U50`) → `[REC]` → `PART [1–7]` → **`[REC]` again** (`STEP REC` lights) → `[PLAY]` | Step-by-step entry via `[PADS 1–16]`, `[FWD/REST]` (Rest), `[BWD/TIE]` (Tie), `[SCALE/MEASURE]` (grid), `PART [R–3]` (Vel), `PART [4–7]` (Gate). *Overwrites from start point forward.* |
| **Step Recording 2 (Drum Grid `R`)** | Classic TR-808/909 16-step drum machine programming | `PATTERN` mode (`U01–U50`) → `[REC]` → `PART [R]` → **`[REC]` again** (`STEP REC` lights) → `[PLAY]` | Pattern loops live! Hold `[SHIFT] + Pad [1–16]` to pick drum sound, release `[SHIFT]`, tap `Pads [1–16]` to toggle steps on/off; `[FWD]`/`[BWD]` switches bars. |
| **Microscope Edit** | Surgical single-note velocity/gate edits, note delete, or TB-303 slides | `PATTERN` mode → `[REC]` (standby) → `PART [R/1–7]` → **`[REC]` again** (`STEP REC` lit, `bar-beat` / `clock` shown). *(Inside Step Recording, `[REC]` toggles between the step-input display and the Microscope. During **Realtime** Recording, `[REC]` enters Rehearsal mode `rHS` instead.)* | Turn `[VALUE]` (or `[FWD]`/`[BWD]`) to inspect notes at 96 PPQN resolution; edit Vel/Gate, insert Portamento slides or Hold messages, or delete individual notes. |
| **RPS Phrase Reg.** | Triggering isolated single-Part loops live from Pads `1–16` | `[PART MUTE]` all parts except 1 → `[RPS SET]` lit → hold **`[RPS SET] + Pad [1–16]`** | Registers pointer to that Pattern + Part on the Pad; can be triggered live or recorded into another User Pattern. |
| **Song Recording** | Chaining up to 999 Patterns into a linear song (`S-1` to `S-10`) | `[PLAY MODE]` (`SONG` lit) → `S-1..S-10` → `[REC]` → `[PLAY]` | Select Pattern with `[VALUE]` → press `[ENTER]` to append step → `[STOP]` when done. |

---

## 4. Core Operations: Hardware-Exact Key Sequences

### A. Setting Metronome, Lead-In (`Cnt`), Time Signature (`bEt`), Length (`LGH`) & Loop Rest (`LoP`)

1. **Metronome Setup (Two Ways):**
   - **Instant Toggle (Anytime):** Hold **`[FUNC]` + press `[SCALE / MEASURE]`** to toggle the metronome click on or off during recording.
   - **System Metronome Mode & Volume (While Stopped):**
     1. Hold **`[SHIFT]` + press Keyboard Pad `[16]`** (System Settings).
     2. Press **`SELECT [>]` 5 times** to reach Metronome Mode (`Mt 1`) → turn **`[VALUE]`** to **`rEC`** (REC ONLY: click during recording only), **`ALY`** (ALWAYS), **`P-r`** (PLAY & REC), or **`oFF`**.
     3. Press **`SELECT [>]` once more** (6th page, `Mt 2`) to adjust **Metronome Volume (`0–127`)** with **`[VALUE]`** → press **`[EXIT]`**.
2. **Recording Standby Parameters (`bEt`, `LGH`, `Cnt`, `LoP`):**
   - In `PATTERN` mode (`[PLAY MODE]` → `PATTERN` lit), select a User Pattern **`U01–U50`** and press **`[REC]`** (`REC` LED blinks).
   - Use **`SELECT [<] [>]`** to step between the **4 recording parameters** and turn **`[VALUE]`** to set each:
     1. **`bEt` (Beat / Time Signature):** `2/4`, `3/4`, or `4/4` *(default `4/4`; can only be set on an empty `u` pattern)*.
     2. **`LGH` (Pattern Length):** `1` to `32` measures *(default `4`; you can lengthen an existing pattern anytime, but to shorten it you must first use Delete Measure `[SHIFT]+[FUNC]+Pad[4]` with data type `PHRASE` so the Tone/setup data is kept—see Section 4E)*.
     3. **`Cnt` (Count-In / Lead-In):**
        - **`0`**: Recording starts immediately when you press `[PLAY]`.
        - **`1`**: **1-measure lead-in** before Bar 1 Beat 1 (4 clicks in 4/4).
        - **`2`**: **2-measure lead-in** (default; 8 clicks in 4/4).
        - **`Wait Note`** (`ntE`): Waits silently and starts recording the instant you strike a Keyboard Pad (or press a hold pedal). `[PTN SET]` and `[RPS SET]` must be dark.
     4. **`LoP` (Loop Rest):** `oFF` (default) or **`on`** *(can also toggle with **`[SHIFT] + [TAP/LOOP REST]`** while in `[REC]` standby)*. When **`on`**, inserts **1 temporary unrecorded blank measure** at the end of the pattern so you can sweep knobs right up to the final beat and hit `[STOP]` (or switch `[FUNC]`) cleanly without overwriting Bar 1!
   - *(These defaults apply to a brand-new pattern. When you record again onto an already-recorded pattern, the settings from its previous recording are reused—manual p.47—but it costs nothing to re-check them.)*

### B. Realtime (Live) Recording & Rehearsal Mode (`rHS`)
1. Select `U01–U50` (`PATTERN` mode), ensure `[PTN SET]` and `[RPS SET]` are **dark**, select your Part (`[PART SELECT]` → `PART [R/1–7]`), and choose your Tone (`SELECT` → `TONE` → `[VALUE]`). *(Tone choices live in the edit buffer until you run Pattern Setup Write after recording—Section 4F.)*
2. Press **`[REC]`** (blinks) → set `bEt`, `LGH`, `Cnt`, `LoP` via `SELECT [<]/[>]` + `[VALUE]` → press target **`PART [R]` or `[1]–[7]`**. *(Optional: press `[QUANTIZE]` now if you want input quantization.)*
3. Press **`[PLAY]`** (or strike a pad if `Cnt = Wait Note`). After the lead-in, `REC` lights solid, `CURRENT` shows total bars, and `NEXT` shows the current bar.
4. Play **`[KEYBOARD PADS 1–16]`** and/or turn **`REALTIME MODIFY` knobs** (`CUTOFF/LEVEL`, `RESONANCE/PANPOT`, `ENVELOPE`, `LFO`).
5. **Switch Parts Non-Stop (`Rehearsal Mode`):** Press **`[REC]`** while recording—`REC` blinks and `CURRENT` displays **`rHS`**. Practice notes or press another **`PART [R/1–7]`** without recording; press **`[REC]`** again to resume recording!
6. Press **`[STOP]`** when finished.

### C. Step Recording 1 (Melodic Parts `1–7`)
1. Select `U01–U50` (`PATTERN` mode) → press **`[REC]`** (blinks) → set `bEt` & `LGH` → press **`PART [1]–[7]`**.
2. Press **`[REC]` a second time**: the **`STEP REC`** LED lights and the Microscope position (`1-1` `00` = Bar 1, Beat 1, Clock 00) appears. *(If not at `1-1` `00`, turn `[VALUE]` counter-clockwise or press `[SHIFT]+[BWD]`.)*
3. Press **`[PLAY]`** (`PLAY` and `REC` light solid).
4. Set note properties anytime before pressing a pad:
   - **Step Grid (Note Value):** Press **`[SCALE / MEASURE]`** repeatedly to light `16th triplet` (16 clocks), `8th triplet` (32), `32nd` (12), or **`16th note`** (24 clocks).
   - **Velocity:** Press **`PART [R]`** (`20`), **`[1]`** (`64`), **`[2]`** (`100`), or **`[3]`** (`127`). *(Hold `PART [R–3]` + turn `[VALUE]` to customize.)*
   - **Gate Time Ratio:** Press one of **`PART [4]`–`[7]`**. Factory values are around `50%` (staccato), `80%` (normal) and `100%` (tenuto), but the manual's figure doesn't show which button holds which—**hold a `PART [4–7]` button to read its value** on the display (and turn `[VALUE]` while holding to change it).
5. Enter musical events (advances automatically on release):
   - **Single Note:** Press & release **`[KEYBOARD PAD 1–16]`** (use `OCTAVE [-]/[+]` for pitch range).
   - **Chord:** Hold multiple pads together, then release all at once.
   - **Rest (Silence):** Press **`[FWD / REST]`** (advances by current Step Time).
   - **Tie (Hold / Lengthen Previous Note):** Press **`[BWD / TIE]`** (e.g., enter a `16th` note + press `[BWD/TIE]` 3 times = quarter note).
   - **Undo Last Note:** Hold **`[SHIFT] + [BWD/TIE]`** (deletes and auditions the removed note).
6. Press **`[STOP]`** when finished. *(Warning: Step Rec 1 overwrites existing notes on that Part from the start point forward.)*

### D. Step Recording 2 — TR-Style Drum Grid (Rhythm Part `R`)
1. Select `U01–U50` (`PATTERN` mode) → press **`[REC]`** (blinks) → set `bEt` & `LGH` → press **`PART [R]`**.
2. Press **`[REC]` a second time** (`STEP REC` lights), then press **`[PLAY]`** (the drum loop plays continuously while you program!).
3. Press **`[SCALE / MEASURE]`** to pick grid resolution (typically **`16th note`** = Pads `1–16` represent 1 full bar of 16 steps).
4. **Pick Drum Instrument:** Hold **`[SHIFT]`** (while holding `[SHIFT]`, press `OCTAVE [-]/[+]` if needed, e.g., `-2` for kicks/snares/hats) and tap a **`[KEYBOARD PAD 1–16]`** to hear & select that drum sound, then **release `[SHIFT]`**.
5. **Toggle Steps:** Press **`[KEYBOARD PADS 1–16]`** to light (add hit) or unlight (remove hit) steps in the current bar. Press `PART [R–3]` to change velocity for newly entered hits.
6. Press **`[FWD]`** or **`[BWD]`** to move the 16-pad grid to the next/previous measure.
7. Press **`[STOP]`** when finished.

### E. Deleting & Erasing Everything (Single Note, Knob Tweaks, Part, Measure, Pattern, Song)

| What You Want to Delete | Exact Hardware Key Sequence |
| :--- | :--- |
| **Single Note or Single Drum Sound (Realtime)** | During Realtime Recording (`[REC]` + `[PLAY]`): press **`[SHIFT] + [TRANSPOSE/ERASE]`** (`CURRENT` shows **`ErS`**). **Hold the specific Keyboard Pad** while the playhead passes over the unwanted note(s). Press `[SHIFT]+[TRANSPOSE/ERASE]` or `[EXIT]` to leave `ErS`. |
| **Range of Notes (Realtime)** | In **`ErS`** mode (`[SHIFT] + [TRANSPOSE/ERASE]`), **hold the lowest and highest Keyboard Pads** of the range to erase everything between them. |
| **Knob Tweaks ONLY — Keep Notes! (Realtime)** | In **`ErS`** mode (`[SHIFT] + [TRANSPOSE/ERASE]`), **hold `[TAP / LOOP REST]`** over the section where you want to wipe `Modify data` (`CUTOFF`, `LEVEL`, etc.) without erasing notes! |
| **All Data in Active Part (Realtime)** | In **`ErS`** mode (`[SHIFT] + [TRANSPOSE/ERASE]`), **hold `[REC]`** for one full loop pass. |
| **Single Specific Note (Microscope Precision)** | Stopped in `PATTERN` mode: press **`[REC]`** (standby) → select the Part → press **`[REC]`** again (`STEP REC` lit, Microscope shown). Turn **`[VALUE]`** (or `[FWD]`/`[BWD]`) to locate the note (its Keyboard Pad lights up; check `OCTAVE [-]/[+]` if unlit). Hold **`[SHIFT] + [FUNC]` + press the lit Keyboard Pad** (pad goes dark = deleted). Press `[STOP]`. |
| **Single Drum Step (Step Rec 2)** | In Step Rec 2 (`PART [R]`), select that drum (`[SHIFT] + Pad`), move to the bar (`[FWD]`/`[BWD]`), and **tap the lit step Pad `1–16`** so its LED goes dark. |
| **Erase Bars (Leaves Blank Bars in Place)** | Stopped in `PATTERN` mode: **`[SHIFT] + [FUNC] + Pad [3]`** (`ErS`) → light target `PART [R/1–7]` → `[VALUE]` start bar → `[ENTER]` → `[VALUE]` bar count (`1–32` or `ALL`) → `[ENTER]` (`SUrE`) → `[ENTER]`. *(Does not erase Setup data or shorten pattern.)* |
| **Delete Entire User Pattern (`U01` → `u01`)** | Stopped in `PATTERN` mode on `U01–U50`:<br>1. Hold **`[SHIFT] + [FUNC]` + press Pad `[4]`** (Delete Measure).<br>2. Press **`PART [R]` and `[1]–[7]`** so **all 8 Part LEDs are lit solid**, and turn **`[VALUE]`** to the data type **`ALL`** *(not `PHRASE`/`SETUP`—`ALL` is what removes the pattern itself)*.<br>3. Press **`[ENTER]`** (`CURRENT` = `1` blinking).<br>4. Press **`[ENTER]`** (`NEXT` blinks) → turn **`[VALUE]`** to **`ALL`** *(number of measures)*.<br>5. Press **`[ENTER]`** (`SUrE`) → press **`[ENTER]`** again. *(Per Roland: a deleted pattern shows a lowercase `u` and holds no note or setup data; an erased pattern shows an uppercase `U` and keeps its setup, e.g. its length.)* |
| **Shorten a Pattern (Delete Bars, Closes the Gap)** | Stopped in `PATTERN` mode: **`[SHIFT] + [FUNC] + Pad [4]`** (Delete Measure) → press the target `PART` button(s) (all of `R, 1–7` shortens the pattern itself) → turn **`[VALUE]`** to the data type **`PHRASE`** (notes + knob data only) → `[ENTER]` → `[VALUE]` first bar to delete → `[ENTER]` → `[VALUE]` number of bars (`1–32`, or `ALL` = to the end) → `[ENTER]` (`SUrE`) → `[ENTER]`. *(The manual says data type `ALL` also deletes the Parts' **setup data** (Tone, knob settings)—use `PHRASE` unless you want that.)* |
| **Delete 1 Step or Clear Entire Song** | Stopped in `SONG` mode on `S-1..S-10`: **`[SHIFT] + [FUNC] + Pad [4]`** → `[VALUE]` (or `[FWD]`/`[BWD]`) to step `#` (or `END` to initialize the entire Song—this also deletes its saved setup data: tempo and effects) → `[ENTER]` (`SUrE`) → `[ENTER]`. *(Or press `[REC]` on a song that already has steps—the display shows `SnG > CLr`—then `[ENTER]` to clear & re-record from scratch.)* |

### F. Essential Saving, Copying, RPS & Song Operations
- **Save Tone, Tempo & Part Knobs (`Pattern Setup Write`):** In `PATTERN` mode, hold **`[SHIFT] + [FUNC]` + press Pad `[15]`** (`SUrE`) → press **`[ENTER]`**. Stores, for all Parts at once: Tones/Rhythm Set, Part parameters (level, pan, cutoff, resonance, envelope, LFO…), effect part levels, mutes, and the pattern's standard tempo.
  - **Writes only to User Patterns.** On a Preset or Variation pattern you get **Error 8**.
  - **Run it *before* your knob passes, never after.** It stores whatever the knobs are set to *right now*, so writing it after a recording pass would bake the end-of-pass values in as the pattern's starting sound.
- **Copy Entire Pattern (`Pattern Copy`):** Select source pattern → **`[SHIFT] + [FUNC] + Pad [1]`** → `[VALUE]` (`ALL`, `PHRASE`, or `SETUP`) → `[ENTER]` → `[VALUE]` destination (`U01–U50`) → `[ENTER]` (`SUrE`) → `[ENTER]`.
- **Register an RPS Phrase (`RPS Sets 1–30`):**
  1. Select source Pattern (e.g., `U01` or `A02`; Variation patterns `L–Q` can't be registered).
  2. Press **`[PART MUTE]`** and mute **every Part EXCEPT the 1 Part** you want on the pad *(leaving 2+ Parts unmuted gives an error and the phrase isn't registered; the manual's error number isn't legible)*.
  3. Press **`SELECT [<]/[>]`** to **`RPS SET`**, press **`[RPS SET]`** (lit), and turn **`[VALUE]`** to pick RPS Set `1–30`.
  4. **Hold `[RPS SET]` + press target Keyboard Pad `[1]–[16]`**. Done! *(With `[RPS SET]` lit, press that pad anytime to fire the phrase.)*
- **Record a Song (`S-1` to `S-10`) & Save Song Tempo (`Song Setup Write`):**
  1. Press **`[PLAY MODE]`** (`SONG` lit) → `SELECT [<]/[>]` to `PTN/SONG` → `[VALUE]` to **`S-1`–`S-10`** (`---` in `NEXT` = empty; a pattern name there means the song already has steps).
  2. Press **`[REC]`** (`STEP REC` lights; if the song already has steps the display shows `SnG > CLr`—press **`[ENTER]`** to clear it, or `[EXIT]` to cancel).
  3. Press **`[PLAY]`** (`CURRENT` = `1`).
  4. Turn **`[VALUE]`** to choose Pattern → press **`[ENTER]`** (advances to step `2`). Repeat for each section *(undo mistake with **`[SHIFT] + [BWD]`**)*.
  5. Press **`[STOP]`** to finish chaining patterns.
  6. **Save Song Tempo & Global EFX:** Set `TEMPO` (`SELECT` → `TEMPO` → `[VALUE]`), then hold **`[SHIFT] + [FUNC]` + press Pad `[15]`** (`SUrE`) → **`[ENTER]`**. *(Stores the song's tempo plus its overall Delay/Reverb and Flanger/Chorus settings; once written, the song tempo overrides each pattern's own standard tempo.)*
- **Back Up Your Work (`Bulk Dump`):** Dumps User Patterns, Songs, RPS Sets and Pattern Sets to an external MIDI sequencer (MC-303 `MIDI OUT` → sequencer `MIDI IN`). With playback stopped, hold **`[SHIFT] + [FUNC]` + Pad `[16]`** (Bulk Dump display), start recording on the sequencer, then press **`[ENTER]`** on the MC-303. Each time transmission pauses, press **`[ENTER]`** again for the next packet until the completion display appears (`[STOP]` or `[EXIT]` cancels). *Restoring a dump erases the MC-303's current User Patterns and Songs (owner's manual p.78–79).*

### G. Real-Time Tweaking & Recording for `LFO` and `ENVELOPE`

#### 1. LFO (`LFO / PORTA TIME` Knob + `[LFO]` Button + `[SHIFT]` Pads `9–12`)
> **Critical MC-303 LFO Gotcha:** Turning the `LFO` knob produces **no audible change** if `LFO PITCH`, `LFO FILTER`, and `LFO AMP` are all at `0` for that Tone! Always set your LFO waveform and destination depths **before** recording, and save them with **Pattern Setup Write** (`[SHIFT] + [FUNC] + Pad [15]` → `[ENTER]`).

1. **Pre-Set LFO Waveform & Destination Depths (Part Setup Menus):**
   - Select your Part (`[PART SELECT]` → `PART [1–7]`), then hold **`[SHIFT]`** and press:
     - **Pad `[9]` (`LFO WAVE`):** Turn `[VALUE]` to pick **`SINE`** (smooth vibrato/wah), **`TRIANGLE`**, **`SAW`**, **`SQUARE`** (rhythmic gate/trill), or **`RANDOM 1 / 2`** (sample-&-hold bleeps) → `[EXIT]`.
     - **Pad `[10]` (`LFO PITCH`):** Turn `[VALUE]` (`0–127`) to set **pitch vibrato** depth → `[EXIT]`.
     - **Pad `[11]` (`LFO FILTER`):** Turn `[VALUE]` (`0–127`, e.g., `50–80`) to set **filter wah / wobble** depth → `[EXIT]`.
     - **Pad `[12]` (`LFO AMP`):** Turn `[VALUE]` (`0–127`) to set **volume tremolo / gate** depth → `[EXIT]`.
   - Save into the Pattern: **`[SHIFT] + [FUNC] + Pad [15]`** (`SUrE`) → **`[ENTER]`**.
2. **Tweak & Record LFO Live (`[REC]` + `[PLAY]` in `PATTERN` Mode):**
   - Make sure **`[FUNC]` LED is dark** *(if `[FUNC]` blinks, the knob controls `PORTA TIME` instead of LFO)*.
   - **Bring In LFO Depth (`LFO MOD`, `0–127`):** Press **`[LFO]`** so its LED **lights up**, then rotate **`LFO / PORTA TIME`** clockwise to deepen the wobble/vibrato/tremolo (`0` = off).
   - **Sweep LFO Speed (`LFO RATE`, `-50` to `+50`):** Press **`[LFO]`** so its LED **goes dark**, then rotate **`LFO / PORTA TIME`** clockwise for faster modulation or counter-clockwise for slow sweeps.
   - *(This is one shared pot—park it where you want to start before touching it; see the shared-pots note in Section 2.)*

#### 2. Envelope (`ENVELOPE / RELEASE` Knob + `[ENVELOPE]` Button + `[FUNC]` Button)
The MC-303's Envelope shapes **both volume and filter contour** over time (`A` = Attack, `D` = Decay, `R` = Release; `-50` to `+50`). All 3 stages record into User Patterns during Realtime Recording (`[REC]` + `[PLAY]`):
- **`ATTACK` (Note Onset Sharpness):** Ensure **`[FUNC]` is dark** and press **`[ENVELOPE]` so its LED is dark**. Rotate **`ENVELOPE / RELEASE`** **left** for a snappy percussive pluck, or **right** for a slow, bow/pad-like swell.
- **`DECAY` (Time to Fall to Sustain Level):** Ensure **`[FUNC]` is dark** and press **`[ENVELOPE]` so its LED is lit**. Rotate **`ENVELOPE / RELEASE`** **left** for a quicker drop after the attack, or **right** for a longer one. *(On sustaining leads such as `t01-15`, DECAY only changes how long the note takes to settle to its sustain level, so it can be subtle—audition it before building a pass around it.)*
- **`RELEASE` (Tail After Key Off):** Press **`[FUNC]` so its LED blinks**. Rotate **`ENVELOPE / RELEASE`** **left** for an instant gated stop when notes end, or **right** for a long, lingering ambient tail. *(Because `[FUNC]` blinking puts `LEVEL` on `CUTOFF/LEVEL` and `RELEASE` on `ENVELOPE/RELEASE`, you can perform volume fades and release-tail swells with both hands simultaneously!)*
- *Note:* The manual warns that for some Tones, adjusting the envelope times produces no audible difference, and that Tones with a sustain level of `0` (pianos, guitars) respond most to DECAY. Audition ATTACK, DECAY and RELEASE on your chosen Tone first (`[SHIFT] + [FUNC]` + turn the knob shows the exact value) and build your passes around the ones you can actually hear.

---

## 5. End-to-End Walkthrough (120 BPM): Recording `t01-15` (`Tri Lead 1`) + Permanently Saved Live `CUTOFF`, `LFO`, `ENVELOPE` & `LEVEL` Tweaks for a ~2-Minute Song (2 × 32 Bars)

**Goal:** Record single instrument **`t01-15`** (`Tri Lead 1`, Bank `01 Synthesizer`) in **`4/4`** at **`120.0` BPM**, perform **live `CUTOFF`, `RESONANCE`, `LFO` (`RATE` & `MOD`), `ENVELOPE` (`ATTACK`, `DECAY`, `RELEASE`), and `LEVEL` tweaks** across a full **~2 minutes (2 × 32 bars = `64` bars = `2:08` at 120 BPM)**, and have **every note, Tone, Tempo, and knob movement permanently saved** in **Song `S-1`** for hands-free playback.

> ### Why This 2-Pattern (`32 + 32 = 64` Bars) + 3-Pass `Loop Rest` Workflow Works on an MC-303 at 120 BPM
> - **Hardware Limit #1:** `SONG` mode only chains Patterns—it **cannot** record live knob movements. Knob automation (`Modify data`) must be recorded in **`PATTERN` mode**.
> - **Hardware Limit #2:** Max Pattern length is **`32` bars**. At `120.0` BPM in `4/4` (`2.0` sec/bar), one full pattern = `1:04`, so two User Patterns = **`64` bars = `2:08`**. Using the full `32` bars keeps every pattern boundary on an 8 × 4-bar phrase line (typical for dance music), and `U02` is a straight Pattern Copy of `U01`—no Delete Measure/trim step, which could also remove setup data.
> - **Hardware Trick (`Loop Rest = On` + 3-Pass Loop Layering):** Different knob parameters layer non-destructively across loop passes! Turning **`LoP = On`** inserts a **1-bar unrecorded buffer** after the final bar so you can relax and record in **3 unhurried passes** without ever touching `[STOP]` in between:
>   1. **Pass 1 (`[FUNC]` dark):** Filter **`CUTOFF`** & **`RESONANCE`**.
>   2. **Pass 2 (`[FUNC]` dark):** **`ENVELOPE` (`ATTACK` / `DECAY`)** & **`LFO` (`MOD` / `RATE`)**.
>   3. **Pass 3 (tap `[FUNC]` during the 1-bar buffer so `[FUNC]` blinks):** Volume **`LEVEL`** & **`ENVELOPE RELEASE`**.
>
> **Scaling to your full-length song (120 BPM):** repeat Phases 3–4 for `U03`, `U04`… and add them in Phase 5. Each `32`-bar pattern adds `1:04`; four patterns = `128` bars = `4:16`.

---

### Phase 1: Select Empty `u01`, Load `t01-15` (`Tri Lead 1`), Set LFO Routing & Set `120.0` BPM
1. Press **`[PLAY MODE]`** until the **`PATTERN`** LED is lit.
2. Make sure **`[PTN SET]`**, **`[RPS SET]`**, and **`[FUNC]`** LEDs are all **dark** (press any lit/blinking one to turn it off).
3. Press **`SELECT [<] / [>]`** until **`PTN/SONG`** is lit, then turn **`[VALUE]`** to **`u01`** (a lowercase `u` = empty; if an uppercase `U01` appears it still holds data or setup, so wipe it first using *Delete Entire User Pattern* in Section 4E).
4. Press **`[PART SELECT]`** so its LED is lit solid, then press **`PART [1]`**.
5. Press **`SELECT [<] / [>]`** until **`TONE`** is lit. Turn **`[VALUE]`** (hold `[SHIFT] + [VALUE]` to jump fast) until the display shows **`t01` `15`** (`Tri Lead 1`).
6. Tap **`[KEYBOARD PADS 1–16]`** (adjust `OCTAVE [-]` / `[+]` if desired) to audition `Tri Lead 1`.
7. **Enable LFO Destination Depths for `Tri Lead 1` (So the `LFO` Knob Works Live!):**
   - Hold **`[SHIFT] + Pad [9]`** (`LFO WAVE`) → turn **`[VALUE]`** to **`TRIANGLE`** (or `SINE`) → press **`[EXIT]`**.
   - Hold **`[SHIFT] + Pad [11]`** (`LFO FILTER`) → turn **`[VALUE]`** to **`65`** (enables filter-wah wobble) → press **`[EXIT]`**.
   - Hold **`[SHIFT] + Pad [10]`** (`LFO PITCH`) → turn **`[VALUE]`** to **`15`** (adds subtle pitch vibrato) → press **`[EXIT]`**.
   - Press **`[LFO]`** so its LED **lights** (`MOD`), turn **`LFO / PORTA TIME`** fully counter-clockwise (`0`) so the LFO starts clean/off until you bring it in live.
8. Press **`SELECT [<] / [>]`** until **`TEMPO`** is lit. Hold **`[SHIFT]`** and turn **`[VALUE]`** (1 BPM steps; without `[SHIFT]` it moves in 0.1 BPM steps) until the display reads **`120.0`**.
> *Tone, LFO depths and tempo now live in the edit buffer only. Don't switch patterns yet—they are written into the pattern in Phase 2, step 14 (after the notes, as in the manual's own worked example, and before the Pattern Copy in Phase 3).*

---

### Phase 2: Set Metronome, `4/4`, `32` Bars, `1`-Bar Lead-In, Record Notes in `U01` & Save Setup
9. **Check Metronome:** Hold **`[SHIFT] + Pad [16]`**, press **`SELECT [>]` 5 times** (`Mt 1`), turn **`[VALUE]`** to **`rEC`** (REC ONLY), and press **`[EXIT]`**. *(During recording, `[FUNC] + [SCALE/MEASURE]` also toggles the click on/off.)*
10. Press **`[REC]`** (`REC` LED blinks). Use **`SELECT [<] / [>]`** and **`[VALUE]`** to set all 4 recording parameters:
    - **`bEt`** (Beat): **`4/4`**
    - **`LGH`** (Pattern Length): **`32`** (`32` bars = `1:04` at `120.0` BPM)
    - **`Cnt`** (Count-In / Lead-In): **`1`** (`1`-bar / 4-click lead-in)
    - **`LoP`** (Loop Rest): **`On`** *(adds 1 unrecorded blank measure after Bar 32)*
11. Confirm **`PART [1]`** is lit, then press **`[PLAY]`**.
12. After the **4 metronome clicks**, play your `Tri Lead 1` melody/riff on **`[KEYBOARD PADS 1–16]`** across Bars `1–32` (`NEXT` shows the bar currently being recorded).
13. As soon as Bar `32` finishes and enters the **1-bar blank Loop Rest** (click only, no recording), press **`[STOP]`**.
    *(Hit a bad note? Re-press `[REC]` → `[PLAY]`, press `[SHIFT] + [TRANSPOSE/ERASE]` for `ErS`, hold that pad over the bad beat, exit `ErS`, and punch in the right note.)*
14. **Save Tone, LFO Routing & Tempo (`Pattern Setup Write`):** Hold **`[SHIFT] + [FUNC]`** and press **Keyboard Pad `[15]`** (`SUrE` appears), then press **`[ENTER]`**. *(Do it now: after the notes, before the Pattern Copy in Phase 3 so `U02` inherits the Tone/LFO/tempo, and before the knob passes in Phase 4—never after them.)*

---

### Phase 3: Copy `U01` → `U02` (Both `32` Bars: `32 + 32 = 64` Bars = `2:08`)
*(Want a different second-half melody? Skip this phase and repeat Steps 3–14 for `u02` with the same settings.)*

15. **Copy `U01` to `U02` (`Pattern Copy`):** With `U01` selected and stopped, hold **`[SHIFT] + [FUNC]`** and press **Keyboard Pad `[1]`**.
16. Turn **`[VALUE]`** to **`ALL`** (copies notes + Tone + LFO setup + tempo) → press **`[ENTER]`** → turn **`[VALUE]`** to **`U02`** → press **`[ENTER]`** (`SUrE`) → press **`[ENTER]`**.

---

### Phase 4: Permanently Record Live `CUTOFF`, `LFO`, `ENVELOPE` & `LEVEL` Tweaks into `U01` & `U02`

#### Part A — First Half (`U01`: Bars 1–32 | `0:00 – 1:04` Intro & Build)
17. Make sure **`PATTERN`** LED is lit (`[PLAY MODE]`). *(If pressing `[REC]` ever shows `SnG > CLr`, you are still in `SONG` mode—press `[EXIT]` and press `[PLAY MODE]` back to `PATTERN`!)*
18. Select **`U01`** (`SELECT` → `PTN/SONG` → `[VALUE]` to `U01`), press **`[PART SELECT]`** → **`PART [1]`**.
19. **Set & Save `U01`'s Starting Sound.** You do **not** need to change the `SELECT` indicator for this—leave it on `PTN/SONG` (showing `U01`). The knobs always act on the Part you selected in step 18 (`[PART SELECT]` lit, `PART [1]` lit), and the manual's knob procedures never use the `SELECT` buttons. Don't touch the `VALUE` dial here (with `PTN/SONG` lit it would change the pattern). `TONE` only had to be lit when you picked the Tone in Phase 1. The pattern is stopped, so nothing is being recorded—you are only setting where the sound starts.
    - **Reading the numbers (optional):** by default the display shows nothing when you turn a knob. To see the value, hold **`[SHIFT]` + `[FUNC]`** and turn the knob: `CURRENT` shows the parameter's name and `NEXT` shows its value (the manual's cutoff example reads `CUt` and a number). The number is that parameter's setting, in these ranges: `CUTOFF`, `RESONANCE`, `ATTACK`, `DECAY`, `RELEASE`, `LFO RATE`: `-50` to `+50`; `LFO MOD`, `LEVEL`, `PORTA TIME`: `0` to `127`; `PANPOT`: `L63` – `0` – `R63`. *(The manual only shows this for `CUTOFF`; how to read the `[FUNC]`-blinking functions such as `LEVEL` this way isn't shown—try it on your unit, or set them by ear.)*
    - With **`[FUNC]` dark** *(suggested start values—adjust by ear, they depend on the Tone)*:
      - **`CUTOFF / LEVEL`** knob = `CUTOFF`: about `-30` (dark/muffled intro).
      - **`[ENVELOPE]`** LED **dark** (`ATTACK`), **`ENVELOPE / RELEASE`** knob: about `+15` (soft, gentle attack).
      - **`[LFO]`** LED **lit** (`MOD`), **`LFO / PORTA TIME`** knob: `0` (no wobble yet).
    - Press **`[FUNC]`** (LED **blinks**):
      - **`CUTOFF / LEVEL`** knob = `LEVEL`: about `35` (quiet start for the fade-in); **`ENVELOPE / RELEASE`** knob = `RELEASE`: about `0`.
      - Press **`[FUNC]`** again so **`[FUNC]` is dark**.
    - Lock in these starting values with **Pattern Setup Write**: hold **`[SHIFT] + [FUNC]` + Pad `[15]`** (`SUrE`) → press **`[ENTER]`**.
20. **Record All `U01` Tweaks in One Continuous 3-Pass Loop:**
    - Press **`[REC]`** (verify `Cnt = 1`, `LGH = 32` and `LoP = On` with `SELECT [<] / [>]`), confirm **`PART [1]`** is lit, and press **`[PLAY]`**.
    - **Pass 1 — Filter (`[FUNC]` dark):** Across Bars `1–32`, slowly open **`CUTOFF / LEVEL`** clockwise from dark to bright, and add **`RESONANCE / PANPOT`** for bite as the build rises. *(Wait through the 1-bar blank `Loop Rest`—leave `[FUNC]` dark!)*
    - **Before Pass 2 (use the blank bar):** park the knobs you will touch first at their start positions—`ENVELOPE / RELEASE` where you want the intro `ATTACK`, and `LFO / PORTA TIME` at `0` with `[LFO]` lit. *(Hold `[SHIFT] + [FUNC]` while turning a knob to read its exact value.)*
    - **Pass 2 — Envelope & LFO (`[FUNC]` dark):**
      - **Envelope:** With **`[ENVELOPE]` dark** (`ATTACK`), turn **`ENVELOPE / RELEASE`** counter-clockwise over Bars `1–16` so the soft intro morphs into a snappy pluck; for Bars `17–32` you can tap **`[ENVELOPE]`** (**lit** = `DECAY`) and open **`ENVELOPE / RELEASE`** clockwise for fuller sustain *(DECAY can be subtle on this Tone—skip it if you can't hear it)*.
      - **LFO:** With **`[LFO]` lit** (`MOD`), turn **`LFO / PORTA TIME`** clockwise from Bar `17` onward to introduce filter-wah wobble; tap **`[LFO]`** (**dark** = `RATE`) for the last 8 bars (`25–32`) and sweep **`LFO / PORTA TIME`** clockwise to speed up the wobble into the peak!
    - **During the 1-Bar Blank `Loop Rest` After Pass 2:** Press **`[FUNC]`** so its LED **blinks**, and turn **`CUTOFF / LEVEL`** to about `35` *(Pass 1 left that pot wide open, and `LEVEL` takes on the pot's position as soon as you touch it)*.
    - **Pass 3 — Volume `LEVEL` & `RELEASE` (`[FUNC]` blinking):** Across Bars `1–32`, smoothly fade **`CUTOFF / LEVEL`** (`LEVEL`) up from ~`35` to `120` while nudging **`ENVELOPE / RELEASE`** (`RELEASE`) slightly clockwise for added space.
    - **During the 1-Bar Blank `Loop Rest` After Pass 3:** Press **`[STOP]`**, then press **`[FUNC]`** so its LED goes dark.
    *(Want to redo knob sweeps without losing notes? `[REC]` → `[PLAY]` → `[SHIFT] + [TRANSPOSE/ERASE]` [`ErS`] → hold **`[TAP]`**!)*

#### Part B — Second Half (`U02`: Bars 1–32 | `1:04 – 2:08` Peak & Ambient Fade-Out)
21. Select **`U02`** (`SELECT` → `PTN/SONG` → `[VALUE]` to `U02`), press **`[PART SELECT]`** → **`PART [1]`**.
22. **Set & Save `U02`'s Starting Sound (Matching End of `U01`):** *(Same method as step 19—knobs only, no `SELECT` change; hold `[SHIFT]` + `[FUNC]` and turn a knob to read its number.)*
    - With **`[FUNC]` dark**: set **`CUTOFF / LEVEL`** bright, **`ENVELOPE`** snappy (`ATTACK` left, `DECAY` open), and **`LFO MOD`** (`[LFO]` lit) moderately active.
    - Press **`[FUNC]`** (blinks): set **`CUTOFF / LEVEL`** (`LEVEL`) high (~`120`), press **`[FUNC]`** again (**dark**), and save setup: **`[SHIFT] + [FUNC] + Pad [15]`** → **`[ENTER]`**.
23. **Record All `U02` Peak & Outro Tweaks in One Continuous 3-Pass Loop:**
    - Press **`[REC]`** (verify `Cnt = 1`, `LGH = 32` and `LoP = On`), confirm **`PART [1]`** is lit, and press **`[PLAY]`**.
    - **Pass 1 — Filter (`[FUNC]` dark):** Work rhythmic **`CUTOFF`** & **`RESONANCE`** peaks through Bars `1–16`, then sweep **`CUTOFF / LEVEL`** counter-clockwise (closing the filter into warm darkness) down to Bar `32`. *(Wait through the 1-bar `Loop Rest` with `[FUNC]` dark.)*
    - **Before Pass 2 (use the blank bar):** park `LFO / PORTA TIME` and `ENVELOPE / RELEASE` at the values you want Pass 2 to start from (`[LFO]` lit = `MOD` at its moderate setting).
    - **Pass 2 — Envelope & LFO (`[FUNC]` dark):**
      - **Bars `1–16` (Peak):** Tap **`[LFO]`** (**dark** = `RATE`) to ride fast rhythmic LFO wobble speeds, and keep **`DECAY`** (`[ENVELOPE]` lit) punchy *(if you can hear it on this Tone)*.
      - **Bars `17–32` (Outro):** Tap **`[LFO]`** (**lit** = `MOD`) and roll **`LFO / PORTA TIME`** smoothly down toward `0`; tap **`[ENVELOPE]`** (**dark** = `ATTACK`) and turn **`ENVELOPE / RELEASE`** clockwise to soften the plucks back into gentle swells.
    - **During the 1-Bar Blank `Loop Rest` After Pass 2:** Press **`[FUNC]`** so its LED **blinks**, and turn **`CUTOFF / LEVEL`** fully clockwise (`127`) *(Pass 1 left that pot closed, so `LEVEL` would otherwise drop to silence the moment you touch it)*.
    - **Pass 3 — `LEVEL` Fade-Out & Ambient `RELEASE` Tail (`[FUNC]` blinking):** Hold **`CUTOFF / LEVEL`** (`LEVEL`) at `127` through Bar `16`, then across Bars `17–32` turn **`ENVELOPE / RELEASE`** (`RELEASE`) clockwise (creating a lush, lingering note tail) while smoothly fading **`CUTOFF / LEVEL`** (`LEVEL`) all the way down to **`0`** at Bar `32`.
    - **During the 1-Bar Blank `Loop Rest` After Pass 3:** Press **`[STOP]`**, then press **`[FUNC]`** so its LED is dark.
24. **Recommended Memory Cleanup (`Data Thin`):** Three passes of continuous Filter + LFO + Envelope + Level sweeps create a lot of controller data. Select `U01`, then run: **`[SHIFT] + [FUNC] + Pad [10]`** → **`PART [1]`** → `[VALUE]` to a thinning amount (`0–99`, higher = heavier thinning; start around **`15`** and audition afterwards) → **`[ENTER]`** (`SUrE`) → **`[ENTER]`**. Repeat for `U02`. *(It affects **all** Modify and Pitch Bend data in the selected Part, can't be limited to a range, and no undo is documented—run it only once you're happy with the sweeps. Check free memory first with **`[SHIFT] + Pad [16]`** → `SELECT [>]` ×8.)*

---

### Phase 5: Chain `U01 → U02` into Song `S-1` & Lock In `120.0` BPM
25. Press **`[PLAY MODE]`** until the **`SONG`** LED is lit.
26. Press **`SELECT [<] / [>]`** until **`PTN/SONG`** is lit, then turn **`[VALUE]`** to **`S-1`** and **check `NEXT`**:
    - **`---`** (display `S-1` ▸ `---`) = the song is empty → carry on to step 27.
    - **A pattern name** (e.g. `S-1` ▸ `b03`, the first pattern in the song) = the song already has steps. Clear it in one of two ways:
      - **Clear it as you start recording (simplest):** carry on to step 27. Pressing `[REC]` shows **`SnG` ▸ `CLr`**; press **`[ENTER]`** to erase every step in the song, or **`[EXIT]`** to cancel and pick a different song.
      - **Clear it now, without recording (Song Initialize):** with playback stopped and `S-1` selected, hold **`[SHIFT] + [FUNC]`** and press **Pad `[4]`** (Delete Pattern) → turn **`[VALUE]`** (or press `[FWD]`/`[BWD]`) to **`END`** → press **`[ENTER]`** (display shows `SU` ▸ `rE`, i.e. `SUrE`) → press **`[ENTER]`** again. `[EXIT]` cancels. *(`END` also deletes the song's saved setup data—its tempo and effects settings.)*
    - Clearing a song only removes its list of patterns; the patterns themselves (`U01`, `U02`…) are untouched.
27. Press **`[REC]`**. *(If `S-1` still has steps, the display shows **`SnG` ▸ `CLr`**—press **`[ENTER]`** to clear them, as in step 26.)* `STEP REC` lights: you are in song-recording standby.
28. Press **`[PLAY]`** (`CURRENT` shows step **`1`**).
29. Turn **`[VALUE]`** to **`U01`** → press **`[ENTER]`** (`CURRENT` advances to step **`2`**).
30. Turn **`[VALUE]`** to **`U02`** → press **`[ENTER]`** (`CURRENT` advances to step **`3`**). *(Wrong entry? Hold **`[SHIFT] + [BWD]`** to step back. For a longer song keep going—`U03`, `U04`… up to 999 steps.)*
31. Press **`[STOP]`** to finish recording Song steps (`32 + 32 = 64` bars = `2:08`).
32. **Save Master Song Tempo (`Song Setup Write`):** Press **`SELECT [<] / [>]`** to **`TEMPO`**, hold **`[SHIFT] + [VALUE]`** to set **`120.0`**, then hold **`[SHIFT] + [FUNC]` + press Pad `[15]`** (`SUrE`) → press **`[ENTER]`**. *(Stores the song's tempo plus its overall Delay/Reverb and Flanger/Chorus settings; once written, the song tempo overrides each pattern's own standard tempo.)*
33. **Hands-Free Playback Verification:**
    - Press **`[SHIFT] + [BWD]`** to jump to Step `1` of Song **`S-1`**, then press **`[PLAY]`**!
    - **Hands off the knobs!** *(If you move a knob past one of its switch points while a Part with recorded knob data plays, `REALTIME MODIFY` lights, the `PART` button blinks, and your knob overrides that Part's recorded data until you press the blinking `PART` button, return to the start of the pattern, or switch pattern.)*
    - Your entire **~2-minute (`2:08`) `t01-15` (`Tri Lead 1`) song** will play back with every note, `CUTOFF`/`RESONANCE` sweep, `LFO` wobble (`MOD` & `RATE`), `ENVELOPE` morph (`ATTACK`, `DECAY`, `RELEASE`), and `LEVEL` fade-in/fade-out permanently saved—even after powering the MC-303 off and back on (the memory is battery-backed).
    - **Songs store only pattern numbers:** if you later re-record or delete `U01`/`U02`, `S-1` changes with them (and a pattern with no data halts song playback). Back up finished work with Bulk Dump (Section 4F).

> **Next:** Section 6 adds a deep-house percussion part on Part R of these same two patterns—the Song you just chained will play it automatically.

---

## 6. Recording Part 2 (120 BPM): Deep-House Percussion on Part R, Building Across `U01` + `U02`

**Goal:** Add a deep-house drum-and-percussion bed on **Part R** (the Rhythm Part) of the same two 32-bar patterns from Section 5, with a **new element entering every 8 bars**: kick → open hat → clap → closed hat → shaker → congas → tambourine → ride. The `t01-15` lead on Part 1 keeps its notes and recorded knob sweeps untouched, and Song `S-1` (`U01 → U02`) plays the drums automatically because songs only store pattern numbers.

> **Style note:** the reference is *Hardrive – "Deep Inside"* (Louie Vega, Strictly Rhythm, 1993; databases list it at about 124 BPM). I couldn't verify how its drums are actually programmed, so the patterns below are generic deep-house building blocks in that spirit—**not a transcription**. This guide stays at **120 BPM**. As elsewhere in this file, nothing here has been run on a physical MC-303; check anything marked *(unconfirmed)*.

**Prerequisite:** Section 5 is finished: `U01` and `U02` hold the lead with its knob sweeps, and Song `S-1` plays `U01 → U02` at `120.0`.

### 6.1 The Build (Everything Already Playing Keeps Playing)

| Song bars | Pattern · bars | Clock (120 BPM) | New on Part R |
| :--- | :--- | :--- | :--- |
| 1–8 | `U01` · 1–8 | 0:00 | **Kick** (four-on-the-floor) |
| 9–16 | `U01` · 9–16 | 0:16 | **Open hat** (off-beat) |
| 17–24 | `U01` · 17–24 | 0:32 | **Clap** (beats 2 & 4) |
| 25–32 | `U01` · 25–32 | 0:48 | **Closed hat** (the 16ths between the other hits) |
| 33–40 | `U02` · 1–8 | 1:04 | **Shaker** (+ **crash** on bar 1, beat 1) |
| 41–48 | `U02` · 9–16 | 1:20 | **Congas** |
| 49–56 | `U02` · 17–24 | 1:36 | **Tambourine** (doubles the clap) |
| 57–64 | `U02` · 25–32 | 1:52 | **Ride** (doubles the open hat)—all eight layers while the lead fades out |

### 6.2 Cheat Card: Pad Map & Tap Grid (Rhythm Set `07` House)

| Drum (sound, note no.) | `OCTAVE` | Pad | Tap steps per bar | Velocity |
| :--- | :---: | :---: | :--- | :--- |
| **Kick** (909 BD 3, 36) | `-2` | `2` | `1 5 9 13` | Loud |
| **Clap** (909 Clap, 39) | `-2` | `5` | `5 13` | Loud |
| **Crash** (909 Crash 1, 49) | `-2` | `15` | `1`, once on `U02` bar 1 | Loud |
| **Open hat** (909 OH, 46) | `-2` | `12` | `3 7 11 15` | Soft |
| **Closed hat** (909 CH, 42) | `-2` | `8` | `2 4 6 8 10 12 14 16` | Soft |
| **Shaker** (626 Shaker, 82) | `+1` | `12` | `1 3 5 7 9 11 13 15` | Soft |
| **Lo conga** (Lo Conga Open, 64) | `0` | `6` | `4 11` | Soft |
| **Hi conga** (Hi Conga Open, 63) | `0` | `5` | `8 14` | Soft |
| **Tambourine** (Tambourine, 54) | `-1` | `8` | `5 13` | Soft |
| **Ride** (909 Ride, 51) | `-1` | `5` | `3 7 11 15` | Soft |

```text
Step       1 e & a 2 e & a 3 e & a 4 e & a
Kick       X . . . X . . . X . . . X . . .
Clap       . . . . X . . . . . . . X . . .
Open hat   . . X . . . X . . . X . . . X .
Closed hat . X . X . X . X . X . X . X . X
Shaker     X . X . X . X . X . X . X . X .
Lo conga   . . . X . . . . . . X . . . . .
Hi conga   . . . . . . . X . . . . . X . .
Tambourine . . . . X . . . . . . . X . . .
Ride       . . X . . . X . . . X . . . X .
```

- **Steps:** one bar = 16 steps, numbered `1–16` left to right and counted `1 e & a 2 e & a 3 e & a 4 e & a`. Step `1` = beat 1, `5` = beat 2, `9` = beat 3, `13` = beat 4; `X` = tap.
- **Pad → note:** `note = 58 + 12 × shift + pad` (manual p.20: pad 2 = C4 = note 60 at shift 0). The sounds come from the Rhythm Set list (manual pp.92–93).
- **Velocity:** Pad Velocity is one fixed value for every pad press (`1–127`, manual p.73), so the kit is recorded in two groups: **Loud ≈ `110`** and **Soft ≈ `80`**. Treat both as starting points and adjust by ear.

---

### Phase 6: Load Rhythm Set `07` (House) into Part R of `U01` & `U02` (Safe Pattern Setup Write)
> **Be careful here:** Pattern Setup Write stores **every Part's current settings at once**, including Part 1's knob positions. After Section 5 those are wherever your last knob pass or playback left them, and writing them now would make that the pattern's new *starting* sound. Selecting a pattern reloads its saved setup (manual p.21: unsaved part-parameter edits are lost when you select a different pattern), so **re-select the pattern first, then touch no knob and press no `[PLAY]` until the write is done.**

34. Press **`[STOP]`** if anything is playing, then press **`[PLAY MODE]`** until **`PATTERN`** is lit, and make sure **`[PTN SET]`**, **`[RPS SET]`** and **`[FUNC]`** are all dark.
35. Press **`SELECT [<] / [>]`** until **`PTN/SONG`** is lit. Turn **`[VALUE]`** to **`U02`**, then back to **`U01`** *(the hop forces `U01`'s saved setup to reload)*.
36. **Hands off the knobs; don't press `[PLAY]`.** Press **`[PART SELECT]`** (lit), then **`PART [R]`**.
37. Press **`SELECT [<] / [>]`** until **`TONE`** is lit. With Part R selected the display shows the **Rhythm Set**: `CURRENT` = `d` plus the set number, `NEXT` = a three-character set name (the manual's example is `d01` ▸ `909`). Turn **`[VALUE]`** to **`d07`** (Rhythm Set 07, **House**).
38. **Audition at `OCTAVE -2`:** press **`OCTAVE [-]`** until the display reads `OCt` ▸ `-2` (the `[-]` LED stays lit), then tap Pads **`2`** (kick), **`5`** (clap), **`8`** (closed hat), **`12`** (open hat) and **`15`** (crash). *(Hearing something else? Re-check `d07` and the octave against the cheat card.)*
39. Press **`SELECT [<] / [>]`** until **`TEMPO`** is lit and confirm it reads **`120.0`** *(re-selecting a pattern restores its stored tempo; if it's off, fix it as in Phase 1, step 8)*.
40. **Pattern Setup Write:** hold **`[SHIFT] + [FUNC]` + Pad `[15]`** (`SUrE`) → press **`[ENTER]`**.
41. **Repeat for `U02`:** `SELECT` → `PTN/SONG` → `[VALUE]` to **`U02`** *(changing pattern reloads `U02`'s saved setup, so no hop is needed)* → hands off the knobs → repeat steps 36–40 *(the octave is already `-2`)*.

---

### Phase 7: One-Time Prep — Quantize, `TIMING` Strength & Pad Velocity
42. **Aim Play Quantize at Part R only** *(so the lead and its knob data are never quantized)*: hold **`[SHIFT]`** and press **`[PART SELECT / QUANTIZE SELECT]`** (its LED **blinks**). The PART buttons now show which Parts Play Quantize applies to: make **only `PART [R]`** lit (press any other lit PART button to switch it off), then press **`[PART SELECT]`** so its LED lights steadily again. *(Unconfirmed: the manual doesn't say how to leave this mode; if the LED still blinks, press `[EXIT]`.)*
43. **Grid resolution:** with playback stopped, hold **`[SHIFT]`** and press Pad **`[2]`** (`rES` ▸ the current resolution). Turn **`[VALUE]`** to **`16`** (sixteenth notes; the options are `4`, `3-4`, `8`, `3-8`, `16`, `3.16`, `32`) → press **`[EXIT]`**. *(The manual's advice: set it to the shortest note value in the pattern.)*
44. **Strength:** with **`[FUNC]`** dark, turn the **`TIMING`** knob fully **clockwise** (100%: every hit snaps to the grid; at 0% quantize does nothing). *(With `[FUNC]` blinking this knob becomes `VELOCITY`—leave `[FUNC]` dark.)*
45. **Note your Pad Velocity** so you can restore it in step 53: hold **`[SHIFT]`** and press Pad **`[16]`** → press **`SELECT [>]` 7 times** (`PuL` ▸ the value; the manual's example shows `120`) → write the number down → press **`[EXIT]`**.
46. **Note your free memory:** hold **`[SHIFT]`** and press Pad **`[16]`** → press **`SELECT [>]` 8 times** (the Available Memory page shows the % remaining) → write it down → press **`[EXIT]`**. *(Check it again after Phase 9.)*

---

### Phase 8: Record the Seven Passes (Realtime Loop Mix, One Pass per Pad Position)
> **How it works:** each pass records into **one pattern** with **one octave shift and one Pad Velocity**, tapping one or two drums from their entry bar to the end of bar 32. Loop Mix **adds** each pass to what is already on Part R, so the groove builds up pass by pass, and `LoP = on` gives you the blank 33rd bar to press `[STOP]` in without clipping bar 32. *(Prefer one drum per pass? Split any row below—it works the same way.)*

47. **The pass routine**—repeat it for every row of the table in step 48:
    - **a. Pattern:** *(stopped, `PATTERN` mode)* `SELECT` → `PTN/SONG` → `[VALUE]` to the row's pattern *(this also resets `TEMPO` to its stored `120.0`)*.
    - **b. Part:** press **`[PART SELECT]`** (lit) → **`PART [R]`**.
    - **c. Octave:** press **`OCTAVE [-]` / `[+]`** until you reach the row's shift (neither LED lit = `0`; `[-]` lit = negative; `[+]` lit = positive; the display shows `OCt` ▸ the shift while you press). Tap the row's pads to confirm the sounds.
    - **d. Velocity:** only if the row's velocity differs from the previous pass: hold **`[SHIFT]`** + Pad `[16]` → `SELECT [>]` ×7 (`PuL`) → `[VALUE]` → `[EXIT]`.
    - **e. Standby:** press **`[REC]`** (blinks). With **`SELECT [<] / [>]`** check **`bEt`** `4-4`, **`LGH`** `32`, **`Cnt`** `1`, **`LoP`** `on`. Press **`PART [R]`** (the Recording Part), then **`[QUANTIZE]`** until the **GRID** indicator is lit. *(`SnG` ▸ `CLr` when you press `[REC]` means you are still in `SONG` mode—press `[EXIT]`, then `[PLAY MODE]` back to `PATTERN`.)*
    - **f. Record:** press **`[PLAY]`**. After the 4 count-in clicks, `NEXT` shows the bar being recorded (e.g. `6.3` = bar 6). Tap the row's hits from each drum's entry bar to the end of bar 32. **Hands off the knobs.**
    - **g. Stop:** after bar 32 comes the blank `Loop Rest` bar (nothing is recorded)—press **`[STOP]`** there.
    - **h. Listen:** press **`[PLAY]`** to hear it *(while recording, hits sound exactly as you play them; the quantized result is what you hear on the next loop)*, then **`[STOP]`**.
48. **The seven passes** (everything already on Part R keeps playing, so you tap along to the groove as it builds):

| # | Pattern | `OCTAVE` | Velocity | Tap this (pad · steps · bars) |
| :-: | :-: | :-: | :-: | :--- |
| 1 | `U01` | `-2` | `110` | **Kick** pad `2` · `1 5 9 13` · bars `1–32`<br>**Clap** pad `5` · `5 13` · bars `17–32` |
| 2 | `U02` | `-2` | `110` | **Crash** pad `15` · step `1` · bar `1` only (together with the first kick)<br>**Kick** pad `2` · `1 5 9 13` · bars `1–32`<br>**Clap** pad `5` · `5 13` · bars `1–32` |
| 3 | `U01` | `-2` | `80` | **Open hat** pad `12` · `3 7 11 15` · bars `9–32`<br>**Closed hat** pad `8` · `2 4 6 8 10 12 14 16` · bars `25–32` |
| 4 | `U02` | `-2` | `80` | **Open hat** pad `12` · `3 7 11 15` · bars `1–32`<br>**Closed hat** pad `8` · `2 4 6 8 10 12 14 16` · bars `1–32` |
| 5 | `U02` | `+1` | `80` | **Shaker** pad `12` · `1 3 5 7 9 11 13 15` · bars `1–32` |
| 6 | `U02` | `0` | `80` | **Lo conga** pad `6` · `4 11` · bars `9–32`<br>**Hi conga** pad `5` · `8 14` · bars `9–32` |
| 7 | `U02` | `-1` | `80` | **Tambourine** pad `8` · `5 13` · bars `17–32`<br>**Ride** pad `5` · `3 7 11 15` · bars `25–32` |

**Pass tips**
- **Entry bars:** watch `NEXT`—start the open hat when it reads bar `9`, the clap and tambourine at bar `17`, and the closed hat and ride at bar `25`.
- **Rehearse first:** press **`[REC]`** during a pass to enter rehearsal (`CURRENT` shows `rHS`): play along without recording, then press `[REC]` again to record (manual p.48).
- **Flubbed a hit?** Don't stop the pass. Fix it afterwards with **Realtime Erase** (Section 4E, *Single Note or Single Drum Sound*): `[REC]` → `PART [R]` → `[PLAY]` → `[SHIFT] + [TRANSPOSE/ERASE]` → hold *that drum's pad* over the bad bars only, `[STOP]`, then re-tap the missing hits in a new pass.
- **Struggling with the fast hats or shaker?** Before step (e), slow the tempo (`SELECT` → `TEMPO` → `[VALUE]` to about `100.0`). The manual (p.47) says tempo changes during recording aren't recorded, so the hits still play at 120 later. Re-select the pattern (or set `TEMPO` back to `120.0`) afterwards, and never run a Setup Write while the tempo is slowed.

---

### Phase 9: Check, Polish & Lock It In
49. **Listen to each pattern:** in `PATTERN` mode select `U01` and press **`[PLAY]`**: kick from bar 1, open hat from bar 9, clap from bar 17, closed hat from bar 25. Then `U02`: crash and shaker on bar 1, congas from bar 9, tambourine from bar 17, ride from bar 25. Press **`[STOP]`** after each.
50. **Optional—mute drum groups to hear each layer on its own:** press **`[RHYTHM MUTE]`** (lit). The PART buttons now mute rhythm groups, and a button that goes **dark** is muted (manual p.16):

| Button | Group | In this kit |
| :-: | :-: | :--- |
| `PART [R]` | BD | kick |
| `PART [2]` | HH | open + closed hat |
| `PART [3]` | CLP | clap |
| `PART [4]` | CYM | crash, ride, tambourine |
| `PART [5]` | TOM/PERC | congas, shaker |

Press **`[PART SELECT]`** to return. **Un-mute everything before any Setup Write**—mutes are stored with the setup.
51. **Optional—balance the drums against the lead:** if Part R is too loud or too quiet, repeat the safe routine from Phase 6 (steps 35–36: select another pattern and then the one you want, hands off the knobs, `PART [R]`), press **`[FUNC]`** so its LED **blinks**, turn **`CUTOFF / LEVEL`** (`LEVEL`) by ear *(it may jump to the knob's position as soon as you touch it—see the shared-pots note in Section 2)*, press **`[FUNC]`** again (dark), then run **Pattern Setup Write** (`[SHIFT] + [FUNC]` + Pad `[15]` → `[ENTER]`). Do it for both patterns.
52. **Optional—add swing (the deep-house bounce).** *Do this last: hits recorded afterwards would be straight.* For each pattern, on Part R only:
    1. Stopped, select the pattern. Hold **`[SHIFT]`** and press Pad **`[4]`** (`rES` ▸ `3-8` or `3.16`), turn **`[VALUE]`** to **`3.16`** (sixteenth-note triplets—the manual says to pick the shortest note value in the pattern), then press **`[EXIT]`**.
    2. Press **`[QUANTIZE]`** until the **SHUFFLE** indicator lights, then press **`[PLAY]`**. With **`[FUNC]`** dark, turn **`TIMING`** (Shuffle Rate): `50%` is straight and higher pushes the upbeats later. Start near **58%** for a light swing (about 66% is a full triplet shuffle; 100% drops the upbeat onto the next downbeat). Only the `e` and `a` 16ths (the even steps) move—beats and `&` hits stay put.
    3. Happy with the feel? Press **`[STOP]`**, leave **SHUFFLE** lit and **don't touch `TIMING` again**. Hold **`[SHIFT] + [FUNC]` + Pad `[11]`** (Edit Quantize) → make **`PART [R]`** the only lit PART button → **`[ENTER]`** (`SUrE`) → **`[ENTER]`**. The swing is now part of the notes, and Play Quantize switches itself off.
    4. Repeat for the other pattern with `TIMING` at the same position. *(Edit Quantize rewrites all of Part R in that pattern and no undo is documented—if you want a way back, first copy the pattern to a spare one with Pattern Copy `ALL`, Section 4F.)*
53. **Clean up:**
    - **Quantize off:** press **`[QUANTIZE]`** until none of GRID / GROOVE / SHUFFLE is lit.
    - **Octave back to `0`:** press `OCTAVE [-]` / `[+]` until neither LED is lit (otherwise Part 1's pads play in the wrong octave next time).
    - **Pad Velocity:** restore the value you noted in step 45 (hold **`[SHIFT]`** + Pad `[16]` → `SELECT [>]` ×7 → `[VALUE]` → `[EXIT]`).
    - **Mutes:** no PART button dark in the `[RHYTHM MUTE]` view; then press **`[PART SELECT]`**.
    - **Tempo:** re-select the pattern (or check `TEMPO` reads `120.0`).
54. **Hear it as a song:** press **`[PLAY MODE]`** until **`SONG`** is lit → `SELECT` → `PTN/SONG` → **`S-1`** → **`[SHIFT] + [BWD]`** → **`[PLAY]`**, hands off the knobs. You should hear the 64-bar (`2:08`) build: the lead's recorded sweeps plus a new drum element every 8 bars, with the crash and shaker landing as `U02` starts at bar 33.
55. **Check free memory again** (step 46) and **back up** with Bulk Dump (Section 4F) now that the arrangement is complete.

#### Quick Fixes

| Symptom | Fix |
| :--- | :--- |
| Pads play the wrong sounds | The Rhythm Set isn't `d07` (step 37) or the `OCTAVE` shift is wrong—compare with the cheat card. |
| Hits are loose or off the grid | Quantize wasn't on (GRID not lit) or `TIMING` was near 0%. Tighten all of Part R afterwards: steps 42–44, `[QUANTIZE]` to GRID, then Edit Quantize (step 52, sub-step 3). Do this *before* adding swing. |
| One drum is too loud or too quiet | Velocity is stored per hit: erase that drum (Realtime Erase, Section 4E) and re-record it in a pass at another Pad Velocity. For overall drum level see step 51. |
| The lead's starting sound changed after Phase 6 | A Setup Write happened after playback or knob moves. Re-set Part 1's starting values as in Section 5, steps 19 and 22, and write the setup again (the recorded knob sweeps themselves are not affected). |

> **Going past 64 bars:** for a 4-minute+ track, build `U03`/`U04` the same way (a new lead pattern per Section 5, drums per this section with the entry bars changed to suit—for example a breakdown that drops the kick), then append them to `S-1` (Section 5, Phase 5).
