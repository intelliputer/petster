# 8039-II-SBC work plan

## Objective

Build a small, externally programmed **8039** bench SBC that retains the
Petster's processor and external-ROM design paradigm. It uses one 28-pin ROM
socket for a 27C32, 27C128, or 27C256. This board is a bench fixture; it is
not connected to a Petster except through the separate 24-to-28-pin
daughterboard during controlled live tests.

## Electrical design contract

* `U1` is a socketed 40-pin 8039-compatible MCU. Configure `EA` for external
  program fetches according to the selected manufacturer's datasheet, then
  mark that fixed setting on the PCB.
* `U2` is a 5 V `74LS373` latch. `AD0`–`AD7` feed both the EPROM data bus and
  the latch inputs; `ALE` clocks the latch; its outputs drive `A0`–`A7`.
  `P2.0`–`P2.3` drive `A8`–`A11`; `/PSEN` drives ROM `/OE`; ROM `/CE` is low.
* `U3` is one 0.600-inch-wide 28-pin DIP or ZIF socket. A 27C32 is installed
  offset two positions toward the socket's high-numbered end: 27C32 pin 1 is
  in socket pin 3 and its pin 24 is in socket pin 28. Thus socket pins 1–2
  are deliberately empty. A 27C128/27C256 instead has pin 1 aligned with
  socket pin 1.
* `A12` and `A13` have three-pin, `GND — address — +5 V`, bank-select
  headers. `A14` has the same header for a 27C256. A dedicated `ROM TYPE`
  jumper routes socket pin 27 either to +5 V (`27C128`, `/PGM` read mode) or
  to `A14` (`27C256`). Do not fit a 27C256 until its exact manufacturer's
  pinout and read-mode requirements are checked.
* `J1` is the M6x09-II-SBC-compatible six-pin FTDI Friend header, marked
  `GND CTS VCC TXO RXI DTR`. `TXO` goes to `T0`; `P2.7` goes to `RXI`.
  `CTS` and `DTR` are left unconnected in Rev A. FTDI `VCC` reaches the
  board's +5 V rail only through a normally-open `USB POWER` jumper.
* Reset is active low: use a pull-up to +5 V, capacitor to ground, pushbutton
  to ground, and a discharge diode. It is not a pull-down circuit.
* Fit a 100 nF ceramic capacitor at every IC supply pair and bulk capacitance
  at the 5 V input. Include a 10 MHz crystal footprint with two load-capacitor
  footprints; fit only values suitable for the actual MCU.

## Bring-up order

1. Check every supply pin, ground pin, reset level, `EA`, and bank-select
   level with no ICs fitted.
2. Fit the LS373 and a confirmed 8039-compatible MCU. Use a 27C128 programmed
   with one small LED test image replicated into all four 4 KiB banks;
   validate reset, clock, `ALE`, `/PSEN`, and latch outputs with a logic
   analyser.
3. Fit the FTDI Friend without its VCC jumper. Prove the `T0` receive and
   `P2.7` transmit paths using the existing 9600-baud serial test program.
4. Test every 27C128 bank, then 27C256 `A14` selection. Verify that a 27C128
   never sees `/PGM` low in normal operation.
5. Only after standalone operation is repeatable, use the 27C128 in the
   separate Petster socket daughterboard for controlled live tests.

## Acceptance criteria before PCB layout

* KiCad ERC is clean after all components and the exact selected MCU/EPROM
  datasheets have been reviewed.
* The 27C32 offset outline and 27C128/27C256 normal outline are unambiguous
  on the PCB silkscreen.
* The USB power jumper is open by default; the board cannot be back-powered
  through the FTDI Friend header.
* Oscilloscope captures show a valid reset pulse and `ALE`/`/PSEN` activity.
