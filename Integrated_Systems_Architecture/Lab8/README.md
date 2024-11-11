# Lab 8 - The RVfpga I/O System - Low Level
This practice aims to let the students continue with the analysis of the RVfpga Input/Output System. Complete the following exercises to modify and test the 8-digit 7-Segment displays controller.

## Exercise 1
The current 8-digit 7-segment displays controller (implemented in module SevSegDisplays_Controller), can only show the 16 hexadecimal digits. Modify the 8-digit 7-segment displays controller so that it can show any combination of ON/OFF LEDs. 

Note that you only need to make changes in file /home/rvfpga/Simuladores_EC_24-25/RVfpga/src/SweRVolfSoC/Peripherals/SystemController/swervolf_syscon.sv. Specifically, within that file, you must modify the module that handles the 7-segment displays device (SevSegDisplays_Controller).

+ You can use as a baseline this [file](https://drive.google.com/file/d/19QDLbpinb2exxjfZP2S4pQ8HS-l7iQGT/view?usp=drive_link), which is already partially completed. In that file, look for comment “/* COMPLETE THE CODE WITH THE NEW FUNCTIONALITY */” and implement the new controller at that point of the code.

+ Instead of an Enables_Reg and a Digits_Reg, the new controller needs eight 7-bit registers: Segments_Digit0 – Segments_Digit6. Each of these 8 registers is associated with each of the eight 7-segment displays. These new registers are already included in the file provided in the previous item.

+ In each of these registers, each bit indicates if the corresponding segment is ON (0) or OFF (1). Specifically, for register Segments_Digit0 (the same applies to the other seven registers), connections are as follows:

<p align="center">
  <img src="Images/7seg.png" width=60% height=60%>
</p>




## Exercise 2




