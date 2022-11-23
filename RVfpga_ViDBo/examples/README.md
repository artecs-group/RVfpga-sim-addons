Follow the next steps to run the provided program in the RVfpga_ViDBo simulator:


1. Open a terminal and go to the current folder. Run the Verilator-simulator using the following command (Ubuntu 20.04): 
```
<path-to-binary-file>/RVfpga_ViDBo_Ubuntu20 +ram_init_file=LedsSwitches/LedsSwitches.vh
```

2. Open another terminal from the same folder and run the virtual board using the following command:
```
python3 -m http.server --directory ../NexysA7board/
```
3. Open a browser and connect to `http://localhost:8000/nexys-a7.html`

4. On the browser, click on "connect to the board" and test the program. If you invert a switch the corresponding LED should also invert its state.
