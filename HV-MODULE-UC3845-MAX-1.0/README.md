# HV-MODULE-UC3845-MAX-1.0

<b>High Voltage DC-DC Power Supply - Max version</b>
<br><br>
Under development.
<br>
<br>
<b>HV-MODULE-UC3845-MAX version compared to first HV-PSU-UC3845 1.1 board</b>
<br>
- Support power up to 65W.
- New DC voltage ouput range: +120V to +485V
- New PCB size: 50 x 100 mm.
- New default Mosfet IRFB4615PBF (replacement: IRF3415PBF or IPP200N15N3GXKSA1 or IRFB4019PBF or TK32E12N1,S1X).
- Changed OPA810 (u3) to SOT-23-5 version to reduce cost.
- Added a snubber circuit to reduce VdsPeak (C15/R11/D2).
- Added a damping network for Q1 (R12/C16) to reduce HF.
- R1 has moved to footprint 1206.
- Added R12 0.1uF for Vref HF filtering.
- Changed parts for C1 and C2 (1nF COG 1%).
- Changed R3 value (Frequency now 50KHz instead of 51KHz).
- Optimized value or parts numbers for R21, R22, R23 and R28.
- Removed TH fuse and replaced it with a SMD 5A fast fuse on the back.
- Removed negative circuit from schematic and PCB.
- New output CLC filter with one electrolytic capacitor footprint before the coil and two footprints after inductor.
- Footprint for output filter electrolytic capacitors now accept D12.5.
- Possibility to use an TH or SMD inductor for L1.
- Mosfet can be installed at botton or below the PCB (to fit on a larger heatsink).
- The GND and B+ signals are duplicated on the output connector.
- D1 footprint now accept DO-201AD or TO-220 diode.
- Integrated fuse now 5A.
- New mother board for power it up to 45W.
- New UC3845 LTSpice Simulation 1.1
  
<br>
<b>Lab test condition:</b><br>
Input: 24V<br>
Output: 450V 120mA<br>
Power: 2.5A under 24V<br>
Consumption: 58W<br>
<br>
PCB size: 100x50mm

![Image](https://github.com/user-attachments/assets/81f605e9-1b9b-4230-8332-19b0aa078913)

![Image](https://github.com/user-attachments/assets/a8d52472-aa61-425f-98f2-dd3d038642e4)

![Image](https://github.com/user-attachments/assets/d4d2dc28-f551-460c-90d8-47df02eae4b3)

![Image](https://github.com/user-attachments/assets/cd4c7495-e20c-4a14-a60e-666cd8dbbad0)

![Image](https://github.com/user-attachments/assets/af42ace9-a288-44ba-8a3a-49302fcaaf25)

![Image](https://github.com/user-attachments/assets/39a34bb5-dae2-489e-9486-c5c8b203a7f7)

![Image](https://github.com/user-attachments/assets/44671733-e2c9-4d0d-a030-9885334d8957)

IRFB4615 drain output - Vin = 24V 1.4A - Vout = 450V / 64mA - Vout ripple = 73mV

![Image](https://github.com/user-attachments/assets/ebacbdf8-1c76-46fd-aed0-8198899cc31d)
