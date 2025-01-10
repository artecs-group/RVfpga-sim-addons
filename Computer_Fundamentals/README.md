# Computer Fundamentals

This is a second-year course in the Computer Science degree program offered at UCM. You can see the contents of this course at [Computer Organization UCM](http://web.fdi.ucm.es/UCMFiles/pdf/FICHAS_DOCENTES/2024/8704.pdf).

The theoretical part of the course provides an in-depth analysis of the RISC-V architecture and assembly programming, along with single-cycle, multi-cycle, and pipelined processors as described in the Harris&Harris book. Exercises and labs are included to reinforce and deepen understanding of these topics. All these materials are provided through an external webpage, both in Spanish [FC2](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2.html) and in English [FC2](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2-en.html).

In this course, some exercises and labs are not only solved on paper but are also analyzed through simulations using [Ripes](https://github.com/mortbopet/Ripes). Students use their own laptops or request one from the school, and they install and run Ripes natively on their devices. Exercises and labs are mainly divided in two parts, for which details are given below:

- [RISC-V Architecture and Assembly Language](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Fundamentals/README.md#risc-v-architecture-and-assembly-language): Related with modules 2-4 of the course.
- [RISC-V Single/Multi-Cycle and Pipelined Processors](https://github.com/artecs-group/RVfpga-sim-addons/blob/main/Computer_Fundamentals/README.md#risc-v-singlemulti-cycle-and-pipelined-processors): Related with modules 5-7 of the course.

*NOTE: This course will be conducted during the second semester of the 2024-2025 academic year (February 2025 to May 2025). During this time, the course materials will continue to be refined and enhanced.*

*NOTE: In case you want to obtain more information about this course (such as the slides, the exercises sheets, the solutions for the labs, etc.), you can contact ```dani02@ucm.es```*

---

## RISC-V Architecture and Assembly Language

### Installation

1. Install Ripes: Follow the instructions provided at this link: [RipesInstallation](https://github.com/mortbopet/Ripes?tab=readme-ov-file#downloading--installation). Note that you could build the simulator yourself, but it is easier to use precompiled binaries. Specifically, use the latest version (v2.2.6) of the precompiled binaries available [here](https://github.com/mortbopet/Ripes/releases). Note that you must download the binaries that correspond to your Operating System.

2. Install the RISC-V Toolchain:
    - Follow the instructions provided at this link: [ToolchainInstallation](https://github.com/mortbopet/Ripes/blob/master/docs/c_programming.md#toolchain). Note that you could build the toolchain yourself, but again it is easier to use precompiled binaries. Use the *sifive/freedom-tools* precompiled version, available [here](https://github.com/sifive/freedom-tools/releases/tag/v2020.04.0-Toolchain.Only). Note that you must download the binaries that correspond to your Operating System.
    - Register the toolchain in Ripes following the instructions provided at this link: [ToolchainRegistration](https://github.com/mortbopet/Ripes/blob/master/docs/c_programming.md#toolchain-registration).

3. Read the information provided at this link: [Introduction to Ripes](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md). Specifically, read the following sections:
    - [Editor](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md#the-editor-tab)  
    - [Simulation Controls](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md#controlling-the-simulator)  
    - [Memory Viewer](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md#the-memory-tab)  

### Basic Use

1. Start the simulator in your device.

2. Environment:
    - On the left side you can see the different windows that can be displayed: Editor, Processor, Cache, Memory, I/O.
    - Depending on the selected window, the view will change. In the following figure we see the Editor window, in which you can enter code in Assembler or C in the left window, the compiled/assembled code will be displayed in the middle window, and it shows the registers of the simulated processor on the right.

<p align="center">
  <img src="Images/EditorFigure.png" width=80% height=80%>
</p>

#### Configuration

3. Before simulating the program, select the Single Cycle processor, enable the M extension and disable the C extension:

<p align="center">
  <img src="Images/SingleCycle.png" width=80% height=80%>
</p>

#### RISC-V Assembly Program

4. To simulate a RISC-V assembly program, we simply type or copy it into the window on the left. For example, in the following figure you can see the program provided next (you can copy the code into your simulator and test it). On the right you can see the disassembled version.

<p align="center">
  <img src="Images/Ex1.png" width=80% height=80%>
</p>

```
  .global main
  
  .equ n ,10
  
  .data
  v: .word 12 ,1 , -2 ,15 , -8 ,4 , -31 ,8 ,8 ,25
  
  .text
  main:
    li s1 , n
    mv s2 , zero # s2 es i
    for:
      beq s2,s1,fin
      la t1 , v 		# t1= @base de v
      slli t3 ,s2 ,2 	# i*4
      add t2 ,t1 ,t3 	# t2= @efectiva de v[i]
      lw s3 ,0( t2)
      addi s3 ,s3 ,-1
      sw s3 ,0( t2)
      addi s2 ,s2 ,1 	# i=i+1
      j for
    fin:
    j fin
```

5. The top menu allows us to control the simulation. By hovering the mouse over each button we are informed about its functionality.

<p align="center">
  <img src="Images/Menu.png" width=40% height=40%>
</p>

6. We can execute the code step by step:
    - The “minor” and “major” arrows in the top menu allow us to go forward or backward instruction by instruction.
    - The current instruction is shown highlighted in red.

<p align="center">
  <img src="Images/Execution.png" width=40% height=40%>
</p>

7. Disassembled/binary code window and registers window:
    - The registers will be updated as we progress through the program.
    - When a register is updated, it will be highlighted in yellow.
    - The middle window shows the disassembled code. Note that, unlike the source, it only includes instructions (not pseudo-instructions).

<p align="center">
  <img src="Images/Registers.png" width=90% height=90%>
</p>

8. The Memory window allows us to visualize the different memory sections. The figure shows the .text section, which includes the text of the code. At the bottom you must select, from the “Go to section” menu, the .text section. You can check that the hexadecimal code corresponds to the program instructions in the Editor.

<p align="center">
  <img src="Images/Memory.png" width=90% height=90%>
</p>

9. At the bottom, in the “Go to section” menu, we can switch to the .data section. You can check that the data correspond to the vector components in the Editor.

<p align="center">
  <img src="Images/DataSection.png" width=90% height=90%>
</p>

#### C Program

10. To simulate a C program, write or copy it into the left window, marking "Input Type" as C language. For example, the next C program can be seen in the following figure (you can test it in your simulator):

<p align="center">
  <img src="Images/Editor.png" width=90% height=90%>
</p>

```
int main(void)
{
   int i,result,num=7;

   if (num > 1){
      result = num;
      for (i=num-1;i>1;i--)
      result = result*i;
   }
   else
      result=1;

   printf("Factorial = %d",result);

   while(1);
}
```

11. Next, compile the program by clicking on the hammer icon. If the program is correct, the disassembled version will appear in the central window:

<p align="center">
  <img src="Images/Martillo.png" width=90% height=90%>
</p>

12. Run the program by clicking the "Fast Execution" button. The result of the factorial calculation will appear in the console:

<p align="center">
  <img src="Images/Execution.png" width=70% height=70%>
</p>

### Exercises about RISC-V Architecture and Assembly
We next show the solution for some of the exercises proposed in Module 3 ([ExercisesModule3](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2problems3.pdf)).

#### Exercise 1


### Labs about RISC-V Architecture and Assembly
We next show the labs proposed in the course.

#### Lab 1

#### Lab 2

#### Lab 3

#### Lab 4

#### Lab from Computer Organization

Resolve Exercises 1-4 proposed in the UCM Computer Organization course: [Ex1-4](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab1#exercise-1).


---


## RISC-V Single/Multi-Cycle and Pipelined Processors


