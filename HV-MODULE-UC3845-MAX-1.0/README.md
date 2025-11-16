# HV-MODULE-UC3845-MAX-1.0

<b>High Voltage DC-DC Power Supply - Max version</b>

Under development.

<br>
<b>HV-MODULE-UC3845-MAX version compared to first HV-PSU-UC3845 1.1</b>

- Support power up to 65W.
- New DC voltage ouput range: +120V to +485V
- New PCB size: 50 x 100 mm.
- New default Mosfet XXX (Vds ≥ 150V, Qg ≤ 70 nC, Ciss ≤ 2000 pF, Rds(on) ≤ 150 mΩ @ Vgs=10 V).
- Added a snubber circuit (C15, R11 and D2).
- R1 has moved to footprint 1206.
- Added R12 0.1uF for Vref HF filtering.
- Changed parts for C1 and C2 (1nF COG 1%).
- Changed R3 value (Frequency now 50KHz instead of 51KHz).
- Changed R21, R22, R23 and R28 values.
- Removed TH fuse and replaced it with a SMD fuse on the back.
- Removed negative circuit from schematic and PCB.
- New output CLC filter with one electrolytic capacitor footprint before the coil and two footprints after inductor.
- Footprint for output filter electrolytic capacitors now accept D12.5.
- Possibility to use an TH or SMD inductor for L1.
- Mosfet can be installed at botton or below the PCB (to fit on a larger heatsink).
- The GND and B+ signals are duplicated on the output connector.
- The D1 footprint now supports DO-201AD or TO-220 diode.
- Integrated fuse now 5A.
- New mother board for power it up to 45W.

<b>Lab test condition:</b><br>
Input: 24V<br>
Output: 450V 120mA<br>
Power: 2.5A under 24V<br>
Consumption: 58W<br>
Heatsink: 100x50x15mm<br>

PCB size: 100x50mm
![Image](https://github.com/user-attachments/assets/81f605e9-1b9b-4230-8332-19b0aa078913)

![Image](https://github.com/user-attachments/assets/7c2ec124-28e7-4ab8-8709-78c3f4e05c80)

![Image](https://github.com/user-attachments/assets/cefa2ec4-6f89-4376-bd55-79bddd73131d)

![Image](https://github.com/user-attachments/assets/cd4c7495-e20c-4a14-a60e-666cd8dbbad0)

![Image](https://github.com/user-attachments/assets/c12b5294-1991-4096-97e2-e0b83394417b)
