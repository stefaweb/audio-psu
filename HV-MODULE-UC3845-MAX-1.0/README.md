# HV-MODULE-UC3845-MAX-1.0

<b>High Voltage DC-DC Power Supply - Max version</b>
<br><br>
Under development.
<br>
<br>
<b>HV-MODULE-UC3845-MAX version compared to the HV-PSU-UC3845 1.1 board</b>
<br>
- Support power up to 65W.
- New DC voltage ouput range: +120V to +485V
- New PCB size: 50 x 100 mm.
- New default Mosfet IRFB4615PBF (replacement: IPP200N15N3G or IRFB4019PBF or TK32E12N1,S1X).
- New default 12R value for R1.
- Changed OPA810 (U3) to SOT-23-5 version to reduce cost.
- Added a snubber circuit to reduce VdsPeak (C15/R11/D2).
- Added a damping network for Q1 (R12/C16) to reduce HF.
- R1 has moved to footprint 1206.
- Added R12 (0.1uF XR7) for Vref HF filtering.
- Changed parts number for C1 and C2 (1nF COG 1%).
- Changed C6 value (0.15uF XR7).
- Changed R3 (17K4) value (Frequency now 50KHz instead of 51KHz).
- Optimized value or parts numbers for R21, R22, R23 and R28.
- Removed TH fuse and replaced it with a SMD 5A fast fuse on the back.
- New output CLC filter with one electrolytic capacitor footprint before the coil and two footprints after inductor.
- Footprint for output filter electrolytic capacitors now accept D12.5.
- Possibility to use an TH or SMD inductor for L1.
- Q1 Mosfet can be installed at botton or below the PCB (to fit on a larger heatsink).
- The GND and B+ signals are duplicated on the output connector.
- D1 footprint now accept DO-201AD or TO-220 diode.
- Removed negative circuit from schematic and PCB.
- Removed unused test footprint.
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

![Image](https://github.com/user-attachments/assets/a55c0433-0dcf-49c5-af2e-af2cbaf476be)

![Image](https://github.com/user-attachments/assets/f4448bf2-0f2f-45b8-b667-f313ec97e2c9)

![Image](https://github.com/user-attachments/assets/c2a5589c-48cd-4dec-a617-963572e70fd1)

![Image](https://github.com/user-attachments/assets/d35abd56-00af-4a2a-8d59-e3eaf3cb4040)

![Image](https://github.com/user-attachments/assets/45dfc3aa-23f2-48a1-a0b5-18d69de82857)

![Image](https://github.com/user-attachments/assets/d4f10a4b-14d3-41ef-a96a-83fd3a112ebb)

IRFB4615 drain output - Vin = 24V 1.4A - Vout = 450V / 64mA - Vout ripple = 73mV

![Image](https://github.com/user-attachments/assets/ebacbdf8-1c76-46fd-aed0-8198899cc31d)
