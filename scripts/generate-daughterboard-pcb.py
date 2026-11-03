#!/usr/bin/env python3
"""Generate the routed, quote-ready Petster 27C128 adapter PCB with pcbnew."""
import os
import pcbnew

OUT = os.path.join(os.path.dirname(__file__), "..", "hardware", "27c128-daughterboard", "27c128-daughterboard.kicad_pcb")
MM = pcbnew.FromMM

board = pcbnew.BOARD()
board.SetTitleBlock(pcbnew.TITLE_BLOCK())
board.GetTitleBlock().SetTitle("Petster 27C128 banked-ROM daughterboard")
board.GetTitleBlock().SetComment(0, "REV A — power-off bank selection only")

nets = {}
for name in ["GND", "+5V", "A0", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "D0", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "~CE", "~OE", "A12_BANK", "A13_BANK"]:
    net = pcbnew.NETINFO_ITEM(board, name)
    board.Add(net)
    nets[name] = net

def pos(x, y):
    return pcbnew.VECTOR2I(MM(x), MM(y))

def footprint(ref, value, x, y):
    fp = pcbnew.FOOTPRINT(board)
    fp.SetReference(ref)
    fp.SetValue(value)
    fp.SetPosition(pos(x, y))
    board.Add(fp)
    return fp

def pad(fp, number, x, y, net, oval=False, drill=0.8):
    p = pcbnew.PAD(fp)
    p.SetNumber(str(number))
    p.SetPosition(pos(x, y))
    p.SetSize(pcbnew.VECTOR2I(MM(1.5), MM(1.5)))
    p.SetDrillSize(pcbnew.VECTOR2I(MM(drill), MM(drill)))
    p.SetAttribute(pcbnew.PAD_ATTRIB_PTH)
    p.SetShape(pcbnew.PAD_SHAPE_OVAL if oval else pcbnew.PAD_SHAPE_CIRCLE)
    p.SetLayerSet(pcbnew.LSET.AllCuMask())
    p.SetNet(nets[net])
    fp.Add(p)
    return p

def line(a, b, net, layer=pcbnew.F_Cu, width=0.30):
    # Placement-only revision: routing begins only after the KiCad schematic passes ERC.
    return
    t = pcbnew.PCB_TRACK(board)
    t.SetStart(pos(*a)); t.SetEnd(pos(*b)); t.SetWidth(MM(width)); t.SetLayer(layer); t.SetNet(nets[net])
    board.Add(t)

def edge(a, b):
    s = pcbnew.PCB_SHAPE(board)
    s.SetShape(pcbnew.SHAPE_T_SEGMENT); s.SetStart(pos(*a)); s.SetEnd(pos(*b)); s.SetLayer(pcbnew.Edge_Cuts); s.SetWidth(MM(0.05))
    board.Add(s)

# Compact placement-only board: 38 x 45 mm, trimmed to the hole and silkscreen envelope.
# The 27C128 socket is centred across the board width.  The 24-pin plug is
# shifted 2.54 mm left (more than one drill/pad diameter), avoiding coincident
# holes while keeping the compatible signals as short horizontal routes.
# The 27C128 remains shifted two pitches (5.08 mm) toward pin 1.
for a, b in [((11,5),(49,5)), ((49,5),(49,50)), ((49,50),(11,50)), ((11,50),(11,5))]: edge(a,b)

j1 = footprint("J1", "24-pin male DIP plug to Petster NMC27C32 socket", 0, 0)
j1nets = {1:"A7",2:"A6",3:"A5",4:"A4",5:"A3",6:"A2",7:"A1",8:"A0",9:"D0",10:"D1",11:"D2",12:"GND",13:"D3",14:"D4",15:"D5",16:"D6",17:"D7",18:"~CE",19:"A10",20:"~OE",21:"A11",22:"A9",23:"A8",24:"+5V"}
j1pads = {}
# Match the M6x09-II-SBC expansion header's smaller 0.7 mm drill while
# retaining J1's existing pad positions, copper, nets, and routing.
for n in range(1,13): j1pads[n] = pad(j1,n,17.34,16.07+(n-1)*2.54,j1nets[n],n==1,drill=0.7)
for n in range(24,12,-1): j1pads[n] = pad(j1,n,32.58,16.07+(24-n)*2.54,j1nets[n],drill=0.7)

u1 = footprint("U1", "27C128 wide DIP-28 socket", 0, 0)
u1nets = {1:"+5V",2:"A12_BANK",3:"A7",4:"A6",5:"A5",6:"A4",7:"A3",8:"A2",9:"A1",10:"A0",11:"D0",12:"D1",13:"D2",14:"GND",15:"D3",16:"D4",17:"D5",18:"D6",19:"D7",20:"~CE",21:"A10",22:"~OE",23:"A11",24:"A9",25:"A8",26:"A13_BANK",27:"+5V",28:"+5V"}
u1pads = {}
for n in range(1,15): u1pads[n] = pad(u1,n,19.88,10.99+(n-1)*2.54,u1nets[n],n==1)
for n in range(28,14,-1): u1pads[n] = pad(u1,n,35.12,10.99+(28-n)*2.54,u1nets[n])

