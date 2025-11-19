# HV-MODULE-UC3845-MAX-1.0

<b>High Voltage DC-DC Power Supply - Max version</b>
<br><br>
Under development.
<br>
<br>
<b>HV-MODULE-UC3845-MAX version compared to first HV-PSU-UC3845 1.1</b>
<br>
- Support power up to 65W.
- New DC voltage ouput range: +120V to +485V
- New PCB size: 50 x 100 mm.
- New default Mosfet IRFB4615.
- Changed U3 OPA810 to SOT-23-5 footprint to reduce cost.
- Added 2 snubber circuits (C15/R11/D2, and R12/C16).
- R1 has moved to footprint 1206.
- Added R12 0.1uF for Vref HF filtering.
- Changed parts for C1 and C2 (1nF COG 1%).
- Changed R3 value (Frequency now 50KHz instead of 51KHz).
- Optimized value for R21, R22, R23 and R28.
- Removed TH fuse and replaced it with a SMD 5A Fast fuse on the back.
- Removed negative circuit from schematic and PCB.
- New output CLC filter with one electrolytic capacitor footprint before the coil and two footprints after inductor.
- Footprint for output filter electrolytic capacitors now accept D12.5.
- Possibility to use an TH or SMD inductor for L1.
- Mosfet can be installed at botton or below the PCB (to fit on a larger heatsink).
- The GND and B+ signals are duplicated on the output connector.
- D1 footprint now accept DO-201AD or TO-220 diode.
- Integrated fuse now 5A.
- New mother board for power it up to 45W.
<br>
<b>Lab test condition:</b><br>
Input: 24V<br>
Output: 450V 120mA<br>
Power: 2.5A under 24V<br>
Consumption: 58W<br>
<br>
PCB size: 100x50mm

![Image](https://github.com/user-attachments/assets/81f605e9-1b9b-4230-8332-19b0aa078913)

![Image](https://github.com/user-attachments/assets/4da646b7-37e7-495e-9125-02c772db97ef)

![Image](https://github.com/user-attachments/assets/dd385116-074a-4f74-a2a3-d982852d0467)

![Image](https://github.com/user-attachments/assets/cd4c7495-e20c-4a14-a60e-666cd8dbbad0)

![Image](https://github.com/user-attachments/assets/96a21d87-3e85-4803-a3de-1a82d99cdacb)

![Image](https://github.com/user-attachments/assets/c53cae38-3346-427d-808c-0c7707242c06)

![Image](https://github.com/user-attachments/assets/7ddebdcd-dc64-41a1-9ddc-03e65da9e8e4)

Vin = 24V 1.4A - Vout = 450V / 64mA - Vout ripple = 73mV

![Image](https://github.com/user-attachments/assets/ebacbdf8-1c76-46fd-aed0-8198899cc31d)
