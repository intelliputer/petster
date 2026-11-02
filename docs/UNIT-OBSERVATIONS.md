# Physical-unit observations

This log separates the owner's observations of the repository's Petster from conclusions drawn from public research. It is deliberately short: photographs and continuity measurements should be attached or linked beside each entry when available.

| Item | Observation | Evidence status | Design consequence |
| --- | --- | --- | --- |
| External EPROM | `NMC27C32` | Owner-reported marking; photograph pending | Standard 4 KiB × 8, 24-pin 2732 interface. A 27C128 needs a 24-pin-to-28-pin adapter. |
| CPU | `20-68039`, `+B8436`, and a two-wave mark described as National-style | Owner-reported marking; photograph pending | Consistent with the external-ROM INS8039 variant reported for 1985 Petsters. Treat the exact order/house number as unresolved. |
| CPU documentation | `datasheets/INS8039.pdf` | Local reference supplied; scanned copy | Use it for MCS-48 external-program timing and pin verification. Do not infer Petster net connections until they are measured. |

## Next evidence capture

1. Photograph the EPROM and CPU square-on, including pin-1 orientation and board silkscreen.
2. With power removed, record continuity from each EPROM socket pin to the CPU/latch and supply rails.
3. Record the 27C373 marking and its orientation.
4. Add the board revision, connector labels, date labels, and a photo of both sides of the board.

The adapter stays a non-fabrication reference until items 1–3 confirm the physical net mapping.
