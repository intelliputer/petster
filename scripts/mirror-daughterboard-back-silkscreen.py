#!/usr/bin/env python3
"""Mirror existing bottom-silkscreen text without changing PCB connectivity or geometry."""
import pcbnew

path = "hardware/petster-27c128-daughterboard/petster-27c128-daughterboard.kicad_pcb"
board = pcbnew.LoadBoard(path)
for item in board.GetDrawings():
    if isinstance(item, pcbnew.PCB_TEXT) and item.GetLayer() == pcbnew.B_SilkS:
        item.SetMirrored(True)
board.Save(path)
