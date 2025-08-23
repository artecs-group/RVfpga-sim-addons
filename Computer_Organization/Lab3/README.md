# Lab 5 (Lab 3 of CO) - The Memory Hierarchy
This practice aims to help students understand the cache memory. You can follow the next steps:

1. Start by looking at the detailed presentation of the Ripes cache simulator provided here: [Presentation_Cache_Ripes](https://drive.google.com/file/d/1ffplxLHiyvC6G4GWyLHEbvgANaIqjZK0/view?usp=sharing).
2. Then, you can read the simulator guide provided [next](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab3#cache-simulation-in-ripes) in this repository.
3. Finally, you can resolve the exercises included [below](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab3#exercise-1) in this repository, using Ripes.

## Cache simulation in Ripes
The cache view allows simulating different configurations and management policies for first-level data and instruction caches. In general, and unless stated otherwise, for this practice, we will configure the compiler to work with optimization level -O1 and set the processor to Single-Cycle 32-bit (see the following two figures). Moreover, in most of the exercises, we will not analyze the instruction cache, so its configuration will not affect us, and we can leave it as the default in the simulator.

<p align="center">
  <img src="Images/CompilerSettings.png" width=80% height=80%>
</p>

<p align="center">
  <img src="Images/Processor.png" width=80% height=80%>
</p>

As an example, we next show the steps to simulate Exercise 1-a (provided [below](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab3#exercise-1) in this repository), which uses the following program (you just need to copy the code to the Ripes editor). 

```
#define N 4

int A[N][N] __attribute__((aligned(128)));
int B[N][N];
int C[N][N];

main(){
   int i, j, x;

/* Initialize matrices */
   for (i=0; i < N; i++)
       for (j=0; j < N; j++){
           A[i][j]=i*N+j+259;
           B[i][j]=i*N+j+1024;
           C[i][j]=0;
       }
          
/* Analyze this loop */
   for (i=0; i < N; i++)
       for (j=0; j < N; j++)
       	C[i][j] = A[i][j] + B[i][j];

}
```

The program begins with an initial nested loop (*Initialize matrices*) that simply initializes the elements in A, B, and C, which we will not analyze and that you should simply ignore. Then, another nested loop follows (*Analyze this loop*), performing a computation that stores in C the sum of the elements in A and B. This is the result (the values are shown in hexadecimal):

<img width="1367" height="266" alt="image" src="https://github.com/user-attachments/assets/5918ba34-3038-4b53-9f2e-e3838d9d7503" />


1. The Cache window allows configuring the data cache and the instruction cache separately. For example, in this case, we would be configuring a data cache with the following parameters:
- 4 lines (2<sup>N</sup> Lines = 2)
- 4 words per line (2<sup>N</sup> Words/Line = 2)
- 1 way (2<sup>N</sup> Ways = 0)
- LRU replacement policy
- Write-back and Write-allocate write policies

<p align="center">
  <img src="Images/CacheConfiguration.png" width=60% height=60%>
</p>

Given that each word is 4 bytes (32 bits) in the RISC-V architecture used, in this case, we would have a cache size of 4 lines * 4 words * 4 bytes = 64B (2<sup>6</sup>B). At the bottom right corner, we can see the statistics for misses, hits, writebacks, etc.

2. Copy the initial program (provided above) into the editor, compile it (use -O1 optimization level), and check that everything works correctly.

<p align="center">
  <img src="Images/ProgramRipes.png" width=80% height=80%>
</p>

3. Locate the ```main``` function and the loops that make up the function. The ```lw``` and ```sw``` instructions are very helpful for locating these loops. In this case, the loop to analyze is the following:

<p align="center">
  <img src="Images/Loop.png" width=50% height=50%>
</p>

4. Set a breakpoint at the beginning of the loop to be analyzed by clicking on the left button over the blue vertical column, next to the instruction where you want to place it.

<p align="center">
  <img src="Images/Breakpoint.png" width=50% height=50%>
</p>

5. Run quickly until the breakpoint at the beginning of the loop to be analyzed. Keep in mind that the execution will stop after the instruction where the breakpoint is located is executed.

<p align="center">
  <img src="Images/Buttons.png" width=40% height=40%>
</p>

6. In the cache tab, write down the number of misses, hits, and writebacks you have at the starting point of the loop to be analyzed, as this will be the initial value from which we will count the misses and accesses of the loop to be analyzed. In the figure you can see that:

	 * Hits = 81
	 * Misses = 76
	 * Writebacks 69

<div align="center">
  <img src="https://github.com/user-attachments/assets/3b95daaf-ff89-4b52-bee7-49dc4b7b8e14" alt="image">
</div>

7. Delete the breakpoint and add another one right after the loop:

<p align="center">
  <img src="Images/Breakpoint2.png" width=50% height=50%>
</p>

8. Run quickly until the breakpoint, and write down again the number of misses, hits, and writebacks. In the figure you can see that:

	 * Hits = 81
	 * Misses = 124
	 * Writebacks 85

<div align="center">
  <img src="https://github.com/user-attachments/assets/b6ae1ed9-afbf-48c8-8faf-f4d161fbf861" alt="image">
</div>

9. With this information, we can calculate the hits, misses, and writebacks:

	 * Hits = 81 - 81 = 0
	 * Misses = 124 - 76 = 48
	 * Writebacks = 85 - 69 = 16

Do these numbers make sense?

Remember that this is the cache configuration that we are using, where the block is determined using bits 4 and 5.

<div align="center">
  <img src="https://github.com/user-attachments/assets/0e3d48a3-3b64-4799-b944-eac3b0b51206" 
       alt="image" 
       style="width: 80%; height: auto;">
</div>

Also, we need to know the addresses where each array is mapped to. We can deduce it by looking at the pointer values.

<div align="center">
  <img src="https://github.com/user-attachments/assets/5a17f801-860f-4a68-bdce-ee33e8574e5e" 
       alt="image" 
       style="width: 80%; height: auto;">
</div>

According to this information, we can deduce the following:

- Starting address of A: 0x11b00 which in binary is 0001 0001 1011 00**00** 0000
- Starting address of B: 0x11b40 which in binary is 0001 0001 1011 01**00** 0000
- Starting address of C: 0x11b80 which in binary is 0001 0001 1011 10**00** 0000

The bits in bold (bits 4 and 5) determine the cache block where the data is mapped to. 

Thus, in each iteration all three arrays will map to the same block and no hit will happen.

12. Finally, analyze step by step and explain the evolution of the cache throughout the execution of the loop, carefully observing the evolution of the blocks. You can progress gradually from the start of the loop, stopping after executing each ```lw``` or ```sw``` instruction and analyzing the cache state. For example, the following figures show the cache state during the fourth iteration:

 * After the first load:

<div align="center">
  <img src="https://github.com/user-attachments/assets/591849bf-d9ca-49fe-a946-c67a556f0bb3" alt="image">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/2f5f4c4c-c329-44d9-b68f-5fa8dc257f7a" alt="image">
</div>

 * After the second load:

<div align="center">
  <img src="https://github.com/user-attachments/assets/9d5fe6f1-c540-43bb-9aef-3628cd308632" alt="image">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/5f07b22f-3933-4aed-ba17-0a7da55c9633" alt="image">
</div>

 * After the store (note that the value written is not shown immediately in the cache, but when the next store is executed):

<div align="center">
  <img src="https://github.com/user-attachments/assets/15e7fa1e-6b88-4a07-823c-29df78a7216a" alt="image">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/fc7de4dc-ef5f-40a7-bdb3-9fb5e79cb053" alt="image">
</div>



## Exercise 1
Copy in Ripes the following program:

```
#define N 4

int A[N][N] __attribute__((aligned(128)));
int B[N][N];
int C[N][N];

main(){
   int i, j, x;

/* Initialize matrices */
   for (i=0; i < N; i++)
       for (j=0; j < N; j++){
           A[i][j]=i*N+j+259;
           B[i][j]=i*N+j+1024;
           C[i][j]=0;
       }
          
/* Analyze this loop */
   for (i=0; i < N; i++)
       for (j=0; j < N; j++)
       	C[i][j] = A[i][j] + B[i][j];

}
```

The program begins with an initial nested loop that simply initializes the elements in A, B, and C, which we will not analyze. Then, another nested loop follows, performing a computation that stores in C the sum of the elements in A and B. This is the loop we will analyze in the cache.

Analyze and explain the cache's behavior for the second nested loop, adding screenshots from the simulator. Analyze misses, hits, and writebacks, as well as the evolution of the cache throughout the loop execution, carefully observing the evolution of the blocks. You can progress gradually from the beginning of the loop, pausing after the execution of each lw (load word) or sw (store word) instruction, and analyzing the state of the cache.

Analyze the following scenarios:

a. Direct mapping data cache (illustrated in the previous section).

<p align="center">
  <img src="Images/CacheConfiguration.png" width=60% height=60%>
</p>

b. Two-way set associative data cache.

  - Increase the number of ways to 2: 2<sup>N</sup> Ways = 1
  - Reduce the number of lines to 2, to keep the total data cache size the same: 2<sup>N</sup> Lines = 1
  - Test the two available write allocation policies: *Write No-Allocate* and *Write Allocate*.

c. Four-way set associative data cache.

d. Modified program: A programmer suggests the following modification for the program that runs in a two-way set associative data cache with write allocation. Analyze in detail the cache behaviour in this case.

```
#define N 4

struct {
		int A;
		int B;
} AB[N][N] __attribute__((aligned(128)));

int C[N][N];

main(){
   int i, j, x;

/* Initialize matrices */
   for (i=0; i < N; i++)
       for (j=0; j < N; j++){
           AB[i][j].A=i*N+j+259;
           AB[i][j].B=i*N+j+1024;
           C[i][j]=0;
       }
          
/* Analyze this loop */
   for (i=0; i < N; i++)
       for (j=0; j < N; j++)
       	C[i][j] = AB[i][j].A + AB[i][j].B;

}
```


## Exercise 2
Simulate the following code in Ripes. 

```
int nota[8] __attribute__((aligned(128)));	
int media[8] __attribute__((aligned(128)));	

main(){
  int i;

  /* Initialize arrays */
  for (i=0; i < 8; i++){
    nota [i] = i;
    media [i] = i+5;
  }
  
  /* Analyze this loop */
  for (i=0; i < 8; i++) {
    if (i > 1 && i < 6)
    		nota[i] = media[i] / 2;
    else
    		nota[i] = nota[i] * media[i];
  }

}
```

The program begins with an initial loop that simply initializes the elements in nota and media, which we will not analyze. Then, another loop follows, performing a different computation that depends on the i value. This is the loop we will analyze in the cache.

Configure the data cache with a total size of 64B, with 16B blocks. Simulate the program with a direct-mapped data cache and No-Write-Allocate. You should analyze and explain the cache's behavior in detail, adding screenshots from the simulator.

a. Locate the loop to be analyzed in the disassembled code in Ripes. The loop is programmed in a somewhat original way. Explain it in detail. You can use a step-by-step simulation and screenshots to assist in your explanation.

b. Analyze the behavior of the data cache in detail. Perform the analysis section by section: iterations 0 to 1, iterations 2 to 6, and iterations 7 to 8.

c. Perform code optimizations (such as array enlargement, array fusion, etc.) and explain the results obtained compared with the results of the original code.

d. Finally, test a 2-way set associative cache (keeping the total size of the cache unchanged) for the original code. Compare the results with the ones obtained in item c.


## OPTIONAL - Exercise 3
Simulate the following code in Ripes. 

```
int A[16][16] __attribute__((aligned(128)));
int B[32];
int C[16][16];

main(){
int i, j;

   /* Initialize matrices */
   for (i=0; i < 16; i++)
       for (j=0; j < 16; j++){
           A[i][j]=i*16+j;
           C[i][j]=0;
       }
  for (j=0; j < 32; j++)
       	B[j]=j+3;

  /* Analyze this loop */
  for (i=0; i< 16; i++)
     	 C[0][i] = A[0][i] + B[4];
  }
```

a. Configure the data cache with a total size of 128B, with 16B blocks. Simulate the program with a direct-mapped data cache and Write Allocate. Simulate step by step and justify the results from the simulator.

b. Simulate the program with a data cache similar to the previous item but with 2-way associativity (keeping the total data cache size unchanged). Explain the results.

c. Analyze and explain in detail the evolution of the instruction cache for the loop to be analyzed, for the following two configurations:

<p align="center">
  <img src="Images/Conf1.png" width=60% height=60%>
</p>

<p align="center">
  <img src="Images/Conf2.png" width=60% height=60%>
</p>


## OPTIONAL - Exercise 4
Consider a computer with a main memory of 4MB, addressable by bytes, equipped with a 2KB cache, with lines of 512B. The cache is direct-mapped and uses write-allocation. The following code is to be executed:

```
int A[1024] __attribute__((aligned(128)));
int B[1024];
int C[1024];

main(){
int i, j;

   /* Initialize matrices */
   for (i=0; i < 1024; i++){
          A[i]=i;
		B[i]=i+7;
          C[i]=0;
       }

  /* Analyze this loop */
  for (i=0; i< 1024; i++)
     	 C[i] = A[i] - B[1023-i];
}
```

Answer the following questions. You should analyze and explain the behavior of the cache in detail, adding screenshots from the simulator.

a. How many cache misses occur?

b. How many cache misses occur with a direct-mapped cache but using a no write allocation policy?

c. How many cache misses occur with a two-way associative cache (with the total cache size remaining the same; that is, there will be half as many block frames) and with write allocation?

d. Analyze the program for the same cache as in section *c* but changing the write policy to Write-Through.
