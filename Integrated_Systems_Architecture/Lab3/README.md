# Lab 3 - Performance counters and benchmark execution on the VeeR EH1 core
In this lab we continue the analysis of the VeeR EH1 core, using the performance counters and executing the CoreMark benchmark. The exercises proposed can be performed both in RVfpga-ViDBo and on the FPGA board.

Follow the next steps:

1. Start by visualizing the following parts of this video [PerformanceBenchmarkingVideo](https://www.youtube.com/watch?v=GqaDEW3W4X0) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here: [PerformanceBenchmarkingEnglishVideo](https://www.youtube.com/watch?v=DXB7jl1iGq8), you can watch an AI-translated-to-Chinese version of the video here: [PerformanceBenchmarkingChineseVideo](https://www.youtube.com/watch?v=d5-0sNLW7wg) or you can enable the subtitles in the video in Spanish) (you can download the [slides](https://drive.google.com/file/d/146nEyUkGkXn85cS15EiUM7R0Bv1nKyoT/view?usp=sharing)):
    * From time 0:10 to time 6:26 you can see a description of the VeeR Performance Counters and an example using RVfpga-ViDBo.
    * From time 24:18 to the end you can see how to run the CoreMark benchmark on the SoC using the FPGA board.

2. Then, you can perform the guided example for RVfpga-ViDBo, provided [here](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Organization/Lab4/README.md#introduction---simulation-of-the-rvfpga-soc) in this same repository. Note however that this example is hosted on a separate webpage. Once you finish, make sure to return here and continue with item 3.

3. Perform the following exercises.

4. Finally, if you want to continue practicing after completing the proposed exercises, you can find more complex exercises in [RVfpga](https://university.imgtec.com/rvfpga-el2-v3-0-english-downloads-page/) labs 11 to 18.


## Exercise 1
*→ View the above PerformanceBenchmarkingVideo from time 0:10 to time 6:29 for the description of VeeR EH1 Performance Counters and an example running on RVfpga-ViDBo.*

Download from the following link the program used for this example: [HwCounters_Example.zip](https://drive.google.com/file/d/1OEnGku9_uccNFXdFMkXveIQuQzTUIfsJ/view?usp=sharing)

Do the following steps:
   * Open the downloaded project in VSCode.
   * Run the program in RVfpga-ViDBo. If needed, set the path for the simulator in the ```platformio.ini``` file as follows:

```board_debug.verilator.binary = /home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_ViDBo/OriginalBinaries/RVfpga-ViDBo_Ubuntu22```

   * Analyze the results displayed in the UART console. Please note that the output may take some time to appear. Are they what you’d expect from the analyzed code?

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

Then, test the program both in the RVfpga-ViDBo simulator. We next copy the code that you must use, which is slightly modified with respect to the one used in the previous lab. Use the project downloaded in the previous exercise (HwCounters_Example) and placed in your home directory, and simply substitute the program for the one provided below in file ```Test_Assembly.S```. Note that, in this program and unlike the previous lab, we repeat the same code a high number of times, in order to reduce undesired effects such as I$ misses. You can calculate the average CPI by dividing the total number of cycles by the total number of instructions executed.

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



## Exercise 3
*→ View the above PerformanceBenchmarkingVideo at time 25:58 to see an example of CoreMark running on the board.*

Analyze the provided PlatformIO project for the CoreMark benchmark. You can download the sources here: [CoreMark](https://drive.google.com/file/d/1WRujundTKyU3CuQxuAvV4vfe-B04-_QB/view?usp=drive_link). 

Then, analyze the execution of the benchmark in RVfpga-ViDBo for the following two configurations: 

- Using a ```-g``` compiler optimization level. For that purpose, set the three final lines of file platformio.ini as follows:

```
build_unflags = -Wa,-march=rv32imac -march=rv32imac -Os
build_flags = -Wa,-march=rv32im -march=rv32im -g
extra_scripts = extra_script.py
```

- Using a ```-O2``` compiler optimization level. For that purpose, set the three final lines of file platformio.ini as follows:

```
build_unflags = -Wa,-march=rv32imac -march=rv32imac -Os
build_flags = -Wa,-march=rv32im -march=rv32im -O2
extra_scripts = extra_script.py
```

If needed, set the path for the simulator in the ```platformio.ini``` file as follows:

```board_debug.verilator.binary = /home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_ViDBo/OriginalBinaries/RVfpga-ViDBo_Ubuntu22```


