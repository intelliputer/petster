# 8039-II-SBC routing check — 2026-11-03

## Result

The schematic passes ERC: **0 errors, 0 warnings**.

The PCB is **not yet routed in the saved board file**:

- 84 unrouted connections
- 2 DRC warnings, both on J2:
  - J2 is a local footprint override that differs from the library footprint.
  - Its pin-1 silkscreen circle overlaps the pad/solder-mask opening.

No copper track or via segments are present in `8039-II-SBC.kicad_pcb`.
Fabrication exports are therefore intentionally not generated yet.

## Next action in KiCad

Route the remaining ratlines, then run **Inspect → Design Rules Checker**.  Clear the two J2 warnings by updating J2 from the schematic/library and moving or replacing its pin-1 marker so it does not overlap pad 1.

