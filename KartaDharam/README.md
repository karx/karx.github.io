## Karta-Dharam
This document is to serve as Spec doc in the future for
' Our framework/toolchain we use to deploy/run/debug logic on embedded systems '

## Content
* Purpose
* Requirement Specifications
    * Functional
    * non functional
* Architectural Specs
* Diagrams
* Rational



## Purpose
Use this skeleton application to quickly setup and start working on a new IoT application. This application uses the latest ESP32 WROOM-32 as the base  


## Business Specification

#### Connectivity
* Beacon
* Bluetooth
* Wifi - Hotspot
* Wifi 
* SIM/
* Intranet
* RFID

#### ACTUATORS and Sensors 
* Actuators
    * Motors
        * servo
        * stepper
    * Linear Atuators
    * Light
    * Relay
* Sensor
    * Real Time vs On Demand sensors
    * Physical Sensors
        * Temperature 
        * Pressure 
        * Load Cell 
        * accelerometers
        * inertia measurement
    * Chemical Sensors
        * Ph Sensor
        * Gas Sensor
    * Digital Sensor 
    * Camera
    * soil sensors
    * Usual sensors
        * IR 
        * Ultrasonic
        * hall effect sensor
        * proximity sensor
        * motion sensor 
        * flame sensor
        * LDR
        * rain drop detection sensor
        * wind speed sensor

#### Authorization 
* RFID/NFC
* Fingerprint
* Coin Collector
* ESP camera
    * Face recognition 
    * Voice recognition


#### I/O Modules

* Input Modules
    * arrow keys 
    * PS2 controller
    * Touch TFT
    * Camera
    * Mic
    * Keypad
    * capasitive touch buttons

* Display/Output  Modules  (can be used for logging/debugging)
    * VGA screen
    * oLED 
    * HDMI output
    * LCD 
    * Speaker 
        * Aux
        * buzzer
        * voice output 
        * recording playback module
    * LED 
    * Touchg TFT

#### Oscilometer code 
* detecing AC current / Voltage
* detecting DC current / voltage

#### Inbuilt IC support
* Should support 3*8 demux by default 
* Should support 4*16 demux by default 
* Analog to digital converter 

#### Power backup / stablization 
* should not lose state/data in case of minor power fluctuation / loss 
* Real time clock 
* multiple type of batteries/ chanrging ports (like esp has vin pin and also takes in using microUSB)
* solar panel

## Industry Requirements
 * Stable/ Reliable
 * OTA 
 * Plug and play devices
 * Easy to deploy code to device
 * (Module) Easy to maintain by multiple deveopers at once 
 * Servicability
    * Problem isolation V important (not a PhD will go to repair the module.) 
    * parts should be removable should not have to remove entire motherboard.
 

## Soft-requrements
* EASY
* 15 mins
* No electronics required at all
* SPI and I2C can be abstracted ?
* GPIO and serial out should feel same


## More about OSI Layer

The below diagram, shows the seven layers of the OSI model.

![OSI Layer Image](https://images.ukdissertations.com/32/0232323.001.jpg)

Source: https://www.ukdiss.com/examples/physical-layer-data-link-layer.php