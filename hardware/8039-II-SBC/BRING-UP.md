# 8039-II SBC bring-up checklist

Use this procedure when the fabricated board arrives.  It assumes a fully
assembled board with socketed ICs, a regulated 5 V source, an EPROM programmed
with a known-good test image, and a multimeter.  A current-limited bench supply
and an oscilloscope or logic analyser are strongly recommended.

The released design passed KiCad ERC and PCB DRC with zero errors, warnings,
violations, and unconnected pads.  This checklist is still required: it verifies
assembly, component orientation, the selected power source, and the first
firmware execution on the physical board.

## 1. Assemble and inspect

1. Check the PCB for damaged traces, solder bridges, missing plating, and
   incorrect connector or socket orientation.
2. Fit all passive components, headers, sockets, and the reset switch before
   fitting U1, U2, or U3.
3. Confirm polarized parts:
   - C1 positive pad is the `RESET` node; its negative pad is GND.
   - D1's marked cathode end (`K`, pad 1) is connected to +5 V.
4. With power removed, measure between +5 V and GND.  It must not read as a
   near-short.  Also check the four mounting holes remain isolated from copper
   if metal screws or standoffs will be used.

## 2. Select safe initial jumper settings

For the first external-ROM 8039 test:

| Jumper | Initial setting | Purpose |
| --- | --- | --- |
| JP5 EA | EA to +5 V | Selects external program ROM for an 8039. |
| JP6 power | 1-2 for FTDI VCC **or** 2-3 for J2 pin 18 | Select exactly one 5 V source. |
| JP1 A12 / JP2 A13 | Both to GND | Selects ROM bank 0. |
| JP3 A14/PGM / JP4 A15/VPP | Both to +5 V with a 27C128 | Correct normal read-mode levels for the initial 27C128 test. |

Do not fit more than one JP6 shunt.  When using the FTDI position, verify that
the FTDI adapter actually supplies **5 V**, not 3.3 V.  When using J2 pin 18,
apply only regulated 5 V.  Change ROM bank or EA jumpers only with power removed
or while U1 is held in reset.

An 8048 may be tested with EA tied to GND for its internal ROM.  Do not expect
the external EPROM image to run in that configuration.  A 27C256 uses JP3 and
JP4 as A14/A15 selectors; confirm the intended bank settings before fitting it.

## 3. Power-only test (no ICs fitted)

1. Fit the selected JP6 shunt and apply 5 V through the selected source.
2. Start with the bench supply current limit set low (for example 50 mA), then
   raise it only after the rail is stable and there is no unexpected heating.
3. Measure +5 V relative to GND at the empty sockets:
   - U1 pins 26 and 40
   - U2 pin 20
   - U3 pin 28
4. Confirm the corresponding ground pins are at ground: U1.20, U2.10, and
   U3.14.  Remove power before fitting any ICs.

## 4. Reset and clock checks

1. Fit U1 only.  On power-up, U1 pin 4 (`~RESET`) should initially be low and
   then rise toward +5 V as C1 charges through R1.  Its nominal RC time constant
   is 100 ms (100 kOhm x 1 uF).
2. Press SW1: U1.4 must go low while pressed and return high when released.
3. Verify oscillator activity at U1 pins 2 and 3 using a high-impedance probe.
   Avoid a x1 probe, which can disturb the oscillator.
4. If reset never rises, remove power and recheck C1 polarity, D1 orientation,
   and the R1/C1/SW1 connections before proceeding.

## 5. First firmware execution

1. Remove power.  Fit U2 and a verified, correctly oriented EPROM in U3.
2. Reconfirm JP5 is set for external ROM and JP1/JP2 select the programmed
   4 KiB image bank.
3. Power the board with current limiting enabled.  Check that no IC becomes hot.
4. Use a minimal diagnostic image that repeatedly toggles one available GPIO
   line.  Observe it at J2 with a scope, logic analyser, or suitable external
   LED-and-resistor fixture.
5. Confirm `ALE` (U1.11) and `~PSEN` (U1.9) show program-fetch activity.  A
   static reset line, absent clock, or no fetch activity should be debugged
   before connecting any external hardware.

## 6. Interface checkout and acceptance

1. Verify the FTDI console with a known baud rate and a simple transmit test.
2. Test the required J2 GPIO lines one at a time with the diagnostic image.
3. Test a reset-button press while firmware is running.
4. Record the fitted processor, EPROM type, ROM checksum, jumper settings,
   supply source, and test results with the board.

The board is accepted for normal bench use when it boots the known-good image
reliably through several power cycles, reset works, supply current is normal,
and the intended console/GPIO tests pass.
