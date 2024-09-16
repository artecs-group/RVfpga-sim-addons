# Lab 3 - The Memory Hierarchy
This practice aims to help students understand the cache memory. You can follow the next steps:

1. If you are new to Computer Organization, you should start by reading Chapter 8 of the H&H book.
2. Then, you should look at the detailed presentation of the Ripes cache simulator provided here: [Presentation_Cache_Ripes](https://drive.google.com/file/d/1ffplxLHiyvC6G4GWyLHEbvgANaIqjZK0/view?usp=sharing).
3. Then, you can read the simulator guided provided [next](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab3#cache-simulation-in-ripes) in this repository.
4. Finally, you can resolve the exercises included [below](https://github.com/artecs-group/RVfpga-sim-addons/tree/main/Computer_Organization/Lab3#exercise-1) in this repository.


## Cache simulation in Ripes
The cache view allows simulating different configurations and management policies for first-level data and instruction caches. The Cache window allows configuring the data cache and the instruction cache separately.

For example, in this case, we would be configuring a data cache with the following parameters:
- 4 lines (field "2N Lines = 2")
- 4 words per line (field "2N Words/Lines = 2")
- 1 way (field "2N Ways = 0")
- LRU replacement policy
- Write-back and Write-allocate write policies

<p align="center">
  <img src="Images/CacheConfiguration.png" width=80% height=80%>
</p>

Given that each word is 4 bytes (32 bits) in the RISC-V architecture used, in this case, we would have a cache size of 4 lines * 4 words * 4 bytes = 64B (26B). At the bottom, we can see the statistics for misses, hits, writebacks, etc.

In general, and unless stated otherwise, for this practice, we will configure the compiler to work with optimization level -O1 and set the processor to Single-Cycle 32-bit (see the following two figures). Moreover, in most of the exercises, we will not analyze the instruction cache, so its configuration will not affect us, and we can leave it as the default in the simulator.

<p align="center">
  <img src="Images/CompilerSettings.png" width=80% height=80%>
</p>

<p align="center">
  <img src="Images/Processor.png" width=80% height=80%>
</p>

In the exercises, it should be noted that the simulation results will generally not match exactly with those from the worksheet, due to various side effects: different memory location of the vectors, blocks present in the cache after the initialization of the vectors, etc.


## Exercise 1
Simulate in Ripes the following code. 

```
#define N 4

int A[N][N];
int B[N][N];
int C[N][N];

main(){
   int i, j, x;

/* Bucle para asignar valores iniciales a las matrices */
   for (i=0; i < N; i++)
       for (j=0; j < N; j++){
           A[i][j]=i*N+j;
           B[i][j]=i*N+j+3;
           C[i][j]=0;
       }
          
/* Bucle a analizar */
   for (i=0; i < N; i++)
       for (j=0; j < N; j++)
       	C[i][j] = A[i][j] + B[i][j];

}
```

You should analyze and explain the cache's behavior in detail, using screenshots from the simulator to assist you. Analyze misses, hits, and writebacks, as well as the evolution of cache blocks step by step (you can pause execution after each load/store, at the end of each iteration, etc.). 

Also, analyze step by step and explain the evolution of the cache throughout the loop execution, carefully observing the evolution of the blocks. You can progress gradually from the beginning of the loop, pausing after the execution of each lw (load word) or sw (store word) instruction, and analyzing the state of the cache.

a. Start with a small matrix size (N=4) and a small data cache size (keep the instruction cache at the default size provided by the simulator) to easily analyze the behavior of the data cache. Specifically, we will use the following data caches:
- Direct mapping

<p align="center">
  <img src="Images/Ex1.png" width=80% height=80%>
</p>

- Two-way set associative:

  - Increase the number of ways to 2: 2N Ways = 1
  - Reduce the number of lines to 2, to keep the total data cache size the same: 2N Lines = 1
  - Test both write allocation policies: Write Allocate and Write No-Allocate.

b. Next, increase the size of the matrices and the data cache to the sizes in the worksheet, and check whether the results from the exercise are consistent with those from the simulator.
