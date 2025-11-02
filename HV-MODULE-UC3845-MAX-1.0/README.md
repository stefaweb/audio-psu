# HV-MODULE-UC3845-MAX-1.0

<br>
<b>HV-PSU-UC3845-MAX version compared to first HV-PSU-UC3845 1.1</b>

- Support power up to 65W (need an external 75W AC-DC power supply).
- New DC voltage ouput range: 120-485V
- New PCB size: 50 x 100 mm.
- New default Mosfet IRF1010EZ (produce less heat, cheaper than IRF3205Z)
- New optimized component values ​​around the UC3845A (C1, C2, C5, R1, R5).
- C1 has moved to footprint 1206.
- R1 has moved to footprint 1206.
- Removed negative parts and specific dedicated footprint
- New output CLC filter with one electronic capacitor footprint before the coil and two footprints after the coil.
- Footprint for output filter electronics capacitor now accept D12.5.
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

![Image](https://github.com/user-attachments/assets/2abaa6a5-f272-4931-895f-04917cda1f99)

![Image](https://github.com/user-attachments/assets/71706521-9f05-4657-840a-edd8bb1e61f1)

![Image](https://github.com/user-attachments/assets/b4017b69-fddc-4f6b-8990-04c959608327)

![Image](https://github.com/user-attachments/assets/b220ef85-5b95-4072-974c-80724e3f92b7)
