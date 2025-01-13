# Computer Fundamentals

This is a first-year course in the Computer Science degree program offered at UCM. You can see the contents of this course at [Computer Organization UCM](http://web.fdi.ucm.es/UCMFiles/pdf/FICHAS_DOCENTES/2024/8704.pdf).

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


### Basic Use

1. Start the simulator in your device. Read the information provided at this link: [Introduction to Ripes](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md). Specifically, read the following sections:
    - [Editor](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md#the-editor-tab)  
    - [Simulation Controls](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md#controlling-the-simulator)  
    - [Memory Viewer](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md#the-memory-tab)  

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

11. On the top menu, set the appropriate compiler arguments in ```Edit-Settings```:
    - Compiler arguments: ```-O1``` (you can select other options such as -O0, -O2, etc.)

  <p align="center">
    <img src="Images/Linker.png" width=90% height=90%>
  </p>

12. Next, compile the program by clicking on the hammer icon. If the program is correct, the disassembled version will appear in the central window:

<p align="center">
  <img src="Images/Martillo.png" width=90% height=90%>
</p>

13. Run the program by clicking the "Fast Execution" button. The result of the factorial calculation will appear in the console:

<p align="center">
  <img src="Images/Execution.png" width=70% height=70%>
</p>

### Exercises about RISC-V Architecture and Assembly
We next show the solution in Ripes for a subset of the exercises proposed in Module 3 ([ExercisesModule3](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2problems3.pdf)). The remaining exercises can also be resolved and tested by the students in Ripes.

#### Exercise 1
Write a RISC-V assembly program that implements the following code.

```
int x = 10, y = 5;
if (x >= y) {
 x = x + 2;
 y = y - 2;
}
```

Once you have completed your version of the program in assembly, compare it with the solution provided below and test the programs in Ripes. Do the following tasks (in this first exercise, we provide an example solution for these tasks, which can serve as a useful reference for completing the remaining exercises in a similar way):
- Analyze the assembled code. Pay special attention to the translation of pseudo-instructions to RISC-V instructions.
- Simulate the program in Ripes step-by-step. Test different values for ```x``` and ```y```.
- Analyze the registrs during the execution.
- Analyze the memory state at the beginning and at the end of the execution. Analyze both the ```.text``` and the ```.data``` sections.


*SOLUTION:*

```
.global main # Hace global la etiqueta " main "

.data # sección de datos iniciados
x: .word 10 # declara una variable de 32 bits de valor 10
y: .word 5

.text # sección de instrucciones
main:
    la t0,x # pseudo instrucción t0=@x
    la t1,y # pseudo instrucción t1=@y
    lw s1,0(t0) # s1 = 10
    lw s2,0(t1) # s2 =5
    blt s1,s2, fin # condición inversa s1 <s2
        addi s1,s1,2 # x=x+2
        addi s2,s2,-2 # y=y -2
    sw s1,0(t0)
    sw s2,0(t1)
fin:
j fin
```

*EXAMPLE SOLUTION FOR THE TASKS:*

**Analyze the assembled code. Pay special attention to the translation of pseudo-instructions to RISC-V instructions.**

On the right window you can see the assembled code generated by Ripes:

![image](https://github.com/user-attachments/assets/480b6ced-e66d-48b8-a87e-6cdbe836d5e4)

You can analyze the translation of each instruction. As an example, the first pseudo-instruction (```la t0,x```) is translated into two RISC-V instructions, where the first instruction (```auipc x5 0x10000```) adds the current PC (0x0) and a 32-bit value with the low 12 bits as 0 and the high 20 bits coming from the U-type immediate (0x10000), and the second instruction (```addi x5 x5 0```) changes nothing in this case. Note that ```t0``` is the alias for ```x5```. Note also that the resulting value is the address where variable x is stored in memory (0x10000000).

**Analyze the registrs during the execution.**

You can analyze the registers after each cycle. As an example, we next show the register file at the end of the ```if``` condition, which is met in this case:

![image](https://github.com/user-attachments/assets/a7f6b5e4-c0a4-4af7-b8bd-3d3743ae8918)

- x9=0xc, which is the result of adding 0x2 to the initial value of x (0xa).
- x18=0x3, which is the result of subtracting 0x2 to the initial value of y (0x5).

**Analyze the memory state at the beginning and at the end of the execution. Analyze both the ```.text``` and the ```.data``` sections.**

This is the .data section at the beginning:

![image](https://github.com/user-attachments/assets/b67fac70-b968-4c68-b098-5c779dee5679)

This is the .data section at the end:

![image](https://github.com/user-attachments/assets/92075615-a2a3-4787-85b9-34463ff5b696)

Finally, this is the .text section, that includes the assembled program in binary. You can compare it with the one shown in the Editor tab:

![image](https://github.com/user-attachments/assets/ef8e2d4a-1c9a-4376-bc03-2ef31cc9169a)


#### Exercise 2
Write a RISC-V assembly program that implements the following code. 

```
int x = 5, y = 10;
if (x >= y) {
 x = x + 2;
 y = y + 2;
}
else {
 x = x - 2;
 y = y - 2;
}
```

Once you have completed your version of the program in assembly, compare it with the solution provided below and test the programs in Ripes. Do the same tasks as in Exercise 1.

*SOLUTION:*

```
.global main

.data # sección de datos iniciados
x: .word 5
y: .word 10


.text # sección de instrucciones
main:
    la t0,x # pseudoinstrucción t0=@x
    la t1,y # pseudoinstrucción t1=@y
    lw s1,0(t0) # s1 =5
    lw s2,0(t1) # s2 =10
    blt s1,s2, else # condición inversa s1 <s2
        addi s1,s1,2 # x=x+2
        addi s2,s2,2 # y=y+2
    j fin_if
    else:
        addi s1,s1,-2 # x = x -2;
        addi s2,s2,-2 # y = y -2
    fin_if:
    sw s1,0(t0)
    sw s2,0(t1)
fin:
j fin
```


#### Exercise 6
The following program calculates the greatest common divisor of two numbers ```a``` and ```b``` according to the Euclidean algorithm. Write a RISC-V assembly program that implements the following code.

```
int a=5, b=15, gcd;
while (a  b) {
 if (a > b)
 a = a - b;
 else
 b = b - a;
}
gcd = a;
```

Once you have completed your version of the program in assembly, compare it with the solution provided below and test the programs in Ripes. Do the same tasks as in Exercise 1.

*SOLUTION:*

```
.global main

.data
a: .word 5
b: .word 15
mcd: .word 0

.text
main:
    la t1,a
    lw s1,0(t1) # s1 es a
    la t2,b
    lw s2,0(t2) # s2 es b
    while:
        beq s1,s2,fin_while
            ble s1,s2,else
                sub s1,s1,s2 # a=a-b
            j fin_if
            else:
                sub s2,s2,s1 # b=b-a
            fin_if:
        j while
    fin_while:
    la t3,mcd # t3 = @mcd
    sw s1,0(t3)
fin:
j fin
```


#### Exercise 8
The following code increments the components of a vector with 10 elements. Translate it into RISC-V assembly code. 

```
#define N 10
int V[N] = {12, 1, -2, 15, -8, 4, -31, 8, 8, 25};
for (i = 0; i < N; i++)
 V[i] = V[i] + 1;
```

Once you have completed your version of the program in assembly, compare it with the solution provided below and test the programs in Ripes. Do the same tasks as in Exercise 1.

*SOLUTION:*

```
.global main

.equ n,10

.data
v: .word 12,1,-2,15,-8,4,-31,8,8,25

.text
main:
    li s1,n # s1=n
    mv s2,zero # s2 es i
    for:
    beq s2,s1,fin
        la t1,v # t1= @base de v
        slli t3,s2,2 # i*4
        add t2,t1,t3 # t2= @efectiva de v[i]
        lw s3,0(t2)
        addi s3,s3,1
        sw s3,0(t2)
        addi s2,s2,1 # i=i+1
    j for
fin:
j fin
```


#### Exercise 9
The following code counts the number of components greater than 0 within a vector with 6 elements. Translate it into RISC-V assembly code. 

```
#define N 6
int V[N] = {14, 1, -2, 7, -8, 4};
int count = 0;
for (i = 0; i < N; i++) {
 if (V[i] > 0)
 count = count + 1;
}
```

Once you have completed your version of the program in assembly, compare it with the solution provided below and test the programs in Ripes. Do the same tasks as in Exercise 1.

*SOLUTION:*

```
.global main

.equ n,6

.data
v: .word -14,1,-2,-7,-8,4
count: .word 0

.text
main:
la t1,v # t1 tiene la dirección base de v
li t2,n # t2=n
li t3,0 # t3 es el índice
li s2,0 # s2 = count =0
for:
   bge t3,t2,fin_for
   slli t5,t3,2 # t5=i*4
   add t5,t5,t1 # @=i*4+ @b
   lw s1,0(t5) # @s1=v[i]
   li t6,0 # t6 =0
   if:
   ble s1,t6,fin_if
       addi s2,s2,1
   fin_if:
   addi t3,t3,1
   j for
fin_for:
la t1,count
sw s2,0(t1)
end:
j end
```


#### Exercise 16
Write a C and a RISC-V assembly program to implement a variant of the bubble sort algorithm. This variant sorts the elements of the vector according to the following code. 

```
do {
 swapped = false
 for (i = 0; i <= N-2; i++){
 if (V[i] > V[i+1]){
 swap( V[i], V[i+1] )
 swapped = true
 }
} while swapped
```

Once you have completed your version of the program in assembly, compare it with the solution provided below and test the programs in Ripes. Do the following tasks:
- Analyze and simulate the C program in Ripes. Test different optimization levels and compare the code generated in each case.
- Analyze and simulate the RISC-V assembly program in Ripes. Pay special attention to the RISC-V calling convention. Compare it with the program generated in C.

*SOLUTION IN C:*

```
#define N 4

int V[N]={5,2,3,1};

void main(void)
{
   int swapped=1, i;

   while(swapped){
       swapped=0;
       for (i=0; i<(N-1); i++){
           if (V[i] > V[i+1]){
               swap(&V[i], &V[i+1]);
               swapped=1;
           }
       }
   }

   while(1);

}

void swap(int *V, int *W){
   int temp;
   temp=*V;
   *V=*W;
   *W=temp;
}
```

*SOLUTION IN RISC-V ASSEMBLY:*

```
.global main
.equ n, 10

.data
V: .word 2,5,6,0,9,4,6,5,-10,-1

.text
main:
li s4,n # s1 =n
addi s4,s4,-1
do:
   mv s3,zero # s3= swapped = false
   mv s5,zero # t1=i
   for:
       bge s5,s4, fin_for
       la t2,V # t2= @base v
       slli t3,s5,2 # i*4
       add a0,t3,t2 # @i
       lw s1,0(a0) # V[i]
       addi a1,a0,4 # @i +1
       lw s2,0(a1) # V[i +1]
       if:
           ble s1,s2,fin_if
           call swap
           li s3,1 # swapped = true
       fin_if:
       addi s5,s5,1
   j for
   fin_for:
   li t4,1
beq s3,t4,do
fin:
j fin

swap:
# prologo
    addi sp,sp,-8
    sw s1,0(sp)
    sw s2,4(sp)
# cuerpo
    lw s1,0(a0)
    lw s2,0(a1)
    sw s1,0(a1)
    sw s2,0(a0)
# epílogo
    lw s1,0(sp)
    lw s2,4(sp)
    addi sp,sp,8
jr ra # también ret
```


#### Exercise 18
Given two points ```P1(x1, y1)``` and ```P2(x2, y2)```, their Chebyshev distance can be calculated with the following algorithm: 

```
int chebyshev(int x1, int y1, int x2, int y2)
{
 int d1, d2;
 d1 = abs(x1 - x2)
 d2 = abs(y1 - y2)
 if (d2 > d1)
 d1 = d2;
 return d1;
}
```

Write a RISC-V assembly function, ```chebyshev(x1,x2,y1,y2)```, which will receive the coordinates of two points P1 and P2 and will return their Chebyshev distance. This function will call another function that calculates the absolute value of a given number.

Then, program the following code and test it in Ripes. The program stores (into a vector D) the Chebyshev distances of a point P to each of the points within a vector V with N elements. P, V y D will be global variables. Vector V will contain 2N integers such that the i-th point will have coordinates (x, y) = (V[2*i], V[2*i + 1]) 

```
#define N, ...
int Px, Py; // x , y coordinates of point P
int V[2N]; //Vector with N points V=[x0,y0,x1,y1,...]
int D[N]; //Vector with N distances
void main(void)
{
int i;
for (i = 0; i < N; i++)
 D[i] = chebyshev(Px, Py, V[2*i], V[2*i + 1]);
}
```

Once you have completed your version of the program in assembly, compare it with the solution provided below and test the programs in Ripes. Do the following tasks:
- Analyze and simulate the RISC-V assembly program in Ripes. Pay special attention to the RISC-V calling convention.

*SOLUTION:*

```
.global main
.equ n,5 #nº de puntos a testear (2*n componentes)

.data
P: .word 4,5 # coordenadas x e y del punto P
V: .word 1,2,-3,4,5,9,17,-15,20,12 # Vector de N puntos V=[x0,y0,x1,y1,...]
sol: .word 0,0,0,0,0

.text
main:
mv s1,zero
li s2,n
la s3,V
for:
bge s1,s2,fin_for
la s6,P
lw a0,0(s6)
lw a1,4(s6)
slli s4,s1,1
slli s4,s4,2
add s4,s4,s3
lw a2,0(s4)
lw a3,4(s4)
call chebyshev
la s5,sol
slli s4,s1,2
add s4,s4,s5
sw a0,0(s4)
addi s1,s1,1
j for
fin_for:
j fin_for

chebyshev:
#prólogo
addi sp,sp,-12
sw s1,0(sp)
sw s2,4(sp)
sw ra,8(sp)
# cuerpo
d1:
sub s1,a0,a2 #x1 -x2
mv a0,s1
call abs
mv s1,a0
d2:
sub s2,a1,a3 #y1 -y2
mv a0,s2
call abs
mv s2,a0
if:
ble s2,s1,fin_call
mv s1,s2
fin_call:
mv a0,s1
# epílogo
lw s1,0(sp)
lw s2,4(sp)
lw ra,8(sp)
addi sp,sp,12
ret

abs:
bgez a0,pos
sub a0,zero,a0
pos:
ret
```


### Labs about RISC-V Architecture and Assembly
Students can now resolve the exercises proposed in Lab 1 of the UCM Computer Organization course: 

- [Exercise 1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab1#exercise-1)
- [Exercise 2](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab1#exercise-2)
- [Exercise 3](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab1#exercise-3)
- [Exercise 4](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab1#exercise-4)

They can also resolve the labs proposed at [FC2](https://www.fdi.ucm.es/profesor/mendias/FC2/FC2-en.html):

- [Lab 1 Spanish](https://drive.google.com/file/d/1vD-dEj_I9e0J7_fJanic2wUBde0CfJug/view?usp=drive_link) and [Lab 1 English](https://drive.google.com/file/d/1uVBFE2tmdGbNSWV2WaadVvWc9HtvPOEh/view?usp=drive_link)
- [Lab 2 Spanish](https://drive.google.com/file/d/1Arfs1Qzv8lMRCRRB0M0ugKqZXWSvwogY/view?usp=drive_link) and [Lab 2 English](https://drive.google.com/file/d/1wIz-KVbmyh0cShWmqq17FFPhKjqD4m2V/view?usp=drive_link)
- [Lab 3 Spanish](https://drive.google.com/file/d/1h-30tYPEItEp7HP_PFog_on8usOPHAIP/view?usp=drive_link) and [Lab 3 English](https://drive.google.com/file/d/1DG843vUgz7SzUuMzVe_iNZjI7YVk_Oyl/view?usp=drive_link)
- [Lab 4 Spanish](https://drive.google.com/file/d/1HYT762RhUX790BzBcWIhEE_K_vc6RVvk/view?usp=drive_link) and [Lab 4 English](https://drive.google.com/file/d/1njXjxYBLNCVi3pccEehvOG6DSoEcrCL9/view?usp=drive_link)


---


## RISC-V Single/Multi-Cycle and Pipelined Processors

Students can resolve the exercises proposed in Lab 2 of the UCM Computer Organization course which are related with Ripes. Specifically:

- Read the information provided at this link: [Introduction to Ripes](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md). Specifically, read the following sections:
    - [ProcessorTab](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md#the-processor-tab)  
    - [ProcessorView](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md#the-processor-view)  
    - [ProcessorModels](https://github.com/mortbopet/Ripes/blob/master/docs/introduction.md#selecting-processor-models)  
- [Ripes Processors](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2#ripes)
- [Exercise 1](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2#exercise-1)
- [Exercise 2](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2#exercise-2)
- [Exercise 3](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2#exercise-3)
- [Exercise 4](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab2#exercise-4)
