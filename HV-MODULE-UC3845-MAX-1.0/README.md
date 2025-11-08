# HV-MODULE-UC3845-MAX-1.0

<br>
<b>HV-PSU-UC3845-MAX version compared to first HV-PSU-UC3845 1.1</b>

- Support power up to 65W.
- New DC voltage ouput range: +120V to +485V
- New PCB size: 50 x 100 mm.
- New default Mosfet IRFB4615 (Vds ≥ 150V, Qg ≤ 70 nC, Ciss ≤ 2000 pF, Rds(on) ≤ 150 mΩ @ Vgs=10 V).
- Added a snubber (C15, R11 and D2).
- R1 has moved to footprint 1206.
- Added R12 0.1uF for Vref HF filtering.
- Changed parts for C1 and C2 (1nF COG 1%).
- Changed R3 value (Frequency now 50KHz instead of 51KHz).
- Changed R21, R22, R23 and R28 values.
- Removed negative parts form schematic and PCB.
- New output CLC filter with one electronic capacitor footprint before the coil and two footprints after the coil.
- Footprint for output filter electronics capacitors now accept D12.5.
- Possibility to use an TH or SMD inductor for L1.
- Mosfet can be installed at botton or below the PCB (to fit on a larger heatsink).
- The GND and B+ signals are duplicated on the output connector.
- The D1 diode footprint now supports DO-201 and TO-220.
- Integrated fuse now 5A.
- New mother board for power it up to 45W.

<b>Lab test condition:</b><br>
Input: 24V<br>
Output: 450V 120mA<br>
Power: 2.5A under 24V<br>
Consumption: 58W<br>
Heatsink: 100x50x15mm<br>

PCB size: 100x50mm
![Image](https://github.com/user-attachments/assets/1bf8086c-ff88-4b36-a7b9-42be59c1bd74)

![Image](https://github.com/user-attachments/assets/a3aa0362-331f-4d83-8799-a9ee5cf1aa22)

![Image](https://github.com/user-attachments/assets/829920a6-592e-4119-b97a-45d743dcb5b3)

![Image](https://github.com/user-attachments/assets/b4017b69-fddc-4f6b-8990-04c959608327)

![Image](https://github.com/user-attachments/assets/05b69a26-7f62-4bc4-ae90-d55410f6fe6b)
