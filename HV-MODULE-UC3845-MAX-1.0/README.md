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
- New default Mosfet IRFB4615PBF (replacement: IPP200N15N3GXKSA1 or IRFB4019PBF or TK32E12N1,S1X).
- New default 12R value for R1.
- Changed OPA810 (U3) to SOT-23-5 version to reduce cost.
- Added a snubber circuit to reduce VdsPeak (C15/R11/D2).
- Added a damping network for Q1 (R12/C16) to reduce HF.
- R1 has moved to footprint 1206.
- Added R12 (0.1uF) for Vref HF filtering.
- Changed parts number for C1 and C2 (1nF COG 1%).
- Changed R3 (17K4) value (Frequency now 50KHz instead of 51KHz).
- Optimized value or parts numbers for R21, R22, R23 and R28.
- Removed TH fuse and replaced it with a SMD 5A fast fuse on the back.
- Removed negative circuit from schematic and PCB.
- Removed unused test footprint.
- New output CLC filter with one electrolytic capacitor footprint before the coil and two footprints after inductor.
- Footprint for output filter electrolytic capacitors now accept D12.5.
- Possibility to use an TH or SMD inductor for L1.
- Q1 Mosfet can be installed at botton or below the PCB (to fit on a larger heatsink).
- The GND and B+ signals are duplicated on the output connector.
- D1 footprint now accept DO-201AD or TO-220 diode.
- New mother board for power it up to 45W.
- New UC3845A LTSpice Simulation 1.1
  
<br>
<b>Lab test condition:</b><br>
Input: 24V<br>
Output: 450V 120mA<br>
Power: 2.5A under 24V<br>
Consumption: 58W<br>
<br>
PCB size: 100x50mm

![Image](https://github.com/user-attachments/assets/81f605e9-1b9b-4230-8332-19b0aa078913)

![Image](https://github.com/user-attachments/assets/d776da0e-fd18-45c4-80a1-35f0f94b5ec6)

![Image](https://github.com/user-attachments/assets/5751922e-954e-4b9b-b309-7c25680291b9)

![Image](https://github.com/user-attachments/assets/cd4c7495-e20c-4a14-a60e-666cd8dbbad0)

![Image](https://github.com/user-attachments/assets/abcdc8f2-5c22-407c-9fcf-7bde1a86fe47)

![Image](https://github.com/user-attachments/assets/5b24a97c-8fa1-4626-bd3e-39490f760f1d)

![Image](https://github.com/user-attachments/assets/a4b6d4aa-601b-4542-aca7-01d6ab7769e8)

IRFB4615 drain output - Vin = 24V 1.4A - Vout = 450V / 64mA - Vout ripple = 73mV

![Image](https://github.com/user-attachments/assets/ebacbdf8-1c76-46fd-aed0-8198899cc31d)
