# Production-readiness status

## Released PCB

`27c128-daughterboard.kicad_pcb` is a routed, 45 × 45 mm, two-layer
adapter PCB. It carries a 24-pin male DIP plug on its underside for the
Petster's original NMC27C32 socket and a 28-pin 27C128 socket on top.

The production package is [`production/27c128-daughterboard.zip`](production/27c128-daughterboard.zip).
It contains the current copper, solder-mask, silkscreen, outline, and drill
outputs.

## Checks completed

* KiCad PCB DRC: **0 violations and 0 unconnected items** (2026-11-02).
* Both copper layers are routed with 0.20 mm tracks.
* All 60 plated through-hole pads have solder-mask openings.
* The board outline is a closed 45 × 45 mm rectangle.
* The NMC27C32-to-27C128 functional pin mapping has been checked against the
  device datasheets.

## Before first power-on

1. Confirm the actual Petster ROM socket orientation and enclosure clearance.
2. Assemble the 24-pin plug, 28-pin socket, C1, and both jumper shunts.
3. With no EPROM fitted, continuity-check each J1-to-U1 connection and verify
   that +5 V is not shorted to GND.
4. Program a known-good image, fit the EPROM, and perform the initial powered
   test with a current-limited supply or a readily accessible power switch.

The KiCad schematic remains a useful record of the design intent, but its
archived ERC report is not clean; the PCB DRC and the published pin map are
the release checks for this board revision.
