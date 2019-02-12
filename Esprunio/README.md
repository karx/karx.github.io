# Esprunio
Espruino – JavaScript SDK and firmware closely emulating Node.js


# Content
In this session we will be covering 
* the basics of Espruino JavaScript
* the Espruino Web IDE
* Running ES6 on ESP32
* Connecting to the WEB
* Small Project (!)

## Basics of Espruino JavaScript
[Espruino Github](https://github.com/espruino/Espruino)
Espruino is a JavaScript interpreter for microcontrollers.
* JavaScript


## Espruino Web IDE
[Web IDE](https://chrome.google.com/webstore/detail/espruino-web-ide/bleoifhkdalbjfbobjackfdifdneehpo)
![Web IDE](https://lh3.googleusercontent.com/oXNOWEiBipyay5T0X7VEBcurNHuVMtE5LXJC3Cv5RDq8WX_FrZSz35WHcK5eNLAuK4yEoHOCBA=w640-h400-e365
)

## Lets run Hello World
```
console.log("Hello World!);
```
Now I would recommend you to play around with this JS interpreter. 
Espruino aims to almost mimic Node.js*



## Connecting to Wifi

```
var ssid = 'YOUR_SSID';
var password = 'YOUR_SSID_PASSWORD';

var wifi = require('Wifi');
wifi.connect(ssid, {password: password}, function() {
    console.log('Connected to Wifi.  IP address is:', wifi.getIP().ip);
    wifi.save(); // Next reboot will auto-connect
});
```


## It is time for a small Project
> Project to be decided based on location and duration of the event.