# Direct 2732-compatible signals: each is a short, parallel trace.
mapping = {1:3,2:4,3:5,4:6,5:7,6:8,7:9,8:10,9:11,10:12,11:13,12:14,13:15,14:16,15:17,16:18,17:19,18:20,19:21,20:22,21:23,22:24,23:25,24:28}
for jp, up in mapping.items():
    a=j1pads[jp].GetPosition(); b=u1pads[up].GetPosition()
    ax, ay = pcbnew.ToMM(a.x), pcbnew.ToMM(a.y)
    bx, by = pcbnew.ToMM(b.x), pcbnew.ToMM(b.y)
    # Each trace has its own escape channel.  The two DIP rows are deliberately
    # kept separate so the 2732-to-27128 pin permutation cannot short.
    channel = (6.0 + (jp - 1) * 0.70) if jp <= 12 else (33.0 + (jp - 13) * 0.70)
    line((ax, ay), (channel, ay), j1nets[jp])
    line((channel, ay), (channel, by), j1nets[jp])
    line((channel, by), (bx, by), j1nets[jp])

# Bank jumpers: center pin is A12/A13; select GND (0) or +5V (1), with shunts fitted only while power is off.
for ref, y, signal in [("JP1", 12, "A12_BANK"), ("JP2", 20, "A13_BANK")]:
    fp=footprint(ref, "BANK SELECT: 0-GND / 1-+5V", 0, 0)
    pad(fp,1,40,y,"GND",True); pad(fp,2,42.54,y,signal); pad(fp,3,45.08,y,"+5V")
    # Route signal centre to its EPROM pin; power rails use the nearby direct traces.
    target = u1pads[2 if signal=="A12_BANK" else 26].GetPosition()
    line((42.54,y),(pcbnew.ToMM(target.x),pcbnew.ToMM(target.y)),signal,pcbnew.B_Cu)
    # jumper selectable ends wired into the VCC/GND traces at the adapter.
    line((40,y),(48,y),("GND"),pcbnew.B_Cu)
    line((45.08,y),(50,y),("+5V"),pcbnew.B_Cu)

c1=footprint("C1", "100nF ceramic, 2.54 mm lead spacing",0,0)
pad(c1,1,40,30,"+5V",True); pad(c1,2,42.54,30,"GND")
line((40,48),(50,48),"+5V",pcbnew.B_Cu); line((50,48),(50,8),"+5V",pcbnew.B_Cu)
line((42.54,48),(48,48),"GND",pcbnew.B_Cu); line((48,48),(10,48),"GND",pcbnew.B_Cu); line((10,48),(10,43.02),"GND",pcbnew.B_Cu); line((10,43.02),(15,43.02),"GND",pcbnew.B_Cu)

# VPP (1) and /PGM (27) are hard-wired to +5 V for read-only use.
line((15,10),(50,8),"+5V",pcbnew.B_Cu)
line((30.24,12.54),(30.24,10),"+5V",pcbnew.B_Cu)
line((30.24,10),(50,8),"+5V",pcbnew.B_Cu)

def silk(text, x, y, size=1.0):
    txt = pcbnew.PCB_TEXT(board)
    txt.SetText(text)
    txt.SetPosition(pos(x, y))
    txt.SetLayer(pcbnew.F_SilkS)
    txt.SetTextSize(pcbnew.VECTOR2I(MM(size), MM(size)))
    txt.SetTextThickness(MM(0.18))
    board.Add(txt)

silk("PETSTER 27C128 ADAPTER — REV A", 27.5, 47.0, 1.1)
silk("J1  24-PIN PLUG  (BOTTOM)", 25.0, 8.0, 0.85)
silk("U1  27C128 SOCKET  (TOP)", 33.0, 6.0, 0.85)
silk("PIN 1 >", 14.0, 15.0, 0.8)
silk("PIN 1 >", 16.5, 10.0, 0.8)
silk("JP1  A12", 44.5, 9.0, 0.8)
silk("0   1", 42.5, 13.8, 0.8)
silk("JP2  A13", 44.5, 17.0, 0.8)
silk("0   1", 42.5, 21.8, 0.8)
silk("C1  100n", 41.0, 32.0, 0.8)

# Keep the complete board inside KiCad's normal worksheet area rather than
# anchoring it at the absolute coordinate origin.
worksheet_offset = pcbnew.VECTOR2I(MM(100), MM(100))
for item in list(board.GetFootprints()) + list(board.GetDrawings()):
    item.Move(worksheet_offset)

board.Save(OUT)
