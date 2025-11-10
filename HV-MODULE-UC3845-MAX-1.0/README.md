# HV-MODULE-UC3845-MAX-1.0

<b>High Voltage DC-DC Power Supply - Max version</b>

Under development.

<br>
<b>HV-PSU-UC3845-MAX version compared to first HV-PSU-UC3845 1.1</b>

- Support power up to 65W.
- New DC voltage ouput range: +120V to +485V
- New PCB size: 50 x 100 mm.
- New default Mosfet IRFB4615 (Vds ≥ 150V, Qg ≤ 70 nC, Ciss ≤ 2000 pF, Rds(on) ≤ 150 mΩ @ Vgs=10 V).
- Added a snubber circuit (C15, R11 and D2).
- R1 has moved to footprint 1206.
- Added R12 0.1uF for Vref HF filtering.
- Changed parts for C1 and C2 (1nF COG 1%).
- Changed R3 value (Frequency now 50KHz instead of 51KHz).
- Changed R21, R22, R23 and R28 values.
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
![Image](https://github.com/user-attachments/assets/41839fb8-1d0e-4321-a148-2fafe1b4099e)

![Image](https://github.com/user-attachments/assets/1470607f-7049-417d-a500-253ae3f6e140)

![Image](https://github.com/user-attachments/assets/f0c7e1e7-22f4-472e-93f0-cefb19ff5588)

![Image](https://github.com/user-attachments/assets/b4017b69-fddc-4f6b-8990-04c959608327)

![Image](https://github.com/user-attachments/assets/c12b5294-1991-4096-97e2-e0b83394417b)
