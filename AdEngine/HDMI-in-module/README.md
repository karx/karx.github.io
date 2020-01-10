## HDMI-In Module For Overlay
The `on-premise` device would use this module, input from DTH boxes. 

### Summary
1201 of the DMCA that makes it illegal to circumvent the protection on encrypted video feeds, even for your own private use.
This would mean that we would not be able to use encrypted feeds -when used- for this purpose. 
This blocks us from using the Video Markers.

Yet, we can overlay with an opaque background to these feeds.
We would require to use techniques like alpha blending which is not possible to do without decrypting the feed.

An ongoing lawsuit that would rectify the same: https://www.eff.org/cases/green-v-us-department-justice

The current approach involves us using HDMI to CSI-2 Bridge.

### POC Details
For the POC/make-it-happen phase, we would be using an HDMI to CSI-2 Converter for Raspberry Pi based on TC358743XBG.
This approch is being discussed in the following forums: 
* [Ask Electronics Thread](https://www.reddit.com/r/AskElectronics/comments/als3x5/hdmi_to_csi2_converter_for_raspberry_pi_based_on/) 
* [Raspi Forums](https://www.raspberrypi.org/forums/viewtopic.php?f=45&t=238826)

![HDMI to CSI-2 Convertor Image](https://akriya.co.in/assets/HDMI-CSI2-Pi.png)

The converter is ordered from China and we expect the delivery by 24th January.
Until we have the converter, the Raspberry Pi Camera Module V2 can be used as it works on the same signatures. (we are using the `raspivid` which was originally build for standard Raspberry Pi modules)

