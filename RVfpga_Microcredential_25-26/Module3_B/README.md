# Module 3 - The VeeR EH1 core: Benchmarking, Performance Counters and ISA Extensions

## Previous work to complete between June 15 and 18:

### 1. Review of the memory hierarchy:

Look at Chapter 8 (Memory Systems) of the H&H book.

### 2. Watch the following video: 

[PerformanceBenchmarkingVideo](https://youtu.be/GqaDEW3W4X0?si=yf1rObPveS-RB-We&t=10) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://youtu.be/DXB7jl1iGq8?si=GODI7vlY9WCXIMny&t=10)).

  - From time 0:0 to time 6:25, the video shows a description of the VeeR Performance Counters and an example using RVfpga-ViDBo.
  - Then, from time 6:29 to time 24:18, the video describes how to extend the VeeR EH1 processor with new instructions and how we can improve its peformance using them.
  - Finally, from time 24:18 to the end, the video describes how to run the CoreMark benchmark on the RVfpga SoC.


### 3. Hw Counters example:

Test on the board the exercise shown in the video from time 0:0 to time 6:25. Do the following steps:
   * Download the following project [HwCounters](https://drive.google.com/file/d/1OEnGku9_uccNFXdFMkXveIQuQzTUIfsJ/view?usp=sharing), unzip it and and move it into folder ```/home/rvfpga/RVfpga_MasterUCLM/Projects```. Open the project in VSCode. Note that this is the same program demonstrated in the video above, where the RVfpga-ViDBo simulator was used.
   * Run the program in RVfpga-ViDBo or on the board (if you have it).
      * RVfpga-Nexys (FPGA board): Set the path for the bitstream in the ```platformio.ini``` file as follows: ```board_build.bitstream_file = /home/rvfpga/RVfpga_MasterUCLM/Projects/src/rvfpganexys.bit```
      * RVfpga-ViDBo (simulator): Set the path for the simulator in the ```platformio.ini``` file as follows: ```board_debug.verilator.binary = /home/rvfpga/RVfpga_MasterUCLM/Projects/verilatorSIM_ViDBo/OriginalBinaries/RVfpga-ViDBo_Ubuntu22```
   * Analyze the results displayed in the serial console. Are they what you’d expect from the analyzed code?

---

## To complete in the 4th Session (Friday, June 12):

## Exercise 1 (mandatory)
In the VeeR EH1 processor, the following code is to be executed. Note that this is the same code used in Exercise 1 of the previous session.

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

Analyze the code in RISC-V assembly. Note that, with respect to the code from the previous lab, we have added an extra loop (```REPEAT```) that repeats the nested loops (```loop_n``` and ```loop_k```) a high number of times, in order to be able to obtain an accurate value for the cycles and instructions measured by the performance counters. Take this into account in your calculations.

Then, test performance of the nested loops for different configurations of the VeeR EH1 core as specified next, and compare and explain the results that you obtain. Use the project you downloaded before (*HwCounters*) and simply replace the text in file ```Test_Assembly.S``` for the one provided in this exercise in RISC-V assembly. Test execution on the Nexys A7 board and on the RVfpga-ViDBo simulator.

- Calculate the CPI for the nested loops when the program executes on a VeeR EH1 processor with superscalar execution, the Secondary ALU, and the Gshare branch predictor disabled (this is the default configuration used in the program provided above).
```
li t2, 0x488
csrrs t1, 0x7F9, t2
```

- Repeat the analysis from the previous item, now enabling superscalar execution. Replace the two instructions for these ones:
```
li t2, 0x088
csrrs t1, 0x7F9, t2
```

- Repeat the analysis from the previous item, now enabling the Gshare predictor. Replace the two instructions for these ones:
```
li t2, 0x080
csrrs t1, 0x7F9, t2
```

- Repeat the analysis with all features enabled. Replace the two instructions for these ones:
```
li t2, 0x0
csrrs t1, 0x7F9, t2
```

- Reorder the code of the ```loop_k``` loop to improve performance, and calculate the CPI for the configuration of the previous item (all VeeR EH1 features enabled). Explain the reason for the improvement achieved by the reordering, focusing on the reduction of the impact of the data/structural/control hazards.

- Compare the results obtained with the performance counters with the results obtained in the previous lab using the RVfpga-Pipeline simulator.



## Exercise 2 (mandatory)
Complete the exercises proposed in the following link: [Benchmarking and Memory System](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Integrated_Systems_Architecture/Lab6). Most of the exercises are already solved, so your task is to follow the steps, ananlyze and explain them, and justify the results you obtain.


## Exercise 3 (optional) - Adding new instructions in the VeeR EH1 core:
Use primarily the instructions provided in the video mentioned above and also, if you need more information, the document for Lab 18 of RVfpga (we recommend you to use the document provided both for the EH1 core and for the EL2 core, as some instructions are more up-to-date in the latter document). Do the tests both in RVfpga-ViDBo and on the board:

- Integrate an FPU (Floating Point Unit) into the VeeR EH1 core, with support for addition, multiplication, and division. You can use the sources provided in the following link, which already provide the modified files: [SoC_Sources](https://drive.google.com/file/d/1199soZSgC8ZiqvnQjMRLNSkZAyRviOb5/view?usp=drive_link). Explain the differences versus the original SoC. Obtain the bitstream (in this case you can generate your own bitstream or use the one provided here: [SoC_FPU](https://drive.google.com/file/d/1DwSW22Nk8Ef6UOMWIHgC7AB96AzB-yJI/view?usp=drive_link)), as well as the simulator binary (in this case follow the instructions explained in the video to compile the simulator).
	
- Test the implementation using a real algorithm. Use the Dot Product program provided in the following link: [DotProduct](https://drive.google.com/file/d/1FxCZzNDfhHamieTfrMSGTSZLJr-9cMYl/view?usp=drive_link)). First, understand the program, both the C and the assembly file. Then, execute the program both in simulation and on the board, and confirm that the results obtained for the dot product are correct. Finally, compare the performance obtained when executing the FP instructions using software emulation vs. hardware implementation.
       
	   
## Exercise 4 (optional) - Other RISC-V cores:
In the following directory you can find some examples of other open RISC-V cores: [OtherRiscvCores](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/RVfpga_Microcredential/Module3/OtherRiscvCores)

