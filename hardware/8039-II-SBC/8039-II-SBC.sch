EESchema Schematic File Version 4
LIBS:power
LIBS:device
LIBS:74xx
LIBS:MCU_Intel
LIBS:Memory_EPROM
LIBS:Connector_Generic
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Petster 8039-II-SBC"
Date "2026-11-03"
Rev "0.1"
Comp "Cartheur Research"
Comment1 "Pre-layout electrical draft — review exact MCU and EPROM datasheets before fabrication"
Comment2 "8039 external-ROM bench SBC with FTDI Friend console"
Comment3 "One 28-pin ROM socket: 27C32 offset, 27C128/27C256 normal"
Comment4 ""
$EndDescr
Text Notes 950 800 0    120  ~ 24
8039-II-SBC — EXTERNAL-ROM MCS-48 BENCH COMPUTER
Text Notes 950 1050 0    60   ~ 12
Socket a confirmed 8039-compatible MCU. Configure EA for external program fetches per its datasheet.
Text Notes 950 1175 0    60   ~ 12
27C32 placement: pin 1 in U3 pin 3 (leave U3 pins 1–2 empty).  27C128/27C256: align pin 1 normally.
$Comp
L MCU_Intel:8039 U1
U 1 1 66000001
P 3100 3800
F 0 "U1" H 2650 4850 50  0000 C CNN
F 1 "8039" H 3500 4850 50  0000 C CNN
F 2 "Package_DIP:DIP-40_W15.24mm_Socket" H 3100 3800 50  0001 C CNN
F 3 "" H 3100 3800 50  0001 C CNN
	1    3100 3800
	1    0    0    -1
$EndComp
$Comp
L 74xx:74LS373 U2
U 1 1 66000002
P 5450 4100
F 0 "U2" H 5100 4850 50  0000 C CNN
F 1 "74LS373" H 5750 4850 50  0000 C CNN
F 2 "Package_DIP:DIP-20_W7.62mm_Socket" H 5450 4100 50  0001 C CNN
F 3 "" H 5450 4100 50  0001 C CNN
	1    5450 4100
	1    0    0    -1
$EndComp
$Comp
L Memory_EPROM:27C128 U3
U 1 1 66000003
P 8550 3850
F 0 "U3" H 8100 5000 50  0000 C CNN
F 1 "27C128 / 27C256 / offset 27C32" H 8950 5000 50  0000 C CNN
F 2 "Package_DIP:DIP-28_W15.24mm_Socket" H 8550 3850 50  0001 C CNN
F 3 "" H 8550 3850 50  0001 C CNN
	1    8550 3850
	1    0    0    -1
$EndComp
$Comp
L Connector_Generic:Conn_01x06 J1
U 1 1 66000004
P 1300 4800
F 0 "J1" H 1218 5217 50  0000 C CNN
F 1 "FTDI FRIEND: GND CTS VCC TXO RXI DTR" H 1218 5126 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 1300 4800 50  0001 C CNN
F 3 "" H 1300 4800 50  0001 C CNN
	1    1300 4800
	-1   0    0    -1
$EndComp
$Comp
L Connector_Generic:Conn_01x03 JP1
U 1 1 66000005
P 7400 1700
F 0 "JP1" H 7480 1742 50  0000 L CNN
F 1 "A12: GND / A12 / +5V" H 7480 1651 50  0000 L CNN
	1    7400 1700
	1    0    0    -1
$EndComp
$Comp
L Connector_Generic:Conn_01x03 JP2
U 1 1 66000006
P 7400 2200
F 0 "JP2" H 7480 2242 50  0000 L CNN
F 1 "A13: GND / A13 / +5V" H 7480 2151 50  0000 L CNN
	1    7400 2200
	1    0    0    -1
$EndComp
$Comp
L Connector_Generic:Conn_01x03 JP3
U 1 1 66000007
P 7400 2700
F 0 "JP3" H 7480 2742 50  0000 L CNN
F 1 "A14: GND / A14 / +5V (27C256)" H 7480 2651 50  0000 L CNN
	1    7400 2700
	1    0    0    -1
$EndComp
$Comp
L Connector_Generic:Conn_01x03 JP4
U 1 1 66000008
P 7400 3200
F 0 "JP4" H 7480 3242 50  0000 L CNN
F 1 "ROM TYPE: +5V / U3.27 / A14" H 7480 3151 50  0000 L CNN
	1    7400 3200
	1    0    0    -1
$EndComp
$Comp
L Connector_Generic:Conn_01x02 JP5
U 1 1 66000009
P 1350 1700
F 0 "JP5" H 1268 1917 50  0000 C CNN
F 1 "EA SELECT" H 1268 1826 50  0000 C CNN
	1    1350 1700
	-1   0    0    -1
