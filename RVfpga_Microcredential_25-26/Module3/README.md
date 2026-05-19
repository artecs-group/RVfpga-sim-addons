## General Contents

In this module, students will explore the internal microarchitecture of the VeeR EH1 (and EL2 in less detail) RISC-V processor. The activities focus on understanding pipelined execution, superscalar architectures, performance evaluation, and memory hierarchy concepts.

Students will analyze instruction execution using RVfpga visualization and tracing tools, evaluate processor performance through hardware counters and benchmarks, and study how architectural features such as branch prediction, caches, and custom instructions affect performance. The module also includes practical exercises extending the processor with floating-point hardware support and comparing hardware versus software execution of floating-point algorithms.

---

## Previous work to complete between June 1 and 11:

1. Review of the simple 5-stages pipelined processor:

   * You can look at Chapter 7 (Microarchitecture) of the [H&H book](https://www.amazon.es/Digital-Design-Computer-Architecture-RISC-V/dp/0128200642), which explains the basic concepts of different RISCV-based processor implementations.
   * Look at the following slides, which describe the processor from the previous textbook: [Module7_FC2-Spanish](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2tema7-imprimible.pdf) or [Module7_FC2-English](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2module7.pdf).

2. Watch this video, which describes the VeeR EH1 microarchitecture in detail: [VeeReh1Video](https://youtu.be/xVnB6OM00cE?si=0HW333O-oPOXUDZG) (the video is in Spanish, but you can watch an AI-translated-to-English version of the video here [VeeReh1EnglishVideo](https://www.youtube.com/watch?v=Ow_0l47xqV4)). Take into account that the RVfpga-Pipeline simulator used in the video is an older version than the one you will use in this course. You can download the slides used in the video [here](https://drive.google.com/file/d/1rSlwCzcHD4F_S4YFLCFn3L0VNXH_sv7L/view?usp=drive_link).

3. Perform the following guided example and solved exercise, which analyze the VeeR EH1 microarchitecture analyzed in the previous item.

---

# Guided Example - Use of RVfpga-Pipeline

1. Open VSCode and load the project folder located at `/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects/ProyectoP2`. To do this, go to `File → Open Folder`, navigate to `/home/rvfpga/Simuladores_EC_24-25/RVfpga/Projects`, select the `ProyectoP2` directory, and click `Open`.

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/OpenFolder.png" width=80% height=80%>
</p>

2. In VSCode, open the editor to view the assembly source code of the project. The file is named `Programa.S` and is located inside the `src` directory of the project.

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/ProgramS.png" width=80% height=80%>
</p>

3. Open the `platformio.ini` file and update the path to the RVfpga-Pipeline simulator as follows:

```ini
board_debug.verilator.binary = /home/rvfpga/Simuladores_EC_24-25/RVfpga/verilatorSIM_Pipeline/OriginalBinaries/RVfpga-Pipeline_Ubuntu
```

4. Open the PlatformIO tab in VSCode and click on the task `RVfpga-ViDBo/Pipeline`. The simulator will then start executing the program.

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/RVfpgaVidboPipeline.png" width=40% height=40%>
</p>

5. The simulator stops when the instruction `and zero, t4, t5` reaches the Decode stage. This instruction is simply used as a breakpoint. Continue the execution cycle by cycle using the `+1 Cycle` button and observe how instructions flow through the VeeR EH1 pipeline.

<p align="center">
  <img src="https://github.com/user-attachments/assets/bbb5d509-ec76-4cb0-a777-78c8cb27a0b5" width="1000" />
</p>

6. The following figure shows a simplified version of the VeeR EH1 microarchitecture, useful for understanding the simulator signals.

<p align="center">
  <img src="../../Computer_Organization/Lab2/Images/VeeReh1.png" width="90%" />
</p>

7. In most cases, the analyzed code is located inside a loop. It is important to analyze iterations after the first or second one because structures such as the branch predictor or the instruction cache are not yet trained during the first executions.

The following figure shows the simulator while instructions from the third, fourth, and fifth iterations are being executed:

<p align="center">
  <img src="https://github.com/user-attachments/assets/216785a3-6655-4086-b182-7b060798baf1" width="1000" />
</p>

8. Analyze the previous figure:

- **WRITE-BACK stage**
  - *Way-0*: Instruction `mul t0, t3, t4` (3rd iteration) writes its result to the Register File.
  - *Way-1*: Due to a structural hazard between consecutive `mul` instructions, a bubble is inserted.

- **COMMIT stage**
  - *Way-0*: Instruction `mul t1, t5, t6` propagates the multiplication result.
  - *Way-1*: Instruction `addi t2, t2, -1` propagates the updated loop counter.

- **EX3/DC3/M3 stage**
  - *Way-0*: Instruction `bne t2, zero, REPEAT`.
  - *Way-1*: Instruction `mul t0, t3, t4` computes the multiplication result.

- **EX2/DC2/M2 stage**
  - *Way-0*: Instruction `mul t1, t5, t6`.
  - *Way-1*: Instruction `addi t2, t2, -1`.

- **EX1/DC1/M1 stage**
  - *Way-0*: Instruction `bne t2, zero, REPEAT`.
  - *Way-1*: Instruction `mul t0, t3, t4`.

- **DECODE stage**
  - *Way-0*: Instruction `mul t1, t5, t6`.
  - *Way-1*: Instruction `addi t2, t2, -1`.

9. To stop the simulator, simply close the simulation window.

---

# Exercise 4 - Guided Exercise in RVfpga-Pipeline

The following video shows the demo presented in class on how to solve this exercise: [Exercise4Demo](https://youtu.be/hqxG4cUnDfs).

Consider the RISC-V VeeR EH1 processor. The processor has all configurable features enabled (pipelined execution, superscalar execution, Gshare branch predictor, etc.), except for the Secondary ALU.

The following program is executed on this processor:

```assembly
.globl main

.section .midccm
D: .space 16

.text
main:

li t2, 0x080
csrrs t1, 0x7F9, t2

la t0, D

li t1, 0x2
sw t1, (t0)

li t1, 0x4
sw t1, 4(t0)

li t1, 0x3
sw t1, 8(t0)

li t1, 0x5
sw t1, 12(t0)

li s1, 4
mv s2, zero

and zero,t4,t5

for:
   slli t3 ,s2 ,2
   add t2 ,t0 ,t3
   lw s3 , 0(t2)
   lw s4 , 4(t2)
   add s3 ,s3 ,s4
   sw s3 , 0(t2)
   addi s2 ,s2 ,1
   bne s2,s1,for
end:

REPEAT:
   beq zero, zero, REPEAT
```

Answer the following questions about the `for` loop both theoretically and using the RVfpga-Pipeline simulator:

a. Draw the pipeline diagram for the third iteration of the loop.

b. Identify the hazards that occur and explain how this processor handles them.

c. Calculate the CPI (Cycles Per Instruction) of the loop.

---

## Partial Solution

### Pipeline diagram

The following figures show different moments during the execution of the third iteration of the loop.

**First cycle of the third iteration**

<p align="center">
  <img src="https://github.com/user-attachments/assets/b2a0ea7c-952b-4d82-a486-45ee9c7da63e" width="1000" />
</p>

**Sixth cycle of the third iteration**

<p align="center">
  <img src="https://github.com/user-attachments/assets/8c16616c-efac-4397-a3be-e6304e5e2b8c" width="1000" />
</p>

**Ninth cycle of the third iteration**

<p align="center">
  <img src="https://github.com/user-attachments/assets/2120c9d9-23df-4893-a6f3-aa00e8d43ad9" width="1000" />
</p>

**Pipeline diagram**

<p align="center">
  <img src="https://github.com/user-attachments/assets/fb48bdbf-5e2b-4c80-b4e2-cb5c5c9e3398" width="600" />
</p>

---

## Hazard analysis

The following figure highlights the dependencies appearing in the loop:

<img width="259" height="271" src="https://github.com/user-attachments/assets/77b0ad9d-11c3-4234-a2b2-71582294b623" />

Main hazards:

- Data hazards are mainly resolved through forwarding.
- The second `lw` instruction suffers a structural hazard and must stall one cycle.
- The dependency between the second `lw` and the `add` instruction requires two stalls.
- The control hazard in the `bne` instruction is resolved using the Gshare branch predictor.

### Example: forwarding between `slli` and `add`

<p align="center">
  <img src="https://github.com/user-attachments/assets/be8d9641-db0e-4c1f-a1af-71e84ca86b1a" width="500" />
</p>

### Example: forwarding between `add` and first `lw`

<p align="center">
  <img src="https://github.com/user-attachments/assets/4f95d2ea-cf39-400b-9bcc-747db3fcb842" width="500" />
</p>

### Example: structural hazard between the two `lw`

<p align="center">
  <img src="https://github.com/user-attachments/assets/a74c2ec0-9609-4fc0-b1f1-274741edb75f" width="700" />
</p>

### Example: hazard between the `lw` instructions and the `add`

<p align="center">
  <img src="https://github.com/user-attachments/assets/1220b417-52b2-4bc9-845a-5baf7d1de3f9" width="1000" />
</p>

### Example: forwarding after the `addi`

<p align="center">
  <img src="https://github.com/user-attachments/assets/82056af0-94a3-46ac-b1ea-d07dc18dfa2f" width="700" />
</p>

---

## CPI calculation

To calculate the CPI of the loop, simulate until the first instruction of the loop reaches the Decode stage in two consecutive iterations. Then, subtract the cycle numbers and divide the result by the number of instructions in the loop.

From the screenshots shown previously:

```text
CPI = (31 - 23) / 8 = 1
```


