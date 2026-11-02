# Petster Deluxe technical research

## Scope

This note records the externally sourced evidence used to guide work on the Petster Deluxe ROM and hardware. It distinguishes documented observations from items that must still be verified on the repository's physical cat.

## Preserved source

* [`Petster-Technical-Teardown-Jonathan-Painter.pdf`](Petster-Technical-Teardown-Jonathan-Painter.pdf) — Jonathan Painter, *Petster Deluxe: An in depth look into the Axlon Petster Deluxe robot*, 2010; downloaded from [The Old Robots](https://www.theoldrobots.com/book58/AxlonPetster.pdf) on 2026-11-02.
  * SHA-256: `90f73c5f50a5caa417225813048c6edb551b1c7a4b746cc8bf18eeccdfb3e625`
  * This is a collector teardown and technical report, not an original Axlon service manual.
* [Radio-Electronics, June 1986](https://www.worldradiohistory.com/Archive-Radio-Electronics/80s/1986/Radio_Electronics_June_1986.CV01.pdf) — contemporary product description of the microphone-controlled processor, two motors, obstacle sensing, LEDs, and leash.

## Findings applicable to the 1985 Deluxe model

The Painter teardown identifies the 1985 board as an INS8039 design with a 27C32 external EPROM and 27C373 octal latch. It describes a later 1986 revision with an INS8049 and internal program memory. The owner's reported markings for this unit—National `NMC27C32` EPROM and a 40-pin processor marked `20-68039`, `+B8436`, with the National-style wave mark—are consistent with that external-ROM 8039 variant. A clear component photograph remains the primary evidence; the house number has not been independently decoded.

The teardown describes two boards:

* A base board with two motor H-bridges and the gearbox optical-encoder input.
* A main board in the head containing the processor and most other electronics.

It also reports six D cells with a 6 V motor rail and a 9 V logic/LED rail; two microphones; front IR obstacle sensing; a gearbox IR optical encoder; and light sensing.

## ROM result

The teardown says that only 2 KiB of the 27C32 is used. The preserved ROM supports that conclusion: its final non-`FF` byte is at `0x079F`, and `0x0800–0x0FFF` are erased (`FF`) padding. The canonical 4 KiB image should nevertheless remain the programming and verification unit, because it captures the complete physical EPROM address space.

For the 27C128 adapter, retain the original address mapping and use four 4 KiB banks selected by the extra `A12` and `A13` lines. This is safer than immediately repurposing the unused 2 KiB region; it preserves reset and address behaviour while experiments begin.

## What is still unknown

No original Petster electrical schematic, component-value list, complete netlist, or verified CPU-port map was found in the public sources searched. Do not infer those details from the generic EDS 8039 reference board or from a different Petster revision. The EDS board demonstrates the normal 8039 external-ROM topology only; its `JP3` maps one 4 KiB EPROM half into the 8039's sole 4 KiB program window and is not runtime bank switching.

Before connecting an adapter or custom firmware, capture these from the actual unit:

1. Main-board revision and every IC marking.
2. Original EPROM label, orientation, and two independent reads.
3. 27C32 socket signals and the 27C373's connections.
4. The head-to-base connector pinout, with power rails identified first.
5. Evidence for each sensor and actuator mapping.

Record photos, measurements, ROM hashes, and confidence level beside every conclusion. The single physical Petster is the final reference when public documentation conflicts.
