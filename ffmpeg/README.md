# ffmpeg
ffmpeg is super awesome. Anything to do with video - transcoding, streaming, cropping. 

## Freq used
* Cropping/Pruning out recorded videos

```
ffmpeg -i input.mp4 -ss 00:01:27 -to 00:41:14 -c:v copy -c:a copy output.mp4
```

Ref blog post: [alexarje](https://www.arj.no/2018/05/18/trimvideo/)

* Streaming feed to RTMP server
  
```
ffmpeg -i INPUT -acodec libmp3lame -ar 11025 --f rtp rtp://host:port
```

Used in [kaaroStream-bridge](https://github.com/karx/kaaroStream-bridge/blob/master/streamer-bridge.js) as a hosted service, to stream from a webpage.   
Also [ffmpeg streaming ref page](https://trac.ffmpeg.org/wiki/StreamingGuide)


## Notes
* ffmpeg is cross platform.
