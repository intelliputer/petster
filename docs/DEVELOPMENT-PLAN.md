# Petster Deluxe development plan

## Goal

Develop and test alternate Petster behaviours without modifying the only available cat or losing the original firmware. The first milestone is a reversible, reset-selected four-bank ROM adapter using a 27C128.

## Non-negotiable safeguards

* Do not desolder, cut traces, or permanently alter the Petster.
* Keep the original EPROM, its socket orientation, and the known-good ROM image untouched.
* Use a socketed adapter that plugs into the existing 27C32 position. A 27C128 is not a drop-in physical replacement for a 27C32: it needs an adapter because it has additional address pins and a different package footprint.
* Keep a physical power switch within reach. Test with the cat supported so its wheels cannot drive away, and keep clear of moving parts.
* Change ROM banks only while power is off, then reset the controller. Runtime bank switching is a later experiment, not a requirement for the first prototype.

## Phase 0 — establish a golden baseline

1. Photograph the unit before opening it: exterior, board, connectors, EPROM label, socket notch, and all cable routing.
2. Record its current behaviour in a short video: power-on, sound response, touch response, motion, and sound output. Note battery type and measured supply voltage.
3. Read the original EPROM at least twice, preferably with two readers or on separate sessions. Compare both reads with [`code/petster.bin`](../code/petster.bin) and record the SHA-256 value.
4. Run `./scripts/verify-rom.sh` and save the result with the experiment log.
5. If the physical EPROM does not match the repository ROM, stop and preserve both images separately. Do not treat either as a replacement for the other.

**Exit criterion:** a documented, working cat; an untouched original EPROM; and a verified baseline image.

## Phase 1 — build a reversible ROM adapter

The 8039 sees a 4 KiB program window. A 27C128 contains 16 KiB, so it can expose four independent 4 KiB images. The preserved baseline has program content only below `0x0800`, but retain its full 4 KiB address mapping—including erased padding—during the first adapter experiments.

| Bank | 27C128 address range | `A13` | `A12` |
| --- | --- | --- | --- |
| 0 | `0x0000–0x0FFF` | 0 | 0 |
| 1 | `0x1000–0x1FFF` | 0 | 1 |
| 2 | `0x2000–0x2FFF` | 1 | 0 |
| 3 | `0x3000–0x3FFF` | 1 | 1 |

1. The original EPROM is identified as a National `NMC27C32`, which establishes the standard 24-pin 2732 pinout. Confirm the Petster socket signals by continuity on the actual board and document the 27C373 latch connections before making the adapter.
2. Make a 27C32-socket-to-27C128 adapter. Map the existing ROM address, data, chip-enable, output-enable, ground, and supply signals directly; put the 27C128 into its normal read mode.
3. Drive the two additional 27C128 address lines (`A12`, `A13`) from a two-position-per-bit DIP switch or jumper block. Add defined pull-downs so the default is always bank 0.
4. Label the adapter's orientation, bank settings, and supply voltage. Inspect continuity and check for shorts before it goes near the cat.
5. Program the baseline `petster.bin` into **all four** 4 KiB banks. Confirm that every switch position starts and runs the unmodified behaviour.

**Exit criterion:** all four positions reproduce the baseline, and reinserting the original EPROM restores the cat immediately.

## Phase 2 — map the existing firmware before changing behaviour

1. Create a reproducible MCS-48/8039 disassembly workflow. Record the tool version, options, CPU variant, and assumed ROM base address.
2. Cross-check instructions against the local MCS-48 reference material in [`tools/8048/`](../tools/8048/).
3. Maintain an address-based notebook: reset vector, interrupt vector, input polling, output writes, delay loops, sound routines, motor routines, and lookup tables.
4. Correlate each observation with a controlled black-box test of the original firmware. Change only one stimulus at a time: clap, touch, leash, front obstacle, and wake-up sound.
5. Treat motor and sensor pin assignments as hypotheses until confirmed with non-invasive probing and repeatable observations.

**Exit criterion:** a reviewed map of the reset path and at least one confirmed input-to-output behaviour path.

## Phase 3 — make safe diagnostic firmware

Reserve the banks as follows:

| Bank | Purpose |
| --- | --- |
| 0 | Immutable known-good baseline ROM. |
| 1 | Minimal diagnostics; no autonomous motion. |
| 2 | Incremental behaviour experiments. |
| 3 | Recovery copy or a second known-good build. |

1. Start bank 1 with a minimal bootable image that does not command the drive motors.
2. Add one observable, low-risk action at a time, such as a status output or speaker chirp, only after its output mapping is confirmed.
3. Add input logging or simple response tests before attempting motor control.
4. After every successful change, program the same image into bank 3 as a recovery image and save its source, binary, checksum, and test notes.

**Exit criterion:** diagnostics boot reliably from bank 1 and the baseline bank remains selectable.

## Phase 4 — behaviour experiments

1. Make small, single-purpose changes: timing, sound selection, one sensor threshold, or one state-transition rule.
2. Test each build on the supported cat with a time limit and the power switch ready.
3. Record the bank, firmware hash, battery voltage, setup, expected result, actual result, and any unexpected actuator movement.
4. Promote a build to bank 2 only after it survives repeated cold starts and basic safety checks.
5. Keep bank 0 unchanged throughout experimentation.

## Phase 5 — optional runtime bank switching

Only consider this after reset-selected banking is dependable. A runtime switch must be controlled by firmware and external latch logic, with a defined handoff point. It needs careful treatment of reset vectors, calls, interrupts, lookup-table references, and any code fetched across a bank boundary. It is not needed to create multiple behaviour personalities.

## Experiment log template

```text
Date / operator:
Cat configuration and battery voltage:
Adapter revision and bank selected:
EPROM image name and SHA-256:
Change from previous image:
Expected behaviour:
Observed behaviour:
Safety observations / current draw:
Result and next action:
```

## First session checklist — baseline only

1. Do only Phase 0.
2. Verify the physical ROM read before programming anything.
3. Do not install an adapter or experimental ROM during this session.
4. Decide whether the baseline evidence is sufficient before moving to adapter construction.
5. Stop if the cat's baseline behaviour changes or supply current is unusual.
