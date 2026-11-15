# Next Steps

**The core MC-303 features the notes don't cover yet, one short walkthrough each**

[record_cheat.md](./record_cheat.md) and [jonty_first_track.md](./jonty_first_track.md) take you from an empty machine to a finished five-pattern track. These five features are the biggest gaps left, in the order I'd learn them. Each one is button-by-button like the rest of the repo and uses the track as its example. Written to be read on a phone.

> **Verification note:** The procedures are from the 1996 Owner's Manual (pp.14–19, 30–35, 38–41, 48, 65–66, 69–72); nothing here has been run on a physical MC-303. Pads the scan makes hard to read are marked *(inferred)*. Almost every step uses `[SHIFT]`, so until your switch is replaced put it on a pedal ([repair.md](./repair.md) §3.4).

**Jump to:** [Arpeggiator](#1-the-arpeggiator) · [Effects](#2-effects) · [Fix a take](#3-fix-things-without-re-recording) · [Edit the Song](#4-edit-the-song) · [Perform live](#5-perform-it-live)

---

## 1. The Arpeggiator

Hold a chord and the MC-303 plays it as an arpeggio, in time with the pattern. You can record that straight into a Part, so the break in `U43` gets a moving line you never have to tap. *(Manual pp.38–41, 48.)*

1. Press **`[STOP]`**, then **`[PLAY MODE]`** until **`PATTERN`** is lit, and select the pattern (for example `U43`). **`[PTN SET]` and `[RPS SET]` must be dark**, or the pads select patterns instead of playing notes.
2. Press **`[PART SELECT]`** (lit) → a free Part (the track leaves `PART [4]` empty) → `SELECT [>]` until `TONE` is lit → **`[VALUE]`** to a Tone with a clear attack (a pluck or e-piano works best).
3. Press **`[ARPEGGIO ON]`** so its indicator lights.
4. **Hold a chord on the pads.** The Part now plays it as an arpeggio. At `OCTAVE 0`, pads `1 · 4 · 8` are B3 · D4 · F#4, a B minor chord (the track's key).
5. **Pick the style**, the biggest choice (34 of them, for example `1/16`, `1/8`, `SYN BASS`, `PIANO BACKING`): hold **`[SHIFT]`** and press Pad **`[1]`** → turn **`[VALUE]`** → **`[EXIT]`**. Shortcut: while you hold `[ARPEGGIO ON]` the style shows on the display and `[VALUE]` changes it, which is handy live.
6. **Shape it** with the **`ACCENT RATE / OCTAVE RANGE`** knob. With `[FUNC]` dark it sets Accent Rate (`0`–`100`; right = a more intense groove). Press `[FUNC]` so it blinks and it sets Octave Range (`-3` to `+3`; right plays upward from your chord, left downward, `0` only the notes you hold). Press `[FUNC]` again to go dark. Hold `[SHIFT] + [FUNC]` while turning to read the number.
7. **Go deeper (optional):** hold `[SHIFT]` and press Pad `[1]`, then press `SELECT [>]` once for **Motif** (the order the notes sound), twice for **Beat Pattern**, three times for **Shuffle Rate** (`50`–`90`%) → `[VALUE]` → `[EXIT]`. Choosing a style sets all four to suit it, so choose the style first.
8. **Record it** with `[ARPEGGIO ON]` lit, as in record_cheat.md Section 4B: **`[REC]`** (standby; check `bEt`, `LGH`, `Cnt`, `LoP`) → the Part → **`[PLAY]`**. After the count-in, play your chord at the moment recording starts and change chords at the bar lines. With `Cnt` set to `Wait Note`, recording and the arpeggio both start on your first pad press. Press **`[STOP]`** in the blank `Loop Rest` bar.
9. **Switch the arpeggiator off** (`[ARPEGGIO ON]` dark) so the pads play single notes again, then save the Part's Tone with Pattern Setup Write (the safe routine, record_cheat.md Phase 6).

> **Good to know:** the arpeggio settings (style, accent and so on) are not stored in the pattern. They can be stored in a Pattern Set (step 24). A pedal set to `HOLD` keeps an arpeggio going after you let go, but a pedal has one job at a time, and repair.md §3.4 uses it as SHIFT.

---

## 2. Effects

There are two effect units: **Delay/Reverb** and **Flanger/Chorus**. Each has a type, a time or rate, an overall level, and a level per Part. Reverb and delay add space; chorus adds width. *(Manual pp.30–35, 69.)*

**How the controls work:** `[EFFECT]` decides which unit the `TIME/RATE` and `EFX LEVEL` knob controls (**indicator dark = Delay/Reverb, lit = Flanger/Chorus**). With `[FUNC]` dark the knob is `TIME/RATE`; with `[FUNC]` blinking it is `EFX LEVEL`. *(Inferred: this follows the `[FUNC]` rule of the other dual-label knobs.)*

10. **Reverb or delay type:** hold **`[SHIFT]`** and press Pad **`[5]`** → turn **`[VALUE]`**: `Room 1–3`, `Hall 1–2`, `Plate`, `Delay` or `Panning Delay` → **`[EXIT]`**. *(By ear: `Hall 1` or `Plate` for a house bed, `Delay` for the free-style.)* Changing the type resets the other settings to suit it, so set the type first.
11. **Time:** press `[EFFECT]` until its indicator is **dark**, make sure `[FUNC]` is dark, and turn the knob (`0`–`127`; right = longer).
12. **Overall level:** `[EFFECT]` dark, press `[FUNC]` so it **blinks**, and turn the knob (`0`–`127`). Press `[FUNC]` again to go dark. At `0` there is no effect at all, whatever the Part levels are.
13. **Level per Part:** hold `[SHIFT]` and press Pad **`[6]`** → press a PART button (or use `SELECT [<]` / `[>]`) → turn `[VALUE]` (`0`–`127`) → next Part → `[EXIT]`. *(By ear: most on Part 2, a little on Part 1, none on the bass and kick.)*
14. **Chorus type:** hold `[SHIFT]` and press Pad **`[7]`** → `[VALUE]`: `Chorus 1–4`, `Feedback Chorus`, `Flanger`, `Short Delay` or `Short Delay (FB)` → `[EXIT]`.
15. **Chorus rate, level and Part levels:** press `[EFFECT]` so it **lights**. `[FUNC]` dark + the knob = rate; `[FUNC]` blinking + the knob = level. For Part levels hold `[SHIFT]` and press Pad **`[8]`** → Part → `[VALUE]` → `[EXIT]`.
16. **Save it.** Part levels belong to each pattern: run Pattern Setup Write (the safe routine) in every pattern, and keep the Part levels similar from pattern to pattern, or the effect jumps at every pattern change. The overall **type, time/rate and level** are stored in the **Song**: set them, then run Song Setup Write (hold **`[SHIFT] + [FUNC]`** and press Pad **`[15]`** → **`[ENTER]`**, as in jonty_first_track.md step 27).

---

## 3. Fix Things Without Re-Recording

Four edits change what you have already recorded, so you don't have to play it again. They act on the **whole Part** (Transpose can be limited to a range). *(Manual pp.65–66.)*

17. Select the pattern (stopped, `PATTERN` mode), then hold **`[SHIFT] + [FUNC]`** and press the pad for the edit below.
18. Press the **PART button(s)** to edit (two or more can be lit), turn **`[VALUE]`** to the amount, press **`[ENTER]`** (execute display) and **`[ENTER]`** again. `[EXIT]` cancels. No undo is documented, so copy the pattern first if you are unsure (record_cheat.md, Section 7).

The four edits:

- **Transpose** · Pad `[6]` *(inferred)*: `-24` to `+24` semitones. To move only some notes, press two pads first: everything between them is transposed. *Example: record the bass at `OCTAVE 0` with the hook, then transpose Part 3 by `-24`. That is two octaves down with no `OCTAVE [-]` presses, and it avoids the dead `[+]` in jonty_first_track.md.*
- **Change Velocity** · Pad `[7]`: adds `-99` to `+99` to every hit (limited to `1`–`127`). *Example: Part 1 is too loud in `U41`, so use `-15`.*
- **Change Gate Time** · Pad `[8]`: adds to (or takes from) the length of every note. Shorter is more staccato, longer is more tenuto.
- **Shift Clock** · Pad `[9]` *(inferred)*: moves the Part's timing by `-99` to `+99` clocks (negative = earlier, positive = later; 24 clocks = one 16th note). A few clocks lays a part back. Data shifted past the start is deleted.

---

## 4. Edit the Song

Change a Song without recording it again. A Song holds up to 999 steps. *(Manual pp.71–72.)*

19. **Insert a pattern:** press `[PLAY MODE]` until **`SONG`** is lit and select the Song (`S-2`). Hold **`[SHIFT] + [FUNC]`** and press Pad **`[5]`** (Insert Pattern) → turn **`[VALUE]`** (or use `[FWD]` / `[BWD]`) to the position (`1`–`998`, or `END` to append) → **`[ENTER]`** → **`[VALUE]`** to the pattern → **`[ENTER]`** → **`[ENTER]`** again. *Example: insert `U44` at position `5` of `S-2` to repeat the peak.*
20. **Delete a step:** record_cheat.md Section 4E (*Delete 1 Step*): `[SHIFT] + [FUNC]` + Pad `[4]` → the step → `[ENTER]` → `[ENTER]`. The steps after it move up to close the gap.
21. **Loop the Song** (to practise against it, or to leave it playing): stopped, hold **`[SHIFT]`** and press Pad **`[16]`** → press **`SELECT [>]`** once *(inferred from the order of the System pages)* → **`[VALUE]`**: `OFF` (play once), `LOOP 1` (repeat this Song) or `LOOP 2` (all Songs in turn) → **`[EXIT]`**. It is kept when the power is off.

---

## 5. Perform It Live

Everything so far builds the track; these play it. *(Manual pp.14–19.)*

22. **Queue the next pattern:** while a pattern plays, turn **`[VALUE]`**. `NEXT` shows the pattern that starts when this one finishes. When the change point is near `NEXT` blinks and you can't change it. `[STOP]` cancels the queue.
23. **Put patterns on pads (a Pattern Set):** use `SELECT` to light `PTN SET` (`NEXT` shows the set number), press **`[PTN SET]`** so its own indicator lights, and turn **`[VALUE]`** to pick a set (`1`–`30`). While `[PTN SET]` is lit, `OCTAVE [-]` / `[+]` also pick the set. *(`PTN SET` is left of `PTN/SONG`, so with `SELECT [<]` dead use `[PTN SET]` + `OCTAVE [-]`, repair.md §3.2.)* Select a pattern (`U41`), then **hold `[PTN SET]` and press a pad**: `U41` is now on that pad. Repeat for `U42` → pad `2` through `U45` → pad `5`. You can do this during playback.
24. **Play them:** with `[PTN SET]` lit, press a pad to select its pattern, even while another is playing. Press `[PTN SET]` again (dark) before you play notes. **Arpeggio settings can live in the set:** set up an arpeggio (section 1), then hold `[SHIFT] + [FUNC]` and press Pad **`[14]`** → **`[ENTER]`** (the on/off state isn't stored).
25. **Change key live (Realtime Transpose):** press **`[TRANSPOSE]`** (lit) and playback is transposed at once. Hold `[TRANSPOSE]` and turn `[VALUE]` to set the amount (`-24` to `+24` semitones; the factory setting is `+4`). Press `[TRANSPOSE]` again to return. It resets to off at power-on. *Example: lift the last groove by 2 semitones.*
26. **Save a mute mix as its own pattern (a Variation Pattern):** select the pattern (`U44`), mute the Parts and drums you want gone (for example `PART [3]` and the kick group, record_cheat.md step 50), then hold `[SHIFT] + [FUNC]` and press Pad **`[13]`** → `[VALUE]` to a free slot (`L01`–`Q50`) → **`[ENTER]`** → **`[ENTER]`**. It stores only the mutes, so it uses almost no memory, and it follows any change to the original (delete the original and the variation can't play). You can chain it in a Song like any pattern (step 19).
27. **Starting from the middle?** After jumping with `[FWD]` / `[BWD]`, the volume or pitch can be wrong because the skipped MIDI messages were never sent. With playback stopped, hold **`[SHIFT]`** and press **`[STOP]`** (MIDI Update) before you press `[PLAY]`.

---

## Left Out on Purpose

These matter less for this track: Groove Quantize templates, playing RPS phrases, Portamento, Song Copy, MIDI sync beyond [repair.md](./repair.md) §3.1, and the MS-1 sampler. They are all in the [Owner's Manual](https://archive.org/details/synthmanual-roland-mc-303-owners-manual).
