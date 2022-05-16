# Embedded_digital_network_analyzer
In this repository the codes are attached: "Available 5/16/2022"
# Digital Network Analyzer
## _INTRODUCTION.- 


![Build Root](https://buildroot.org/)

In this repository, the base descriptions for the description of the CODE projects developed in 2022 for the Project of Master1 of the Franche Comte University in the master program in Smart Integrated System are presented.
The software used will be:
- [BUILDROOT] -For the generation of the embedded ISO or the operative system.
- [PYTHON] - For the integration of the different componens and the Programation of the logic
- [GNURADIO] - For the exploration of radiofrecuency.
- [TKINTER] - For the design of the interface.

This repository is organized as follows, in order to show a progress consistent with the instructions shown in http://jmfriedt.free.fr/ for the Final Project.

- WEEK 1: Exploration of the build Root  
- WEEK 2: Exploration and using GNURadio 
- WEEK 3: Implementation: Using an
RTL-SDR DVB-T dongle as radiofrequency receiver 
## EXPLORATION OF BUILDROOT(1st Week)

- Generate the image for GNURdio available in (https://github.com/oscimp/oscimp_br2_external/tree/master/configs)
- Configurate with Dropbear
- Test Audio output


## USING GNU RADIO(2nd Week)
This week was explored GNURadio in order to generate files to recieve and send data by ethernet with the  Rpi4, for this week is neccesary:
- Use TKinter to create the interface
- Use Python to implement sockets
- with SCP copy the files to the Rpi4


## IMPLEMENTATION(3rd Week)

In this week is explored:
- The investigation of readiofrecuency emissions
- The use of the Internal PPL of the RPI4
- Controlling and receiving the signas of the DVB-T dongle.
Its imporatant to be carefully with the installation of RPITX, explained in: https://github.com/jmfriedt/gr-rpitx

## Installation

To use the programs, clone the repository scripts:


```sh
git clone https://github.com/GroverAruquipa/Embedded_digital_network_analyzer/
```-
