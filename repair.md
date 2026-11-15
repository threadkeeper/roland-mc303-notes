# Roland MC-303 Groovebox — Left SELECT, SHIFT & OCTAVE [+] Button Repair: Diagnose, Work Around & Replace the Tact Switches

The left **`SELECT [<]`** button stopped responding, and the **`[SHIFT]`** and **`OCTAVE [+]`** buttons are also faulty. All three use the same tact switch, so this note covers confirming the faults with the MC-303's built-in test mode, working around them in the meantime, and replacing all three switches (**`SW34`**, **`SW1`** and **`SW30`**) in one job, including a PiShop South Africa shopping list and beginner soldering tips.

> **Verification note:** The test-mode steps, button-test order, switch and diode names (`SW34`, `SW1`, `SW30`, `D33`, `D1`, `D28`), Roland part numbers, screw sizes and board layout are read from the scanned **Roland MC-303 Service Notes** (First Edition, May 1996, pp. 1–4, 7–13, 18–19). The `SELECT`, `OCTAVE`, pedal, sync and backup steps are from the **Owner's Manual** (pp. 14–17, 20, 71–72, 78, the "Repairs and Data" notice and the Topical Index). Switch specs are from **Panasonic's EVQ21305R page**, and the pin spacing was measured from the service notes' panel-board drawing. Shop details were checked on **2026-11-15**. Anything those documents don't describe is marked *(unconfirmed)*—check it on your MC-303.

---

## 1. Symptoms: Left SELECT, SHIFT and OCTAVE [+]

### 1.1 Left SELECT `[<]`

- **Symptom:** `SELECT [<]` does nothing; `SELECT [>]` still works.
- The two SELECT buttons move a lit indicator along a row of five LEDs, and the `VALUE` dial then edits whichever one is lit (manual pp. 14–15, 17). Left to right they are **`TEMPO`** · **`PTN SET`** · **`PTN/SONG`** · **`RPS SET`** · **`TONE`**; `[<]` moves the lit one left and `[>]` moves it right.
- **With `[<]` dead you can only move right.** From `PTN/SONG`, `[>]` reaches `RPS SET`, then `TONE`. `PTN SET` and `TEMPO` are to the *left*, so SELECT can't reach them (the manual's tempo figure shows the left button being pressed, p. 15), and you can't step back.
- *(Unconfirmed — the manual is silent)* Which indicator is lit at power-on, whether the row wraps around, and whether a power cycle returns it to `PTN/SONG`.

> **Check on your unit:** the manual's figures and the service notes' LED list put `PTN SET` to the *left* of `PTN/SONG`, so one `[>]` press from `PTN/SONG` should light `RPS SET`, not `PTN SET` (some write-ups claim otherwise). Press `[>]` once and see which LED lights. If your unit differs, trust the unit and correct this note.

### 1.2 `[SHIFT]`

- **Symptom:** `[SHIFT]` is unreliable.
- It is the modifier button. `[SHIFT] + Pad [1]–[16]` opens the parameter menus printed in black frames on the panel (the System settings are on `Pad [16]`), and `[SHIFT]` + `VALUE` changes values in bigger steps: the pattern number in tens, the tempo in whole BPM (manual, front-panel description and pp. 14–15). In test mode it also steps to the next test item, like `[ENTER]` (Service Notes p. 7).
- Until it's replaced, expect any `[SHIFT] + …` step in this note to need a few tries. Tap tempo and `[PTN SET]` + `OCTAVE [-]` don't use it.

### 1.3 `OCTAVE [+]`

- **Symptom:** `OCTAVE [+]` is faulty.
- It shifts the keyboard pads up one octave (the range is −4 to +4, and the `OCTAVE [+]` indicator lights; manual p. 20). With `[PTN SET]` or `[RPS SET]` lit, `OCTAVE [-] [+]` instead steps the Pattern Set or RPS Set number (manual p. 17 and the Topical Index).
- With `[+]` dead you can only step *down* with `OCTAVE [-]`: the pads can't go above the current octave, and the set number can't be raised.

---

## 2. Diagnosis: The Built-In Switch/LED Test

The MC-303 has a service test mode (Service Notes pp. 7–13). Its **Switch/LED Test** checks every panel button, including the left SELECT button (`SEL L`), `SHIFT` and `OCTAVE +`.

