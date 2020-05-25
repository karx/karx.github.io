* https://ubuntu.com/tutorials/tutorial-ubuntu-desktop-aws#4-aws-configuration
* https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-nvidia-driver.html#nvidia-driver-types
* https://docs.peer5.com/guides/setting-up-hls-live-streaming-server-using-nginx/
  

##  So we have VNC.   
  
A VNC server does not run an X server, a VNC server is an X server. It does not "screen scrape," it implements a frame buffer in main memory (a virtual display, if you will) and protocols to transmit frame buffer updates over the wire. 

So we cannot run OBS or any other Softwares that require OpenGL.

```

The VNC server X implementation does not provide the GLX extension; as you noted this is why GL apps cannot run. You can verify this by running xdpyinfo in a terminal inside a VNC session and a console X session on the same machine. 

```

https://forums.gentoo.org/viewtopic-t-768353-start-0.html

## Intro VirtualGL
This ScreenGrabs from the Remote Server, compresses and then sends.

* To setup headless nVidea, follow this: https://virtualgl.org/Documentation/HeadlessNV
* Alot of later protocols have root in this.
* https://virtualgl.org/Main/HomePage


## Then we have X2Go
* Python based
* Much newer as compared to all other. 2018
* https://wiki.x2go.org/doku.php/doc:installation:x2goserver

## NX
* Installed using: https://computingforgeeks.com/install-nomachine-rdp-tool-on-ubuntu-linux/   
Replace wget link with latest from: https://www.nomachine.com/download/

* The client/server app is same and is available [here](https://www.nomachine.com/download/) for all platforms.

* For headless on Server: https://www.nomachine.com/AR10K00710cat
* Setting up server for ssh
  
* https://www.nginx.com/blog/video-streaming-for-remote-learning-with-nginx/


## Current Issues 
* Skype NDI now available for Linux

## Looking forwards
* If we are to use SRT protocol instead of RTMP for internal i.e before sending to Twitch or YouTube, we might see improvements in Latency, and better resilience to network issues.   
More about SRT here: https://obsproject.com/wiki/Streaming-With-SRT-Protocol#general-overview

