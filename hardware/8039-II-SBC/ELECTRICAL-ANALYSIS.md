# 8039-II SBC electrical and functional analysis

## Scope and status

This review covers the released `8039-II-SBC.kicad_sch` and
`8039-II-SBC.kicad_pcb` after the final routing simplification.  It is an
electrical-design and manufacturability review; it does not replace inspection
and powered testing of the fabricated assembly.

The final KiCad checks completed on 2026-11-05:

| Check | Result |
| --- | --- |
| Schematic ERC | 0 errors, 0 warnings |
| PCB DRC | 0 violations |
| PCB connectivity | 0 unconnected pads |
| Footprint checks | 0 footprint errors |

## Functional blocks

### Processor, clock, and reset

U1 is an MCS-48 8039-compatible 40-pin processor.  Its 6 MHz crystal clock is
connected to X1/X2 with C2 and C3 (20 pF C0G) returned to ground.

The active-low reset circuit is:

```text
+5 V -- R1 (100 kOhm) --+-- U1.4 /RESET
                         +-- C1 (1 uF) -- GND
                         +-- SW1 -- GND
                         +-- D1 anode

D1 cathode -- +5 V
```

R1 and C1 provide a nominal 100 ms power-on reset delay.  SW1 provides a
manual reset.  D1 provides a fast capacitor-discharge path during power-down;
its cathode/bar end must be fitted toward +5 V.  C1 is polarized, with its
positive lead on the RESET node and negative lead on GND.

### External-ROM bus

The program-memory interface follows the MCS-48 multiplexed-bus arrangement:

| Function | Connection |
| --- | --- |
| Multiplexed low address/data | U1 DB0-DB7 to U2 inputs and U3 D0-D7 |
| Address latch enable | U1 ALE to U2 LE |
| Latched A0-A7 | U2 outputs to U3 A0-A7 |
| Upper address | U1 P2.0-P2.3 to U3 A8-A11 |
| Program read | U1 `/PSEN` to U3 `/OE` |
| EPROM enable | U3 `/CE` tied low |
| Latch output enable | U2 `/OE` tied low |

JP1 and JP2 set EPROM A12 and A13, selecting a 4 KiB page with GND = 0 and
+5 V = 1.  For a 27C128, JP3 and JP4 are both set to +5 V for normal read
operation.  With a 27C256, JP3 and JP4 select A14 and A15.  Change bank
settings only with power removed or U1 held in reset.

### EA and power selection

JP5 sets U1 EA:

| Processor use | JP5 setting |
| --- | --- |
| 8039 external program ROM | EA to +5 V |
| 8048 internal program ROM | EA to GND |

JP6 has exactly one valid fitted shunt:

| JP6 shunt | Board supply source |
| --- | --- |
| 1-2 | FTDI VCC at J1.3 |
| 2-3 | External regulated 5 V at J2.18 |

JP6.2 is the board +5 V rail.  Do not fit both shunts.  If the FTDI source is
used, verify that the adapter supplies 5 V rather than 3.3 V.

### I/O and decoupling

J2 is the processor expansion header.  It exposes the available GPIO and
external-bus control signals, but not the multiplexed DB0-DB7 bus.

| J2 pins | U1 signal | Function / production use |
| --- | --- | --- |
| 1-8 | P1.0-P1.7 | Eight quasi-bidirectional general-purpose I/O lines for firmware-controlled inputs or outputs. |
| 9-11 | P2.4-P2.6 | Three additional quasi-bidirectional general-purpose I/O lines. |
| 12 | T1 | External timer/counter input; firmware may use it for event counting or as a test input. |
| 13 | PROG | Firmware-controlled auxiliary/program-strobe output for an external peripheral. |
| 14 | `/RD` | Active-low external-data read strobe, asserted on external-memory (`MOVX`) read cycles. |
| 15 | `/WR` | Active-low external-data write strobe, asserted on external-memory (`MOVX`) write cycles. |
| 16 | `/INT` | Active-low external interrupt-request input. |
| 17 | `/SS` | Single-step control input for externally controlled/debug execution. |
| 18 | — | Optional regulated +5 V input; select it with JP6. This is not a logic signal. |
| 19 | — | Ground. |
| 20 | — | Intentionally unconnected. |

P2.0-P2.3 are not on J2 because they drive EPROM address bits A8-A11 during
program fetches. P2.7 is likewise not on J2 because it is the FTDI serial
transmit signal. J1 provides the FTDI/power interface, with J1.2 and J1.6
intentionally unconnected.

C4, C5, and C6 are 100 nF supply bypass capacitors.  They remain connected
across the +5 V and GND rails for U1, U2, and U3.

## PCB review

The board is a two-layer through-hole design.  The final simplification removed
redundant ground traces and retained a filled B.Cu GND zone over the board
area.  The zone has 0.20 mm clearance and 0.25 mm minimum copper thickness.
The DRC result confirms that the remaining copper and zone provide complete
connectivity; no ground or power pad is left isolated.

The four M3 mounting holes use copper clearance suitable for metal hardware.
They are not assigned to GND.

## Release conclusion

The schematic and routed board are electrically consistent and clear KiCad's
ERC/DRC checks.  The current production archive is suitable for fabrication.

Before accepting an assembled board, follow [`BRING-UP.md`](BRING-UP.md):
inspect the assembly, verify that +5 V is not shorted to GND, power the board
with current limiting, confirm reset and clock behaviour, and boot a
known-good diagnostic EPROM image.  Correct assembly, the selected jumper
settings, component orientation, and firmware content remain essential
real-world validation steps.
