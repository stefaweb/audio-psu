# HV-MODULE-UC3845-MAX-1.0

<br>
<b>HV-PSU-UC3845-MAX version compared to first HV-PSU-UC3845 1.1</b>

- Support power up to 65W (need an external 75W AC-DC power supply).
- New DC voltage ouput range: 120-485V
- New PCB size: 50 x 100 mm.
- New default Mosfet xxxx (Vds > 150V, Qg < 70 nC, Ciss < 1800 pF, Rds(on) < 150 mΩ @ Vgs=10 V)
- R1 has moved to footprint 1206.
- Added R12 0.1uF for Vref HF filtering.
- Changed parts for C1 and C2 (1nF COG 1%)
- Changed R3 value and parts (Frequency now 50KHz instead of 51KHz)
- Removed negative parts and specific dedicated footprint.
- New output CLC filter with one electronic capacitor footprint before the coil and two footprints after the coil.
- Footprint for output filter electronics capacitors now accept D12.5.
- Possibility to use an TH or SMD inductor.
- Mosfet can be installed at botton or below the PCB (to fit on a larger heatsink)
- The GND and B+ signals are duplicated on the output connector.
- The D1 diode footprint now supports DO-201 and TO-220.
- New mother board for power it up to 45W.

<b>Lab test condition:</b><br>
Input: 24V<br>
Output: 450V 120mA<br>
Power: 2.5A under 24V<br>
Consumption: 58W<br>
Heatsink: 100x50x15mm<br>

Size: 100x50mm

![Image](https://github.com/user-attachments/assets/4013e5c9-fdbd-4de7-980b-e373365278c5)

![Image](https://github.com/user-attachments/assets/1dafbb42-e3bb-4a47-9123-29072d82b443)

![Image](https://github.com/user-attachments/assets/9c2fecd9-941a-45ba-841c-890cc488b585)

![Image](https://github.com/user-attachments/assets/b4017b69-fddc-4f6b-8990-04c959608327)

![Image](https://github.com/user-attachments/assets/63e6a7de-9056-472e-b355-cb85619c127a)
