# LVPS DC-AC Regulated Inverter EGS

<b>Project under development.</b>

DC-AC 4-8V AC power supply for heating audio tubes.

This DC-AC regulated power supply board is used to power the audio tube heater with AC voltage. The voltage is adjustable from 4V to 8V via a potentiometer on the PCB.

The LVPS DC-AC Regulated Inverter EGS board is based on the use of the EGS002 module. It is a control board for pure sine wave inverters, primarily used in DC-AC power conversion systems.

It integrates the EG8010 chipset for generating pure sine waves with digital control and dead-time management. The module supports fixed frequencies of 50Hz and 60Hz, as well as adjustable frequencies ranging from 0 to 400Hz (need mods).

It offers protections against overvoltage, undervoltage, overcurrent, and overheating.

The LVPS DC-AC Regulated Inverter EGS board operates up to about 4A with a voltage of 12Vdc or 15Vdc (prefered). It can be configured with different inductors in the output filter depending on the types of audio tubes to be heated and the needed power.

The board has an output on 3 pins with an optional middle point (2 resistors to be soldered under the PCB). This avoids soldering the cathode resistors onto the tube socket.


PCB size: 110 x 44 mm, Height: 42 mm
![proto_1_live](https://github.com/user-attachments/assets/02422585-1285-445d-99c7-c7ba34aeaa83)

![3D](https://github.com/user-attachments/assets/2496f39d-2d90-4a6f-acf9-cefd24a25147)

![Front](https://github.com/user-attachments/assets/5f82ab2c-a95d-4607-acbc-b7f53503b762)

![Back](https://github.com/user-attachments/assets/ac9a6694-d086-44f4-b7f5-4cbb6fb62821)

![Diagram](https://github.com/user-attachments/assets/65d54ccd-4a9c-4e1e-8e5e-a0d018c87817)

Pink = generator - Yellow = EGS board
![300B](https://github.com/user-attachments/assets/f6abea5d-960c-43b1-8391-2fd42699885a)

300B (5V 1.1A) with 0.1mH 962uF and ƒ 500Hz
<img width="1283" alt="300B-QA-0.1mH-962uF" src="https://github.com/user-attachments/assets/c9e9bde9-bf24-4840-81dc-0f2df1cf76d9" />

300B (5V 1.1A) with 3.3mH 260uF and ƒ 170Hz
<img width="1279" alt="300B-QA-3.3mH-260uF" src="https://github.com/user-attachments/assets/3a844ac6-59e6-4d95-9d79-ff05fc5693a9" />

