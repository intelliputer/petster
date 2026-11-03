## The Petster Deluxe

An archival and reverse-engineering workspace for the Axlon Petster Deluxe electronic pet.

![Petster Deluxe](images/petster-cat.JPG)

### What is preserved

Petster Deluxe is an electronic pet with a microprocessor-controlled behaviour system. It responds to sounds and touch, can be led by a leash, and uses forward sensing to avoid obstacles.

The central artifact is a 4 KiB ROM image. The 8039 is an Intel MCS-48-family controller with external program memory; the bundled 8048-family references and tools are included to support investigation of that ROM.

| Path | Purpose |
| --- | --- |
| [`code/petster.bin`](code/petster.bin) | Canonical 4,096-byte ROM image. |
| [`code/petster.hex`](code/petster.hex) | Intel HEX encoding of the canonical ROM. |
| [`code/petster-array`](code/petster-array) | C-style byte-array representation. |
| [`code/PetsterDeluxeEprom.zip`](code/PetsterDeluxeEprom.zip) | Original-style archive containing the same ROM payload. |
| [`docs/`](docs) | Owner's manual, technical guide, and reference material. |
| [`docs/TECHNICAL-RESEARCH.md`](docs/TECHNICAL-RESEARCH.md) | Sourced 1985 hardware findings, preserved teardown, and open questions. |
| [`datasheets/`](datasheets) | INS8039-family reference datasheet. |
| [`docs/UNIT-OBSERVATIONS.md`](docs/UNIT-OBSERVATIONS.md) | Owner-reported markings and the evidence still needed from this specific cat. |
| [`tools/`](tools/README.md) | Period 8048/8039 development and analysis tools. |

### Hardware status

The 27C128 banked-ROM daughterboard is now a routed, two-layer PCB suitable
for a standard fabrication run. It adapts the Petster's 24-pin National
`NMC27C32` socket to a 28-pin `27C128`, with two jumpers selecting A12 and
A13 (four 4 KiB banks). Its functional pin assignments have been checked
against the NMC27C32B and 27C128 datasheets.

| Item | Current state |
| --- | --- |
| KiCad source | [`hardware/27c128-daughterboard/`](hardware/27c128-daughterboard/) |
| PCB | Routed, 45 × 45 mm, two copper layers, 0.20 mm tracks |
| Electrical rules check | 0 violations; 0 unconnected items (KiCad, 2026-11-02) |
| Production archive | [`27c128-daughterboard.zip`](hardware/27c128-daughterboard/production/27c128-daughterboard.zip) |
| Solder mask | Present on both sides and on all plated pads |
| Hardware test | Pending continuity checks, then a controlled power-on test in the Petster |

This is a passive adapter: it relies on the Petster's existing +5 V supply
and external-ROM signals. Fit C1, both bank-select shunts, the 24-pin male
plug, and the 28-pin socket before use. Do not change bank jumpers while the
Petster is powered.

### Integrity and provenance

The ZIP payload and Intel HEX file both resolve byte-for-byte to `code/petster.bin`. The canonical ROM is 4,096 bytes and has this SHA-256 digest:

```text
609d6505297a6365abb4fdbd869a2d76aad65ebd2accc628e37023a11ffefee9
```

Run the following from the repository root to verify those representations:

```sh
./scripts/verify-rom.sh
```

The check requires standard POSIX utilities plus `unzip`, GNU `objcopy`, and `sha256sum`.

See [`docs/TECHNICAL-RESEARCH.md`](docs/TECHNICAL-RESEARCH.md) before working on hardware. It records the 1985 external-ROM architecture, the ROM's verified used range, and the checks needed before attaching an adapter.

### Reverse-engineering status

This project does not yet contain a validated disassembly. Earlier generated listings were removed because one decoded the ROM as Motorola 68HC11 instructions and another as x86; neither is valid for an MCS-48-family target. A reproducible, mechanical MCS-48/8039 linear listing is available at [`src/petster_8039_linear.asm`](src/petster_8039_linear.asm). It preserves every ROM byte and calculates MCS-48 branch targets, but it deliberately does not claim code-versus-data classification, labels, or behavioural analysis. Regenerate it with:

```sh
python3 scripts/disassemble-mcs48.py \
  'src/Petster Deluxe Eprom (Burnt on a 27c32 eprom).bin' \
  src/petster_8039_linear.asm
```

Treat `petster.bin` as the source of truth. A future disassembly should identify the exact MCS-48 tool and version, command line, ROM base address, CPU variant, and the byte ranges classified as code versus data. Contributions that add labels, hardware mappings, or behavioural analysis should cite the supporting manual, board observation, or ROM addresses.
