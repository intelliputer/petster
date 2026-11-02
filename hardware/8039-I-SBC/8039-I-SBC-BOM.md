# EDS 8039 controller reference BOM

This BOM was transcribed from the archived EDS schematic image. It is a purchasing/checklist aid for the generic reference board, not a verified Petster BOM. Confirm package, voltage rating, pinout, and jumper position against the source image before ordering or building.

| Refs | Qty | Value / part | Notes |
| --- | ---: | --- | --- |
| U1 | 1 | 8039-family MCU | Original design permits 8035/8039/8040, 8048/8049, or 8748/8749 variants; external-program selection is required. The Petster evidence currently points to an INS8039-compatible, externally programmed part. |
| U2 | 1 | 74LS373 | Octal latch for multiplexed low ROM address. |
| U3 | 1 | 27C32 EPROM | `Package_DIP:DIP-24_W15.24mm`; this is the Petster-relevant and default footprint. The original board describes alternatives, but those require pinout and jumper review. |
| U4 | 1 | 7805 | 5 V linear regulator. |
| Y1 | 1 | 2–12 MHz crystal | Select for the fitted MCU; check its clock limits. |
| R1 | 1 | 100 kΩ | Reset pull-up. |
| R2 | 1 | 10 kΩ | EPROM / bank-jumper support. |
| R3, R4 | 2 | 100 kΩ | I/O pull-ups. |
| C1, C2 | 2 | 22 pF | Crystal load capacitors. |
| C3 | 1 | 1 µF, ≥10 V | Reset timing capacitor. |
| C4, C5, C6 | 3 | 100 nF | Supply decoupling. |
| C7 | 1 | 47 µF, ≥10 V | Regulator input reservoir. |
| C8 | 1 | 2200 µF, ≥25 V | Regulator output reservoir. |
| D1 | 1 | 1N4148 | Reset discharge diode. |
| D2–D6 | 5 | 1N4004 | Input/reverse-polarity and rectifier network; verify orientation from the source image. |
| PB1 | 1 | Momentary pushbutton | Reset. |
| JP1, JP2 | 2 | 2-pin jumper | EPROM programming/configuration selection. |
| JP3 | 1 | 3-pin jumper | Upper-bank remap selection for larger EPROMs. |
| J1 | 1 | 2×10 IDC header | User I/O header. |
| J2 | 1 | 5-pin input header | 9–12 V AC/DC input connection. |

The machine-generated [`8039-I-SBC-bom.csv`](8039-I-SBC-bom.csv) is exported by KiCad from the symbols currently placed in the schematic. It is intentionally a partial BOM until the remaining support and jumper symbols have been placed and connected.

Do not fit a 27C128 directly at U3: it is a 28-pin DIP. Use a 24-pin-to-28-pin adapter for the banked-ROM experiment. The EDS `JP3` option is a fixed 4 KiB-window remap and cannot substitute for the adapter's two bank-select signals.
