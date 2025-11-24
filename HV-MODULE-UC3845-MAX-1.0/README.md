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

![Image](https://github.com/user-attachments/assets/a55c0433-0dcf-49c5-af2e-af2cbaf476be)

![Image](https://github.com/user-attachments/assets/7316d510-3527-403a-b720-2cc5fe4359ed)

![Image](https://github.com/user-attachments/assets/bbc1d281-38e6-4edf-b066-c59f6eeb2619)

![Image](https://github.com/user-attachments/assets/beabd182-529c-4ee8-8c6c-5e2424139640)

![Image](https://github.com/user-attachments/assets/662d2069-14e6-4d9f-a5ae-879ebb83006a)

![Image](https://github.com/user-attachments/assets/3505c117-388b-492c-8e3e-e3fcac53af63)

![Image](https://github.com/user-attachments/assets/4d5dcb2d-fb41-4be7-91be-202b87eb3013)

IRFB4615 drain output - Vin = 24V 1.4A - Vout = 450V / 64mA - Vout ripple = 73mV

![Image](https://github.com/user-attachments/assets/ebacbdf8-1c76-46fd-aed0-8198899cc31d)
