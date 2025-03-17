# LVPS DC-AC Regulated Inverter EGS 1.0.3

DC-AC 4-8V AC power supply for heating audio tubes.

This DC-AC regulated power supply board is used to power the audio tube heater with AC voltage. The voltage is adjustable from 4V to 8V via a potentiometer on the PCB.

The LVPS DC-AC Regulated Inverter EGS board is based on the use of the EGS002 module. It is a control board for pure sine wave inverters, primarily used in DC-AC power conversion systems.

It integrates the EG8010 chipset for generating pure sine waves with digital control and dead-time management. The module supports fixed frequencies of 50Hz and 60Hz, as well as adjustable frequencies ranging from 0 to 400Hz (need mods on the EGS002 module).

It offers protections against overvoltage, undervoltage, overcurrent, and overheating. The board is also equipped with an independent fuse to protect the EGS002 module (5V and 12V). To avoid damaging the tubes, there is a 3 second soft start mode by default.

The LVPS DC-AC Regulated Inverter EGS board operates up to about 4A with an input voltage of 15Vdc or 24Vdc. It can be configured with different inductors in the output filter depending on the types of audio tubes to be heated and the needed power.

The board has an output on 3 pins with an optional middle point (2 resistors to be soldered under the PCB). This avoids soldering the cathode resistors onto the tube socket.

<b>Specifications:</b>

DC voltage input: 15-24V<br>
AC 50Hz output: 4V-8V<br>
SNR: 58dB-64dB (depend of the type of coil)<br>
Distorsion: < 1%<br>
PCB size: 110 x 44 mm, Height: 42 mm (with the EGS002 board)

<br><br>

Final version 1.0.3

![Image](https://github.com/user-attachments/assets/c0117173-db08-4180-b7b3-ac5c3b566903)

Prototype with an 3.3mH coil.

![EGS-3.3mH](https://github.com/user-attachments/assets/ae89ef2d-0272-4c18-8b69-7ce8ab1d3bec)

Last PCB version 1.0.3.

![3D](https://github.com/user-attachments/assets/a6120a3a-62c9-4db3-9469-7f31b0ac5dce)

![Front](https://github.com/user-attachments/assets/19bbad18-7f58-453f-9d53-71d9bfd4a7c2)

![Back](https://github.com/user-attachments/assets/8486b1d9-2e4d-49d5-8de5-5380c9e94615)

![Diagram](https://github.com/user-attachments/assets/a139dfc9-a23d-4c60-904d-09aa414f23fe)

Pink = generator - Yellow = EGS board
![300B](https://github.com/user-attachments/assets/f6abea5d-960c-43b1-8391-2fd42699885a)

300B (5V 1.1A) with 0.1mH 962uF and ƒ 500Hz
<img width="1704" alt="300B-0.1mH-962uF-1.1A-REW" src="https://github.com/user-attachments/assets/90798f62-60ff-491b-b303-c54e215a05f7" />

300B (5V 1.1A) with 3.3mH 260uF and ƒ 170Hz
<img width="1279" alt="300B-QA-3.3mH-260uF" src="https://github.com/user-attachments/assets/3a844ac6-59e6-4d95-9d79-ff05fc5693a9" />

5U4G (5V 3.1A) with 0.27mH 962uF and ƒ 320Hz
![5U4G-0.27mH-962uF-5V-3.1A-QA](https://github.com/user-attachments/assets/e5125323-d2cc-42f5-973f-fb2e9df9769d)
