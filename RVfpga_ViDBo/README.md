For using this simulator in Ubuntu it is required to first install websockets library: 

```
sudo apt-get install -y libwebsockets-dev
```

Then, follow the next steps to run the LedsSwitches program in the RVfpga_ViDBo simulator:

1. Open a terminal and go into the *RVfpga-sim-addons/RVfpga_ViDBo/examples* folder. Run the Verilator-simulator using the following command (Ubuntu 20.04): 
```
<path-to-binary-file>/RVfpga_ViDBo_Ubuntu20 +ram_init_file=LedsSwitches/LedsSwitches.vh
```

2. Open another terminal and go into from the same folder (*RVfpga-sim-addons/RVfpga_ViDBo/examples*). Run the virtual board using the following command:
```
python3 -m http.server --directory ../NexysA7board/
```
3. Open a browser and connect to `http://localhost:8000/nexys-a7.html`

4. On the browser, click on "connect to the board" and test the program. If you click on any of the 16 switches its state will invert as well as the state of the corresponding LED.