### Before you start

1. **Back up your data (recommended).** The manual warns that memory can be lost during repairs. Bulk Dump sends User Patterns, Songs, RPS Sets and Pattern Sets to a MIDI sequencer (p. 78): connect `MIDI OUT` → the sequencer's `MIDI IN`, stop playback, press **`[SHIFT] + [FUNC] + Pad [16]`**, start recording on the sequencer, press `[ENTER]`, and press `[ENTER]` again each time the transfer pauses. `[SHIFT]` is unreliable at the moment, so this and the battery check below may need a few tries.
2. **Optional battery check.** In normal mode hold **`[SHIFT] + [SCALE/MEASURE]`** and press **`PART [5 (TOM/PERC)]`**. The display shows `bAt` and the battery voltage (the service notes' example reads 3.0 V). A weak battery can lose all memory, so back up and have it replaced.
3. Plug in **headphones or a monitor speaker**: the test plays a note for each correct press.

### Steps

1. Switch the power **off**.
2. Hold **`[ARPEGGIO ON]` + `PART [R (BD)]`**, switch the power **on**, and keep both held until the display reads **`tSt ▶ tSt`**. The memory, battery and MIDI tests then start automatically (the MIDI test expects a cable looped from `MIDI OUT` to `MIDI IN`, which this repair doesn't need).
3. Jump to the switch test with **`[FUNC] + Pad [6]`**. `CURRENT` shows `t06` and **all LEDs should light** (if not, the notes say to check the main and panel boards).
4. Press the buttons one at a time in this order. Each correct press plays the next note of a scale and shows the button's number in `NEXT`. Buttons with several LEDs need several presses (`×4` etc.) to switch them all off:

   - `ARPEGGIO ON` → `PLAY QUANTIZE` ×4 → `EFFECT`
   - then `PORTAMENTO` → `LFO` → `ENVELOPE`
   - then `PART SELECT` → `PART MUTE` → `RHYTHM MUTE`
   - then `PART R`, `1`, `2`, `3`, `4`, `5`, `6`, `7`
   - then `SEL L` *(yours)* → `SEL R` ×5
   - then `BWD` → `FWD` → `REC` → `STOP` → `PLAY`
   - then `ENTER` → `EXIT` → `OCTAVE -`
   - then `OCTAVE +` *(also yours)*
   - then `TRANSPOSE` → `PTN SET` → `RPS SET`
   - then `PLAY MODE` ×3 → `SCALE` → `FUNC`
   - then `SHIFT` ×4 *(also yours)*
   - then `PAD 1–16` → `TAP`

5. **Result for the left SELECT button:** at `SEL L` nothing registers (no note and no new number in `NEXT`) while the buttons around it respond. Counting the sequence, `SEL L` is the 18th of 52 buttons. That points to the `[<]` switch (**`SW34`**) or its circuit, and replacing the switch is the cheapest first fix. (`Err` in `NEXT` is a different fault: the notes label it *Button Conflict NG* and say to check the main and panel boards, p. 10.)
6. **What to look for with SHIFT:** it is the 35th of 52 and takes four presses to switch off the four `SCALE 1`–`4` LEDs (p. 10). Needing more than four presses, or a `SCALE` LED left lit, means `[SHIFT]` (**`SW1`**) is probably missing presses.
7. **What to look for with OCTAVE +:** it is the 28th of 52, pressed once right after `OCTAVE -`. It should play the next note, show its number in `NEXT` and switch off its own indicator LED (`LED32`). If that LED stays lit and nothing registers, `[+]` (**`SW30`**) isn't being detected.
8. Switch the power **off** to leave test mode. (The test only moves on to the encoder test once every LED is off, so a stuck LED keeps it looping; that's expected.)

> **Don't step past the Sound Test.** `[ENTER]`/`[SHIFT]` move to the next test item, and the last item, **Factory Preset**, is described as "Load factory preset data" (p. 12). The notes say you leave test mode by executing Factory Preset *or* switching the power off, so switch off, and never press `[FUNC] + Pad [10]` unless you mean to reset. An unreliable `[SHIFT]` makes stepping with it unpredictable, so jump with `[FUNC] + Pad [n]` or just power off. *(The notes don't say exactly what it overwrites; assume your User Patterns and Songs.)*

---

## 3. Workarounds Until It's Fixed

> `[SHIFT]` is unreliable too, so the steps below that start with `[SHIFT] + Pad [16]` may need a few tries. Tap tempo and `[PTN SET]` + `OCTAVE [-]` don't use it, and a pedal that's already assigned works without it.

### 3.1 Change the tempo without `[<]`

The tempo is normally set with `SELECT [<]` → `TEMPO` → `VALUE` dial (manual p. 15). Three alternatives:

- **Tap tempo:** press **`[TAP / LOOP REST]`** at least **three** times at quarter-note intervals (p. 15). It works even when the tempo isn't on the display.
- **Pedal switch as TAP:** plug a pedal switch into the rear **`PEDAL SWITCH`** jack (Roland lists the DP-2 and FS-5U as options). With playback stopped, press **`[SHIFT] + Pad [16]`** → **`SELECT [>]` ×2** (display `PdL`) → turn `VALUE` until `NEXT` shows **`tAP`** → `[EXIT]`. The pedal now does what `[TAP]` does, and the setting survives power-off (p. 72). *(Another momentary footswitch should work if its polarity matches — unconfirmed.)*
- **External MIDI clock:** with playback stopped, press **`[SHIFT] + Pad [16]`** → **`SELECT [>]` ×3** → turn `VALUE` to **SLAVE** → `[EXIT]`, then send MIDI Clock to `MIDI IN`. In SLAVE mode with no clock arriving, `[PLAY]` does nothing, so set it back to INT afterwards (p. 72).

> The System display can't be opened while a pattern or song is playing. `[>]` only steps forward, so if you overshoot, press `[EXIT]` and re-enter with `[SHIFT] + Pad [16]`. The Topical Index counts the `[>]` presses from entry (Pedal Assign = 2, Sync Mode = 3).

### 3.2 Use a Pattern Set without `[<]`

The `PTN SET` position on the SELECT row can't be reached (it's left of `PTN/SONG`). Use the dedicated buttons instead: press **`[PTN SET]`** so its own indicator lights, pick the set (1–30) with **`OCTAVE [-]`**, then use the pads to pick patterns. **`[RPS SET]` + `OCTAVE [-]`** does the same for RPS sets (manual p. 17 and the Topical Index). With `OCTAVE [+]` faulty you can only step *down*, so count your presses; the manual doesn't say whether the number wraps from 1 to 30 *(unconfirmed)*.

### 3.3 What `[>]` still reaches

`PTN/SONG` → `RPS SET` → `TONE`, and every System setting (one step per press: Tuning, Song Loop, Pedal Assign, Sync Mode …).

### 3.4 Make a pedal act as `[SHIFT]`

The Pedal Assign setting in §3.1 also offers **SHIFT** (display `SFt`): the pedal then does what the `[SHIFT]` button does (manual p. 72). Set it the same way as the TAP option, but turn `VALUE` to `SFt` instead of `tAP`. A pedal has one assignment at a time, so you have to choose between SHIFT, TAP and the other options. Setting it needs `[SHIFT] + Pad [16]` once, which may take a few tries.

### 3.5 Play higher notes without `OCTAVE [+]`

Octave Shift only moves the pads, in one-octave steps from −4 to +4 (manual p. 20). `OCTAVE [-]` still shifts them down, but with `[+]` dead you can't step back up, so count your presses *(whether a power cycle resets the octave to 0 is unconfirmed)*. For notes above the pads' current range, play a connected MIDI keyboard: Octave Shift doesn't affect it (p. 20).

---

## 4. The Replacement Switch

### 4.1 The original part

- **Panasonic EVQ-21305R = Roland part `13169752`.** The service notes' parts list row reads `13169752 · EVQ 213 05R · TACT SWITCH · SW1,19-52 on PB` (p. 4; p. 2 gives the same pairing): every panel button except TAP and the 16 pads. The left SELECT button is **`SW34`** (labelled `< V/SEL` on the schematic, p. 19; the right one is `SW35`), **SHIFT is `SW1`** (labelled `SHIFT`) and **OCTAVE + is `SW30`** (labelled `OCTAVE +`), so all three need this same part.
- **TAP and the 16 pads use a different switch:** EVQ-QJJ05Q, Roland `00125590`, `SW2–18` (p. 4; p. 2 prints it as "05R"). Don't order it for the SELECT button.
- **Roland `13169697` is not the MC-303's part.** A community chart lists it as an Alps SKHVBD / Mitsumi SOR-123HS used on the D-5, JV-80/90, JV-880 and U-20 (same ~100 gf feel), but it doesn't appear in the MC-303 service notes. Use `13169752`.
- **Panasonic has discontinued the EVQ21305R**, so a generic equivalent (§4.3) is the practical option.

### 4.2 Specs to match (Panasonic EVQ21305R)

- **Body:** 6.0 mm × 6.0 mm and **5.00 mm** tall (Panasonic lists both overall and mounting height as 5.00 mm; 3.90 mm without the push plate).
- **Action:** top push, snap action, SPST momentary (normally open); about **1.0 N (≈100 gf)**, 0.25 mm travel; red push plate.
- **Mounting:** through-hole (DIP) with radial legs. **2 legs, about 5 mm apart:** the service notes' panel-board drawing (p. 18), measured at 600 dpi against a DIP IC's 2.54 mm pin pitch, puts the footprint's two solder holes ≈5.1 mm apart. *(Panasonic's page doesn't list pin count or pitch.)* `SW1` and `SW30` are drawn with the same footprint. Don't use 4-pin or surface-mount switches.
- **Electrical:** 10 µA 2 V DC to 20 mA 15 V DC (resistive load), 100,000 cycles. The panel board runs on +5 V logic (`D+5V` on `CN1`, p. 19), so the generic switch's 50 mA / 12 V rating is ample.

### 4.3 The generic stand-in

The PiShop switch (§5) lists approx. 6 × 6 × 5 mm, 50 mA, 12 V and 100,000 cycles, and its photo shows two straight legs and a round plunger. The page doesn't give leg spacing, operating force or how the 5 mm is measured *(unconfirmed)*, so **test-fit before soldering**:

- Legs about 5 mm apart (bend them slightly with needle-nose pliers if they're a little off).
- Body sits flat and square on the board.
- Plunger is level with a neighbouring original switch (`SW35` for `SW34`; `SW19`, the FUNC switch, for `SW1`; `SW29` or `SW31`, the OCTAVE `-` and TRANSPOSE switches, for `SW30`), so the key cap isn't held half-pressed.

The feel may differ slightly from the original.

---

## 5. Shopping List — PiShop South Africa

Prices include VAT and were checked on **2026-11-15**; stock changes.

1. **Replacement switches:** [Micro Tactile Push Button Switch 6x6x5mm 2p (5 pack)](https://www.pishop.co.za/store/micro-tactile-push-button-switch-6x6x5mm-2p-5-pack): **R9.90**, in stock. One pack covers the three repairs: one each for `SW34`, `SW1` and `SW30` plus two spares for any of the other 32 buttons that use this switch (not TAP or the pads). A third button has now failed, so a second pack is cheap insurance.
2. **Temperature-controlled iron:** [908S 80W Thermostatic Soldering Iron LCD with Adjustable Temperature (220V)](https://www.pishop.co.za/store/908s-80w-thermostatic-soldering-iron-lcd-with-adjustable-temperature-220v): **out of stock** when checked (180–500 °C, EU plug, 1.3 m lead). PiShop's other irons (40 W and 60 W) are fixed-wattage with no temperature control, so skip them: wait for a restock or buy an adjustable-temperature iron elsewhere.
3. **Solder and flux:** [Basic Soldering Wire and Rosin Paste Kit](https://www.pishop.co.za/store/basic-soldering-wire-and-rosin-paste-kit): **R219.90**, 1 in stock. 50 g of 0.6 mm **60/40 Sn/Pb (leaded)** solder, rosin paste, plus bonus wire and two mini screwdrivers.
4. **Desoldering braid:** [2.0mm 1.5m Desoldering Braided Solder Remover Wick](https://www.pishop.co.za/store/20mm-15m-desoldering-braided-solder-remover-wick): **R39.91**, in stock; pre-fluxed.
5. **Iron stand:** [Soldering Iron Stand with sponge](https://www.pishop.co.za/store/soldering-iron-stand-with-sponge): **R79.90**, in stock; arrives as loose parts to assemble, and the sponge must be wetted before use. This is the only iron holder on the list. The [CMT Gold Cleaning Wire](https://www.pishop.co.za/store/cmt-welding-soldering-solder-iron-tip-cleaner-gold-cleaning-wire-with-stand-3566) (**R59.90**, in stock) is a dry brass-wire tip-cleaner pot with no iron rest, so it's an optional extra, not a substitute.
6. **Work mat (optional):** [25x35cm Heat Resistant Soldering Station Pad](https://www.pishop.co.za/store/25x35cm-heat-resistant-soldering-station-pad): **R129.90**, **out of stock** (rated 350 °C). Any heat-resistant, non-conductive board works instead.

**Also needed (not from PiShop):** Phillips screwdrivers (#1 and #2; the service notes list 3 mm screws), needle-nose pliers or a small spanner for the `VALUE` encoder nut, isopropyl alcohol and cotton swabs, and flush cutters.

---

## 6. Beginner Soldering Rules & Safety

- **Practise first:** desolder and resolder a few joints on an old remote control or scrap board before touching the MC-303.
- **Set the iron to about 300–320 °C.** A fixed-wattage iron with no thermostat can run hot enough to lift copper pads. If the solder won't flow within about 2 s, nudge the temperature up rather than holding the tip on longer.
- **Add a little fresh solder to each old joint** before pressing the wick on it: fresh flux and solder carry heat across faster and pull the old solder out cleanly.
- **3–4 second rule:** never keep the tip on one pad for more than about 3–4 s at a time, and let it cool for a few seconds before trying again. Use about 2 s per leg when soldering the new switch. *(General guidance: neither the PiShop listing nor Panasonic's page gives a soldering limit.)*
- **Keep alcohol off the plastic.** Use isopropyl alcohol only on the bare PCB; the manual warns that alcohol and solvents can discolour or deform the unit's finish ("Maintenance").
- **Static and shorts:** the boards carry CMOS chips, so touch bare metal before handling them and lay them on a non-conductive surface, clear of loose screws and offcuts. The unit runs from a 9 V DC adaptor (Service Notes p. 1), so there is no mains inside, but unplug it anyway.
- **Stay safe:** ventilate the room, rest the hot iron in its stand, and wash your hands after handling leaded solder.

---

## 7. Replacement: Step by Step

### Phase 1: Disassembly

1. **Disconnect everything.** Finish the backup (§2) first, then unplug the adaptor and every audio, MIDI and pedal cable.
2. **Remove the knobs.** Pull the control knobs and the large `VALUE` dial straight up off their shafts and keep them in a container.
3. **Open the chassis.** Lay the unit face-down on a soft towel, remove the screws holding the bottom cover (the service notes show 3 × 6 mm screws) and lift the cover off.
4. **Free the main board.** Photograph every ribbon cable and connector, unplug the connectors joining the main board to the panel board, remove the main board's screws and set it aside on a non-conductive surface. Leave the backup battery alone.
5. **Remove the panel board.** Take the nut and washer off the `VALUE` encoder shaft, undo the panel board's screws and lift it straight off (it has four connectors, `CN1`–`CN4`).
   - **Caution:** keep the faceplate lying flat (face-down) so the loose button caps stay in place and don't get lost.

### Phase 2: Desolder & Solder

1. **Find all three switches.** On the component side (the side facing the faceplate): **`SW34`** is the left of the two switches just below the five SELECT LEDs, with diodes `D33` and `D34` between it and `SW35`. **`SW1`** is in the bottom-left corner: the lowest of the three buttons stacked along the left edge (`SW20` SCALE/MEASURE, `SW19` FUNC, `SW1` SHIFT), with diode `D1` just above it. **`SW30`** is the middle of the three buttons in the row above `PTN SET`/`RPS SET`/`PLAY MODE` (`SW29` OCTAVE `-`, `SW30` OCTAVE `+`, `SW31` TRANSPOSE), with diode `D28` just to its right. Its indicator LED (`LED32`) is mounted directly above it: the LED is the round part, the tact switch is the square one. Left and right swap when you flip the board, so photograph both sides and match them up before you start. Each switch's two legs are its two joints; ignore any empty holes around them and the nearby LED and diode pins.
2. **Desolder the legs** of `SW34` first. Add a touch of fresh solder, lay the wick over one leg and press the iron on the wick for 3–4 s until the solder wicks into the braid. Repeat for the other leg, letting the pad cool between attempts.
3. **Remove the old switch and clean.** Gently pull the switch out from the component side. If it resists, a leg still has solder, so re-wick it (don't force it: pads lift). Clean flux from the area with isopropyl alcohol and a cotton swab, and check that both pads and holes are intact and clear.
4. **Test-fit the new switch** (§4.3). Its two legs go through from the component side. The switch isn't polarised, so either way round works.
5. **Solder the new joints.** Touch the iron to the leg and pad together for about 2 s, feed in a little solder until it forms a shiny cone, then remove the iron. Trim the legs and check there is no solder bridge to neighbouring pads or the nearby diode (`D33`, `D1` or `D28`).
6. **Repeat steps 2–5 for `SW1`** (SHIFT) and then `SW30` (OCTAVE `+`), one switch at a time. For `SW30`, heat only the tact switch's two legs and keep the iron off the LED's legs (`LED32`) just above it.

### Phase 3: Test & Reassemble

1. **Partial reassembly for testing.** Refit the panel board into the faceplate (screws, `VALUE` nut and washer) so the button caps work, reconnect the cables using your photos, and lay the main board beside it on a non-conductive surface with the bottom cover still off. Connect headphones and the adaptor.
2. **Quick check (normal mode).** Power on and press `SELECT [<]`: the lit indicator should step one position left on each press (for example `PTN/SONG` → `PTN SET` → `TEMPO`), and `VALUE` should then change the tempo. Then hold `[SHIFT]` and turn `VALUE`: values should move in bigger steps (the pattern number in tens, the tempo in whole BPM; manual pp. 14–15). `[SHIFT] + Pad [16]` with playback stopped should open the System display (`[EXIT]` leaves it). With `[PTN SET]` and `[RPS SET]` dark, press `OCTAVE [+]`: its indicator should light (the display shows the octave value while you hold the button); press `OCTAVE [-]` once to return to 0 (manual p. 20).
3. **Full check.** Repeat the §2 Switch/LED test (power on holding `[ARPEGGIO ON]` + `PART [R (BD)]`, then `[FUNC] + Pad [6]`) and confirm that `SEL L` now plays a note and shows its number, that four presses of `SHIFT` switch off the four `SCALE` LEDs, and that `OCTAVE +` plays a note and switches off its LED. Then power off; don't continue past the Sound Test.
4. **Close it up.** Power off and unplug, then screw the main board down, refit the bottom cover and press the knobs back on.
   - Most of the screws are listed in the service notes as 3 mm "Binding Head B tight" types (thread-forming, so they bite into plastic): start them gently in their existing threads and don't over-tighten.

---

## 8. If It Still Doesn't Work

- Re-check every new joint for cold joints, solder bridges or a lifted pad or trace.
- `SW34`, `SW1` and `SW30` are each wired in series with a matrix diode (`D33`, `D1` and `D28`, all MA165; schematic, p. 19): check the diode and joints of whichever switch still misbehaves.
- `Err` in the switch test is labelled *Button Conflict NG* in the notes: look for a short or a stuck switch around the new joints.
- If a key cap sticks or a button feels dead, compare the new plunger's height with its neighbour (`SW35`; `SW19` for `SW1`; `SW29` or `SW31` for `SW30`): a taller switch holds the cap half-pressed, and a shorter one may not be reached.

---

## Sources

- [Roland MC-303 Service Notes, First Edition, May 1996 (SynthXL PDF)](https://www.synthxl.com/wp-content/uploads/2018/02/Roland-MC-303-Service-note.pdf): exploded view (p. 3), parts list (pp. 2, 4), test mode (pp. 7–13), panel board layout and schematic (pp. 18–19)
- [Roland MC-303 Owner's Manual (Internet Archive)](https://archive.org/details/synthmanual-roland-mc-303-owners-manual): SELECT indicators, SHIFT, Octave Shift, TAP, Pattern Sets, System settings, Bulk Dump, "Repairs and Data", "Maintenance"
- [Panasonic EVQ21305R product page (discontinued)](https://industry.panasonic.com/ap/en/products/control/switch/light-touch/number/evq21305r)
- [Roland tact switch reference chart (llamamusic.com)](https://llamamusic.com/super-jx/tact_switches.html): community cross-reference of Roland part numbers
- PiShop South Africa product pages linked in §5
