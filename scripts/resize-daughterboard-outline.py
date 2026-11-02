#!/usr/bin/env python3
"""Resize only the Edge.Cuts outline; preserve the routed PCB verbatim."""
import pcbnew

path = "reference/petster-27c128-daughterboard/petster-27c128-daughterboard.kicad_pcb"
board = pcbnew.LoadBoard(path)

for item in board.GetDrawings():
    if isinstance(item, pcbnew.PCB_TEXT) and item.GetLayer() == pcbnew.B_SilkS:
        item.SetMirrored(True)

for item in list(board.GetDrawings()):
    if item.GetLayer() == pcbnew.Edge_Cuts:
        board.Remove(item)

def point(x, y):
    return pcbnew.VECTOR2I(pcbnew.FromMM(x), pcbnew.FromMM(y))

def edge(a, b):
    segment = pcbnew.PCB_SHAPE(board)
    segment.SetShape(pcbnew.SHAPE_T_SEGMENT)
    segment.SetStart(point(*a))
    segment.SetEnd(point(*b))
    segment.SetLayer(pcbnew.Edge_Cuts)
    segment.SetWidth(pcbnew.FromMM(0.05))
    board.Add(segment)

for start, end in [((108, 105), (148, 105)), ((148, 105), (148, 150)),
                   ((148, 150), (108, 150)), ((108, 150), (108, 105))]:
    edge(start, end)

board.Save(path)
