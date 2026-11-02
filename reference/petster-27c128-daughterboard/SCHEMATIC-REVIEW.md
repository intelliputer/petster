# Daughterboard schematic review — Rev A

This is the electrical contract for the KiCad schematic. Review and approve it before PCB placement or routing. It is specific to the reported National `NMC27C32` original EPROM and an external-ROM INS8039 Petster.

## Function

`J1` is a **24-pin male DIP plug**, made with turned/machined pins or an equivalent interposer—not a DIP socket. It plugs into the Petster's original NMC27C32 socket. `U1` is a 28-pin wide-DIP socket for a 27C128. The adapter has two three-pin jumpers, which select the two additional address bits while the Petster is unpowered.

```text
Petster 24-pin EPROM socket ── J1 ── U1: 27C128 socket
                                      │
                              JP1: A12 = 0 / 1
                              JP2: A13 = 0 / 1
```

## Direct signal map

All signals in this table are one-to-one connections. There is no logic, buffering, or address decoding on the adapter.

| Original NMC27C32 socket / J1 pin | Signal | 27C128 / U1 pin |
| ---: | --- | ---: |
| 1 | A7 | 3 |
| 2 | A6 | 4 |
| 3 | A5 | 5 |
| 4 | A4 | 6 |
| 5 | A3 | 7 |
| 6 | A2 | 8 |
| 7 | A1 | 9 |
| 8 | A0 | 10 |
| 9 | D0 | 11 |
| 10 | D1 | 12 |
| 11 | D2 | 13 |
| 12 | GND | 14 |
| 13 | D3 | 15 |
| 14 | D4 | 16 |
| 15 | D5 | 17 |
| 16 | D6 | 18 |
| 17 | D7 | 19 |
| 18 | `/CE` | 20 |
| 19 | A10 | 21 |
| 20 | `/OE` | 22 |
| 21 | A11 | 23 |
| 22 | A9 | 24 |
| 23 | A8 | 25 |
| 24 | +5 V | 28 |

## 27C128-only connections

| U1 pin | Signal | Connection |
| ---: | --- | --- |
| 1 | VPP | +5 V, **read mode only**; confirm against the exact 27C128 manufacturer's datasheet before fitting. |
| 2 | A12 | `JP1` centre pin. |
| 26 | A13 | `JP2` centre pin. |
| 27 | `/PGM` | +5 V, **read mode only**; confirm against the exact 27C128 manufacturer's datasheet before fitting. |

`C1` is a 100 nF ceramic capacitor directly between U1 pins 28 (+5 V) and 14 (GND).

## Bank-selection jumpers

Each 1×3 header is ordered `GND — address — +5 V`. Fit a shunt between the centre and the chosen end:

| Bank | JP2 / A13 | JP1 / A12 | 27C128 byte range |
| ---: | ---: | ---: | --- |
| 0 | 0 | 0 | `0x0000–0x0FFF` |
| 1 | 0 | 1 | `0x1000–0x1FFF` |
| 2 | 1 | 0 | `0x2000–0x2FFF` |
| 3 | 1 | 1 | `0x3000–0x3FFF` |

Never move either shunt while the Petster is powered. Fit one shunt on each header; leaving an address input floating is invalid.

## KiCad acceptance criteria

Before layout, the KiCad schematic must show every connection above, must have no dangling U1/J1/JP1/JP2/C1 pins, and must pass ERC with no errors. The PCB must subsequently use a 24-pin **plug** land pattern and a 28-pin **socket** land pattern, not two socket assumptions.