$EndComp
$Comp
L Connector_Generic:Conn_01x02 JP6
U 1 1 6600000A
P 1350 2150
F 0 "JP6" H 1268 2367 50  0000 C CNN
F 1 "USB POWER (OPEN)" H 1268 2276 50  0000 C CNN
	1    1350 2150
	-1   0    0    -1
$EndComp
$Comp
L Device:R R1
U 1 1 6600000B
P 1900 3000
F 0 "R1" H 1970 3046 50  0000 L CNN
F 1 "100k RESET pull-up" H 1970 2955 50  0000 L CNN
	1    1900 3000
	1    0    0    -1
$EndComp
$Comp
L Device:C C1
U 1 1 6600000C
P 2300 3300
F 0 "C1" H 2415 3346 50  0000 L CNN
F 1 "1uF RESET" H 2415 3255 50  0000 L CNN
	1    2300 3300
	1    0    0    -1
$EndComp
$Comp
L Switch:SW_Push SW1
U 1 1 6600000D
P 1900 3500
F 0 "SW1" V 1946 3452 50  0000 R CNN
F 1 "RESET" V 1855 3452 50  0000 R CNN
	1    1900 3500
	0    -1   -1   0
$EndComp
$Comp
L Device:D D1
U 1 1 6600000E
P 2600 3000
F 0 "D1" V 2554 3080 50  0000 L CNN
F 1 "1N4148 reset discharge" V 2645 3080 50  0000 L CNN
	1    2600 3000
	0    1    1    0
$EndComp
$Comp
L Device:Crystal Y1
U 1 1 6600000F
P 3400 6000
F 0 "Y1" H 3400 6268 50  0000 C CNN
F 1 "10MHz — verify MCU rating" H 3400 6177 50  0000 C CNN
	1    3400 6000
	0    -1   -1   0
$EndComp
$Comp
L Device:C C2
U 1 1 66000010
P 3000 6250
F 0 "C2" H 3115 6296 50  0000 L CNN
F 1 "22pF DNP/verify" H 3115 6205 50  0000 L CNN
	1    3000 6250
	1    0    0    -1
$EndComp
$Comp
L Device:C C3
U 1 1 66000011
P 3850 6250
F 0 "C3" H 3965 6296 50  0000 L CNN
F 1 "22pF DNP/verify" H 3965 6205 50  0000 L CNN
	1    3850 6250
	1    0    0    -1
$EndComp
Text Notes 4550 5450 0    55   ~ 11
Fit C4–C6: 100 nF ceramic, one at each IC supply pair. Add bulk capacitance at +5 V input.
Text Notes 7150 5550 0    55   ~ 11
U3 PIN-27 MODE: 27C128 requires +5 V (/PGM read mode); 27C256 uses selectable A14.
Text Notes 7150 5680 0    55   ~ 11
Never change ROM-type or bank shunts while powered. Fit every address-select shunt.
Text Label 4300 3000 0    50   ~ 0
AD0
Text Label 4300 3100 0    50   ~ 0
AD1
Text Label 4300 3200 0    50   ~ 0
AD2
Text Label 4300 3300 0    50   ~ 0
AD3
Text Label 4300 3400 0    50   ~ 0
AD4
Text Label 4300 3500 0    50   ~ 0
AD5
Text Label 4300 3600 0    50   ~ 0
AD6
Text Label 4300 3700 0    50   ~ 0
AD7
Text Label 6450 3000 0    50   ~ 0
A0
Text Label 6450 3100 0    50   ~ 0
A1
Text Label 6450 3200 0    50   ~ 0
A2
Text Label 6450 3300 0    50   ~ 0
A3
Text Label 6450 3400 0    50   ~ 0
A4
Text Label 6450 3500 0    50   ~ 0
A5
Text Label 6450 3600 0    50   ~ 0
A6
Text Label 6450 3700 0    50   ~ 0
A7
Text Notes 4200 2650 0    60   ~ 12
MCS-48 multiplexed bus
Text Notes 6400 2650 0    60   ~ 12
Latched low address
Text Notes 7800 2350 0    60   ~ 12
Universal ROM socket and bank controls
Text Label 6950 4050 0    50   ~ 0
A8
Text Label 6950 4150 0    50   ~ 0
A9
Text Label 6950 4250 0    50   ~ 0
A10
Text Label 6950 4350 0    50   ~ 0
A11
Text Label 6950 4550 0    50   ~ 0
~PSEN
Text Label 1850 4800 0    50   ~ 0
T0_RX
Text Label 1850 4900 0    50   ~ 0
P27_TX
Text Notes 900 5350 0    55   ~ 11
FTDI Friend: TXO → T0_RX; P2.7 → RXI. CTS/DTR NC in Rev A. VCC only via JP6.
Text Notes 900 7000 0    55   ~ 11
This schematic intentionally records the reviewed architecture before component-pin wiring/ERC. Complete it against the exact 8039 and EPROM datasheets before PCB layout.
$EndSCHEMATC
