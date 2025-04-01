# Module 2 - Input/Output in the RVfpga SoC

In this second module, students will learn how to use and extend the input/output (I/O) system of RVfpga to enable the RISC-V processor to interact with peripheral devices. Since the SoC used in the course is programmed in Verilog, we will begin with an introduction to this hardware description language (Topic 1).

In Topic 2 of this second module, we will first describe the main features of a general-purpose I/O system and the one used in the RVfpga system. Then, a simplified theoretical version of a generic GPIO controller will be presented. Finally, we will focus on the GPIO controller used in SweRVolfX: first, its high-level specification will be analyzed and basic exercises will be presented, followed by a deeper look into its low-level implementation and more advanced exercises where new GPIO-based peripherals will be added.

Next, following a similar structure, Topics 3 and 4 will provide a detailed study of 7-segment displays and counters, including both basic and advanced exercises where these devices will be modified to include new functionalities.

In Topic 5, we will introduce interrupt-based I/O and develop programs that use this mechanism, comparing them to similar polling-based programs.

Finally, in Topic 6, serial buses will be introduced, and we will work with the accelerometer available on the board.
