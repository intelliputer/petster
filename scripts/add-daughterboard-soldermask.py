#!/usr/bin/env python3
"""Add top and bottom solder-mask openings to all PTH pads, preserving routing."""
import pcbnew

path = "hardware/petster-27c128-daughterboard/petster-27c128-daughterboard.kicad_pcb"
board = pcbnew.LoadBoard(path)
for footprint in board.GetFootprints():
    for pad in footprint.Pads():
        layers = pad.GetLayerSet()
        layers.AddLayer(pcbnew.F_Mask)
        layers.AddLayer(pcbnew.B_Mask)
        pad.SetLayerSet(layers)
board.Save(path)
