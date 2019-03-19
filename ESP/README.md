# ESP
ESP8266 and ESP32 is a series of low-cost, low-power system on a chip microcontrollers with integrated Wi-Fi and dual-mode Bluetooth.

created and developed by Espressif Systems, a Shanghai-based Chinese company
![ESP32](https://www.espressif.com/sites/default/files/modules/esp32-wroom-32-01-s.png)


## Feature List of the board
* Good processor!
(240 MHZ)
* Enough memory!!
(520 KB but context)
* Wifi + Bluetooth
* Base feature set - Secureboot, Stadard Security fetures, Cryptograhic hardware accelerations, Power management!!!!!


## Programming/Interfacing

We have a few options here now. As mentioned, The ESP communutity has a thriving ecosystem of developers!
* Arduino IDE
* ESP Easy
* Official Espressif Develepment Frameworks - They also have one dedicated for Mesh Systems
* Esprunio
* Mongoose OS
* Lua
* RToS
* MicroPython

Then we also have a bunch of tools that were created in this ecosystem.
* PlatformIO


## Small intro to firmware
Breif description about by taking Arduino Stack as example

Code that we write -> Building - > Firmware
Bootloader + Firmware - Goes to chip

A good rule of thumb to categorize something as firmware: is it part of the layer, which also provides API for interacting with GPIO ports

In a the basic ino files we observe, the breakdown is something like:
The parts
* Arduino IDE - The building and uploading tool used 
* Arduino C - The languge used for logic building
* Arduino Framework - The OS/Firmware type

## Time to choose our firmware/framwork, tools, and language of choice
Choice of ecosystems:
* Standard Arduino Stack

* Arduino Framework with C++
We structure our code better. Instead of using Arduino's version of C. we take more control of the running logic.
Note here that the underlying framework is Arduino. 

* MicroPython
MicroPython is a vibrant community of enthusiasts that have build this implementation of CPython Specs, tailored for these class of Processors
Python on device
[Micropython](https://karx.github.io/Micropython)

* Esprunio
JS on device
[Esprunio](https://karx.github.io/Esprunio)


## Choose your Board
* ESP8266
* ESP32
* ARM based
* Framework native boards - PyBoard, Pixl.js, etc


## OTA
* We can wrap the entire "sketch" inside an OTA version management system so to say.