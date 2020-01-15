## AdEngine Status Update
Status update scheduled for 15th Jaunary 2020

### Summary
The main focus of the work done has been Module 1.1 `DTH Piggybanking H/W`. For the POC we are using a `HDMI to CSI-2 bridge` and piggybanking on Camera-In of a Raspberry Pi. The output is built with pass-thought video + overlay which is editable HTML.

### Progress
* Raspberry Pi for `on-premise` device, basic setup.
* HTML Overlay with control (Tested using connected Keyboard)
* Video pass-through using PiCamera 2

### Immediate Tasks
* MQTT Broker setup for local communications
* On boot autostart AdEngine Module 
* Using `CSI-2 Brige` instead of Pi Camera for pass-through video
* DTH Video with time-script as input

### Problems/Risks
* Order delivery is taking longer than expected.
We should have 2 X `HDMI to CSI-2 bridge` by 25th January 2020
* Without Hardware accelertors, we would see performace issues on video feeds greater than 720p 30fps.

### Hardware Budget
* Raspberry Pi 4  x 2 : 11500/-
* Raspberry Pi Camera Module x 1 : 2500/-
* HDMI to CSI Bridge x 2  + Delivery : 80$ = 5700/- 

### More details
Details of approch for `on-premise` module can be found here: [Week A: HDMI-In-Module](./HDMI-in-module)