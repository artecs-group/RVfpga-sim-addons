# Lab 3 - Performance counters on the VeeR EH1 core
In this lab we continue the analysis of the VeeR EH1 core, using the performance counters and executing the CoreMark benchmark. The exercises proposed can be performed both in RVfpga-ViDBo and on the FPGA board.

Follow the next steps:

1. Do the task that corresponds to the tool that you are using:
	- If you are working with RVfpga-Nexys (FPGA board): Complete the following document [RVfpgaNexys_InitialTests](https://drive.google.com/file/d/1OtZvekekP1e0v28yUr1u0TI2xWcc8VFF/view?usp=sharing)
	- If you are working with RVfpga-ViDBo (simulator): Perform the guided example for RVfpga-ViDBo, provided in section *Introduction - Simulation of the RVfpga SoC in RVfpga-ViDBo* at [SimulationInRVfpgaViDBo](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization/Lab4/README.md#introduction---simulation-of-the-rvfpga-soc-in-rvfpga-vidbo). Note however that this example is hosted on a separate webpage. Once you finish, make sure to return here and continue with item 3.

2. View, from time 0:0 to time 6:25, this video [PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=10) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=10), you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://youtu.be/d5-0sNLW7wg?si=6P5wM8ruumOQuSnD&t=10) or you can enable the subtitles in the video in Spanish) (you can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing)). The video shows a description of the VeeR Performance Counters and an example using RVfpga-ViDBo.

3. Perform the following exercises.

4. Finally, if you want to continue practicing after completing the proposed exercises, you can find more complex exercises in [RVfpga](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) labs 11 to 18.


## Exercise 1
Do the following steps:
   * Download the following project [HwCounters](https://drive.google.com/file/d/1OEnGku9_uccNFXdFMkXveIQuQzTUIfsJ/view?usp=sharing) and open it in VSCode.
   * Run the program in RVfpga-ViDBo and on the board (if you have it).
      * RVfpga-Nexys (FPGA board): Set the path for the bitstream in the ```platformio.ini``` file as follows: ```board_build.bitstream_file = /home/rvfpga/Simuladores_EC_24-25/RVfpga/src/rvfpganexys.bit```
      * RVfpga-ViDBo (simulator): Set the path for the simulator in the ```platformio.ini``` file as follows: ```board_debug.verilator.binary = /home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_ViDBo/OriginalBinaries/RVfpga-ViDBo_Ubuntu22```

   * Analyze the results displayed in the serial console. Are they what you’d expect from the analyzed code?

**NOTE**
To view the serial console on the board, right after the program starts to run and stops at the ```main``` function, open the serial monitor, by clicking on the plug button available on the bottom of VS Code:

![image](https://github.com/user-attachments/assets/0afb7bda-409d-434a-aab6-41915c44f37a)


**TASK:**
Measure other events in the Hardware Counters for the provided program. For this purpose, you must change in file ```Test.c``` the configuration of the events to be measured with function ```pspPerformanceCounterSet```. Note that the different events (shown in the table in the video) can be configured using the macros defined in WD’s PSP file:

```/home/rvfpga/.platformio/packages/framework-wd-riscv-sdk/psp/api_inc/psp_performance_monitor_eh1.h```

For example, to measure the number of I$ misses instead of the number of branch prediction misses, you must substitute in file ```Test.c``` line: 

```pspPerformanceCounterSet(D_PSP_COUNTER3, E_BRANCHES_MISPREDICTED);```

for line: 

```pspPerformanceCounterSet(D_PSP_COUNTER3, E_I_CACHE_MISSES);```

Are the results for I$ misses reasonable?

**TASK:**
Propose additional RISC-V Assembly codes that evaluate different scenarios and measure the results using appropriate performance counters (such as instruction cache misses, branch misprediction rate, etc.).


## Exercise 2
In the VeeR EH1 processor, the following code is to be executed. Note that this is the same code used in [Exercise 3 of Lab 2 in RVfpgaPipeline](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2/VeeR#exercise-3):

```
for ( n = 0; n < 8; n ++ ) {
    for ( k = 0; k < 3; k ++ ) {
    Salida[n] += Filtro[k] * Entrada[n + k];
    }
}
```

To achieve the highest performance in executing this program on the VeeR EH1 processor, the following assembly implementation is decided:

```
.globl Test_Assembly

.section .midccm
Entrada: .space 40
Filtro: .space 12
Salida: .space 32

.text
Test_Assembly:

li t2, 0x488 # Disable Superscalar Exec, Sec. ALUs and Branch Pred.
csrrs t1, 0x7F9, t2

la t0, Entrada
li t1, 0x1   				 
sw t1, (t0)   			 
li t1, 0x3   				 
sw t1, 4(t0)   			 
li t1, 0x5   				 
sw t1, 8(t0)   			 
li t1, 0x7   				 
sw t1, 12(t0)   			 
li t1, 0x9   				 
sw t1, 16(t0)   			 
li t1, 0x1   				 
sw t1, 20(t0)   			 
li t1, 0x3   				 
sw t1, 24(t0)   			 
li t1, 0x5   				 
sw t1, 28(t0)   			 
li t1, 0x7   				 
sw t1, 32(t0)   			 
li t1, 0x9   				 
sw t1, 36(t0)   			 

la t0, Filtro
li t1, 0x2   				 
sw t1, (t0)   			 
li t1, 0x3   				 
sw t1, 4(t0)   			 
li t1, 0x4   				 
sw t1, 8(t0)   			 

la t0, Salida
li t1, 0   				 
sw t1, (t0)   			 
li t1, 0   				 
sw t1, 4(t0)   			 
li t1, 0   				 
sw t1, 8(t0)   			 
li t1, 0   				 
sw t1, 12(t0)   			 
li t1, 0   				 
sw t1, 16(t0)   			 
li t1, 0   				 
sw t1, 20(t0)   			 
li t1, 0   				 
sw t1, 24(t0)   			 
li t1, 0   				 
sw t1, 28(t0)   			 

la   a3 , Entrada
la   a4 , Filtro
la   a5 , Salida

li   a2, 0
li   t1, 3
li   a1, 0
li   t0, 8

nop
nop
nop
nop

and zero, t4, t5

li t2, 0x0
add a6, a6, 0x240

REPEAT:
	loop_n :
	addi a2 , x0 , 0
		loop_k :
	    	lw t3 , 0( a3)
	    	lw t4 , 0( a4)
	    	mul t6 , t3 , t4
	    	lw t5 , 0( a5)
	    	add t5 , t6 , t5
	    	sw t5 , 0( a5)
	    	addi a3 , a3 , 4
	    	addi a4 , a4 , 4
	    	addi a2 , a2 , 1
	    	blt a2 , t1 , loop_k
	addi a5 , a5 , 4
	addi a3 , a3 , -8
	addi a4 , a4 , -12
	addi a1 , a1 , 1
	blt a1 , t0 , loop_n
addi t2, t2, 1
bne t2, a6, REPEAT # Repeat the loop

ret
```

Analyze the code in RISC-V assembly.
- Note that in the assembly program we are initializing the arrays in the Data Scratchpad before entering the loops, element-by-element, so this needs quite a few instructions.
- Besides, note that we have added an extra loop (```REPEAT```) that repeats the nested loops (```loop_n``` and ```loop_k```) a high number of times, in order to be able to obtain an accurate value for the cycles and instructions measured by the performance counters.

Then, test performance of the nested loops for different configurations of the VeeR EH1 core as specified next, and compare and explain the results that you obtain. Use the project you downloaded in Exercise 1 (project ```HwCounters```) and simply replace the text in file ```Test_Assembly.S``` for the one provided in this exercise in RISC-V assembly. Test execution on the Nexys A7 board (the same should work on the RVfpga-ViDBo simulator).

- Calculate the CPI for the nested loops when the program executes on a VeeR EH1 processor with superscalar execution, the Secondary ALU, and the Gshare branch predictor disabled (this is the default configuration used in the program provided above).
```
li t2, 0x488
csrrs t1, 0x7F9, t2
```

- Calculate the CPI with the Secondary ALU, and the Gshare branch predictor disabled. Replace the two instructions for these ones:
```
li t2, 0x088
csrrs t1, 0x7F9, t2
```

- Calculate the CPI with the Secondary ALU disabled. Replace the two instructions for these ones:
```
li t2, 0x080
csrrs t1, 0x7F9, t2
```

- Calculate the CPI with all features enabled. Replace the two instructions for these ones:
```
li t2, 0x0
csrrs t1, 0x7F9, t2
```

- Finally, reorder the code of the ```loop_k``` loop to improve performance, and calculate the CPI for the configuration of the previous item (all VeeR EH1 features enabled). Explain the reason for the improvement achieved by the reordering, focusing on the reduction of the impact of the data/structural/control hazards.


## Exercise 3
Download the following project: [C-Assembly_Filter](https://drive.google.com/file/d/1tjkmxy05dDP707fF0TR4bMYCx_8zYlSa/view?usp=sharing). It includes the program from Exercise 2, first in C and then in RISC-V assembly language (in the latter we have removed the REPEAT loop).

Place a breakpoint at line 29 of the C file and execute the program in the RVfpga-Whisper simulator. Compare the results obtained by the C program and its translation to RISC-V assembly. Note that you can visualize the values of the Salida array in the Variables window for the program in C, and in the Memory window (address 0xf0040000) for the program in assembly.

Reorder the program in assembly language as in the last item of Exercise 2 and confirm if the results for the Salida array are still correct.


