# Petster 27C128 daughterboard

This is the active KiCad project for a passive, bank-selected adapter from
the Petster's 24-pin National `NMC27C32` socket to a 28-pin `27C128` EPROM.
It is for the external-ROM Petster revision.

The PCB is routed and has passed KiCad DRC with zero violations and zero
unconnected items. The manufacturing output is
[`production/27c128-daughterboard.zip`](production/27c128-daughterboard.zip).

## Function

`J1` is a 24-pin male-DIP plug on the underside. `U1` is the 28-pin EPROM
socket on top. The original address, data, enable, power, and ground signals
route directly between their equivalent pins. `JP1` selects A12 and `JP2`
selects A13, giving four 4 KiB banks. Change shunts only while the Petster is
unpowered.

The complete functional pin map and bank truth table are in
[`SCHEMATIC-REVIEW.md`](SCHEMATIC-REVIEW.md). The release and assembly checks
are in [`PRODUCTION-READINESS.md`](PRODUCTION-READINESS.md).

## Assembly

Fit the 24-pin male plug, a 0.600-inch-wide 28-pin socket, both three-pin
headers and shunts, and C1 (100 nF ceramic). The PCB has no voltage regulator:
it uses the Petster's existing +5 V supply.
