# Limits of ESP32
The limits, based on use-case, so that we can target where to optimize in our IoT pipeline.

## Freq Counter

#### Time

* Local events 1 GHz   
These can be touch events.   
This means that ESP32 should not be choice of board for extreame real-time systems, where least count of less than 10^-6 sec is required.   


* Reboot time:

* Internet ping: 90 ms   
These can be MQTT messages, an HTTP call or similar.


For Internet based event, like Light turned ON, a Tweet, a post, weather update:   
The bottleneck is network latency. It takes about 99.1% of the time of the total turn around time.   

So optimization efforts should be targeted accordingly, no point having a faster chip/code if the affect on overall time is insignificant.


#### Memory
* Persistant Memory: 

* RAM: 


#### Power Consumption

* Average current consumption 80mA when processor is ON

* Deepsleep current consumption: 

* Ultra lowpower consumption: 



## References
* https://www.youtube.com/watch?v=CJhWlfkf-5M