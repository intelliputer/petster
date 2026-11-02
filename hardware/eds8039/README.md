# EDS 8039 reference board — KiCad capture

This project captures the generic EDS 8039 controller shown in [`tools/Eds8039Board/8039s.gif`](../../tools/Eds8039Board/8039s.gif). It is a reference design for understanding the 8039 external-ROM interface; it is **not** a Petster schematic and must not be fabricated or connected to a Petster without independent verification.

The initial capture covers the processor, 74LS373 multiplexed-address latch, external 27C32, reset circuit, clock, user I/O header, and the board's 5 V regulator block. Named nets document the intended bus topology:

* `DB0`–`DB7`: multiplexed low address/data bus.
* `A0`–`A7`: latched low ROM address.
* `A8`–`A11`: upper ROM address from the processor.
* `~PSEN`, `ALE`, and `EA`: program-memory control.

## Relevance to Petster

The EDS design is a useful **bus-topology reference** for the early external-ROM Petster: an 8039 presents multiplexed `A0`–`A7`/`D0`–`D7`, `ALE` drives a 74LS373-class latch, `P2.0`–`P2.3` provide `A8`–`A11`, and `~PSEN` controls program reads. It is not evidence of Petster component values, connectors, power circuitry, I/O assignments, or net routing.

Its source documentation says `JP3` remaps addresses `0x1000`–`0x1FFF` of a larger EPROM into the 8039's fixed `0x0000`–`0x0FFF` program window. That provides an erase-and-retry convenience, not live bank switching. A Petster 27C128 adapter instead needs independently controlled `A12` and `A13`, with the bank changed only while power is off or the MCU is held in reset.

Open `eds8039-reference.kicad_sch` in KiCad 10 or later. It was migrated and exported successfully with the installed Flatpak KiCad 10. The machine-generated CSV BOM and the source-image transcription checklist are both included.

The current ERC report deliberately records unresolved pins while the image transcription is completed. It is an audit artifact, not a clean electrical verification; no EDS PCB fabrication files should be generated from it yet.
