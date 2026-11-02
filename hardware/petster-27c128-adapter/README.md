# Petster 27C128 banked-ROM adapter

This is a reversible 24-pin-EPROM-socket-to-28-pin-27C128 daughterboard design. It is intended for the 1985 external-ROM Petster only, after the exact EPROM socket and CPU/latch signals have been verified on the physical unit.

## Electrical plan

The 24-pin plug carries every original 27C32 signal to the 27C128 equivalent: `A0–A11`, `D0–D7`, `~CE`, `~OE`, `VCC`, and `GND`. The adapter supplies the additional 27C128 pins:

| 27C128 pin | Function | Adapter treatment |
| ---: | --- | --- |
| 1 | `VPP` | Tie to `VCC` for read mode, subject to the actual device datasheet. |
| 2 | `A12` | `BANK0`: 10 kΩ pull-down and a switch/jumper to `VCC`. |
| 26 | `A13` | `BANK1`: 10 kΩ pull-down and a switch/jumper to `VCC`. |
| 27 | `~PGM` | Hold high for read mode, subject to the actual device datasheet. |
| 28 | `VCC` | +5 V from the original ROM socket. |

`BANK1:BANK0` selects one of four 4 KiB images. Both pull down at power-up, selecting bank 0. Do not alter either selector while powered; change it with power off, then reset or power-cycle the Petster.

## Mechanical plan

* Bottom: 24-pin **wide** DIP male plug, `15.24 mm` row spacing, inserted into the original 27C32 socket.
* Top: 28-pin DIP socket or ZIF socket for the 27C128.
* Controls: two labelled jumpers or DIP-switch poles, `BANK0` and `BANK1`.
* Keep the adapter low enough to clear the enclosure and mark pin 1/orientation at both levels.

The original 27C32 is not fitted to this adapter. It remains the recovery ROM: remove the adapter and reinstall it directly to restore the factory configuration.

## Before building

1. Read the exact 27C128 manufacturer datasheet; confirm read-mode requirements for `VPP` and `~PGM`.
2. Continuity-check every plug-to-socket mapping with no EPROM installed.
3. Program the canonical 4 KiB baseline image into all four banks first.
4. Test every bank with the cat supported and a power switch immediately available.
