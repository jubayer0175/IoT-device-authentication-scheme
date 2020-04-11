## IoT device authentication scheme using an SRAM device signature
**This can be an elementary introduction to hardware security. It has SRAM PUF and signature generation process along with some basic crypto such as hash (SHA-256)** 

 This repo contains the implementation of this paper: [Mahmod, Md Jubayer al, and Ujjwal Guin. "**A Robust, Low-Cost and Secure Authentication Scheme for IoT Applications.**" Cryptography 4.1 (2020): 8.](https://www.mdpi.com/2410-387X/4/1/8/htm)
 * Author: [Jubayer Mahmod](https://sites.google.com/vt.edu/jubayer/home) 
 * Bradly department of Electrical and Computer Engineering
 * Graduate student researcher
 * Date:  4/9/2019

##### Running
A simple power-up method and hamming distance is used to generate SRAM device signatures. The signature is employed in a secure authentication protocol:

![Tux, protocol](https://www.mdpi.com/cryptography/cryptography-04-00008/article_deploy/html/images/cryptography-04-00008-g002.png)
I used Arduino (mega) as ED and Pi as a gateway. During enrollment, one Arduino is used to control the power of DUT (another Arduino). DUT would need a few codes to complete the process. Load `Power_control.ino` in the power control Arduino. Run this `ID_automate_v_0.1.py` and this will tell which `.ino` needs to be loaded in the DUT. Note that you will need some circuit that can support power-on of function in DUT. I did not have much time to design a PCB, so I went with a simple relay to do that. A relay connected with power control Arduino and the relay controls the power of the DUT. 
ID_automate_v_0.1.py` has all the necessary subroutines to give you the extracted ID of the DUT. It is not a fully automatic script, so it will ask you to load some codes in the DUT (this repo has everything).

During the authentication phase run: `Gatway_v_1.py` -> this code needs to be in the Pi. The DUT is connected to the Pi using a USB cable. Careful with the COM port setting. 
##### Dependencies
Just copy the folders `./library/*`to your Arduino library directory (typically in the ./Documents/arduino/library/ in windows OS)

******************************************************************************
 Copyright (C) 2019 by **Jubayer Mahmod- Electricla and Computer Engineering, Auburn University, AL 36830, United States**.
 Redistribution, modification or use of this software in source or binary forms is permitted as long as the files maintain this copyright. Users are permitted to modify this and use it to learn about the field of embedded system security. Jubayer Mahmod and Auburn University are not liable for any misuse of this material. 
 *****************************************************************************



