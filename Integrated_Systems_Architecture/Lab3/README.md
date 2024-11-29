# Lab 3 - Performance of the VeeR EH1 core
In this lab we continue the analysis of the VeeR EH1 core.

You can follow the next steps:
1. View this video [PerformanceBenchmarkingVideo](https://www.youtube.com/watch?v=GqaDEW3W4X0) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://www.youtube.com/watch?v=DXB7jl1iGq8), or you can enable the subtitles in the video in Spanish). You can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing). The video illustrates the following items:
    * How to measure performance in the RVfpga System (description of the VeeR EH1 Performance Counters is at time 0:10 and an example running on RVfpga-ViDBo is at time 2:14).
    * How to extend the VeeR EH1 processor with new instructions and how we can improve its peformance using them (a description of how to add new instructions to VeeR EH1 is at time 6:29 and an example running on RVfpga-ViDBo is at time 14:49).
    * How to run the CoreMark benchmark in the RVfpga System (at time 24:18).

2. Perform the following exercises.


## Exercise 1
*→ View this [video](https://www.youtube.com/watch?v=GqaDEW3W4X0) at time 0:10 for the description of VeeR EH1 Performance Counters and at time 2:14 to see an example running on RVfpga-ViDBo.*

Download from the following link the program used for this example: [HwCounters_Example.zip](https://drive.google.com/file/d/1OEnGku9_uccNFXdFMkXveIQuQzTUIfsJ/view?usp=sharing)

Do the following steps:
   * Open the downloaded project in VSCode.
   * Run the program in RVfpga-ViDBo.
   * Analyze the results. Are they what you’d expect from the analyzed code?

**TASK:**
Measure other events in the Hardware Counters for the provided program. For this purpose, you must change in file ```Test.c``` the configuration of the events to be measured with function ```pspPerformanceCounterSet```. Note that the different events (shown in the table in the video) can be configured using the macros defined in WD’s PSP file:

```/home/rvfpga/.platformio/packages/framework-wd-riscv-sdk/psp/api_inc/psp_performance_monitor_eh1.h```

For example, to measure the number of I$ misses instead of the number of branch prediction misses, you must substitute in file ```Test.c``` line: 

```pspPerformanceCounterSet(D_PSP_COUNTER3, E_BRANCHES_MISPREDICTED);```

for line: 

```pspPerformanceCounterSet(D_PSP_COUNTER3, E_I_CACHE_MISSES);```

Are the results for I$ misses reasonable?


## Exercise 2
Measure the CPI using the Performance Counters for the program provided below, that was used in a previous lab, with all VeeR EH1 core features enabled. Compare the result with the one you obtained in the previous lab for the same situation.

Then, test the program both in the RVfpga-ViDBo simulator.

We next copy the code that you must use, which is slightly modified with respect to the one used in the previous lab. Use the project downloaded in the previous exercise (HwCounters_Example) and placed in your home directory, and simply substitute the program for the one provided below. Note that, in this program and unlike the previous lab, we repeat the same code a high number of times, in order to reduce undesired effects such as I$ misses. You can calculate the average CPI by dividing the total number of cycles by the total number of instructions executed.

```
   .globl Test_Assembly
   
   .section .midccm
   Entrada: .space 40
   Filtro: .space 12
   Salida: .space 32
   
   .text
   
   Test_Assembly:
   li t2, 0x0 # Enable all VeeR EH1 features
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

   .end
```



