# Petster 27C128 daughterboard

This KiCad project describes a reversible, bank-selected adapter for the external-ROM Petster variant. It plugs into the original 24-pin 27C32 socket and carries a 28-pin 27C128.

The reviewable electrical source of truth is [`SCHEMATIC-REVIEW.md`](SCHEMATIC-REVIEW.md). It fixes the complete J1-to-U1 pin map, uses two three-pin bank-select jumpers, and specifies VPP/`~PGM` read-mode connections.

The intended physical arrangement is a centred 24-pin male-DIP plug on the bottom and a half-pitch-length-offset 28-pin EPROM socket on the top. This keeps the adapter compact while avoiding coincident, unlike pads and providing short two-layer routing channels.

It is a design reference, not yet a fabrication release. Verify the actual 27C128 manufacturer datasheet and all Petster socket signals before manufacture. The current PCB file is a routing study only and must not be sent for fabrication until the schematic has been recreated from the approved netlist and passes ERC.
