# Production-readiness status

## Current placement board

The current `petster-27c128-daughterboard.kicad_pcb` is a compact **38 × 45 mm**, two-layer placement-and-drill template. It includes the board outline, plated through-holes, jumper holes, capacitor holes, and front silkscreen. It is intended for manual routing in KiCad.

## What has passed

* PCB DRC: no geometry, silkscreen-edge, or footprint errors after the outline trim.
* The 24-pin plug and 28-pin socket patterns are separated by 2.54 mm horizontally, preventing pad overlap.

## Release blockers

Do not order this as a functional board yet. It has no routed copper because routing is being completed manually. Before generating Gerbers, the board needs:

1. Every net routed and PCB DRC rerun with no unconnected items.
2. The KiCad schematic recreated from `SCHEMATIC-REVIEW.md` and passing ERC.
3. Exact 27C128 read-mode requirements checked for the fitted manufacturer.
4. A final physical fit check against the Petster enclosure and ROM socket.
