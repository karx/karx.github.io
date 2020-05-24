# Streaming

## Streaming from System
* Preferred software for Straming: [OBS](https://obsproject.com/)


## Streming from Canvas
![Canvas to Stream](https://raw.githubusercontent.com/fbsamples/Canvas-Streaming-Example/master/doc/architecture.png)   


Original repository: [Facebook Canvas2Stream](https://github.com/fbsamples/Canvas-Streaming-Example)

* Used it here: https://github.com/devedvanta/pod-content/tree/kaaro/stream
* Gist on using it: https://gist.github.com/karx/327ab5d980f8950e49fec356962dd8c8
* Stream bridge repo: https://github.com/karx/kaaroStream-bridge


## Streaming from multiple Sources

### NDI   
Network Device Interface (NDI) is a royalty-free software standard developed by NewTek to enable video-compatible products to communicate, deliver, and receive broadcast-quality video in a high-quality, low-latency manner that is frame-accurate and suitable for switching in a live production environment.
* Skype enable NDI: https://www.skype.com/en/content-creators/
* https://www.youtube.com/watch?time_continue=49&v=QPg5IfqAkAI&feature=emb_logo
* The plugin for OBS: https://github.com/Palakis/obs-ndi

### OBS on Cloud/Shared PC
* https://www.youtube.com/watch?v=TtOqqj7RhZY

## Mobile Screen to PC
* https://github.com/Genymobile/scrcpy : Free

### RTMP bridge to OBS
Using VLC source as intermediate, https://www.reddit.com/r/obs/comments/692oeb/obs_studio_media_source_and_nginxrtmp/   
Also, 
```
using the VLC source, and then I have a second video file of random static in the playlist. It seems to work -- when there's a stream, it's showing the RTMP feed. When there's no more RTMP data, it switches to the next item in the playlist which is that static .avi.
```

### nginx RTMP module
https://docs.peer5.com/guides/setting-up-hls-live-streaming-server-using-nginx/

## Useful Links/Products
* https://github.com/sallar/mac-local-rtmp-server
* https://softvelum.com/larix/
* https://help.elgato.com/hc/en-us/articles/360031363132-OBS-Link-Setup
* https://garaninapps.com/rtmpminiserver
  
