## SmartBike hardware 


## Requirement
The hardware on the bike is required to fulfil the following purpose
* Regular streaming of current bike state
This includes the following
```
    geolocation
    bike battery percentage
    bike current speed
    bike lock status
    bike dock status
```
* Async Tasks
```
    Unlocking the cycle lock
    conformation of bike locking
    conformation of bike docking
```


## Issues/Questions
* Existing modules/infrastructure knowledge 
    I personally, do not have much specs or information about the already onboard system on the bike. 
    Eg. The system requires a dump of battery percentage, it would be great if we could leverage the what has already been built and tested.
    
    If there is any high level document, or someone who can help me create such a document. So that we can start sending these data points upstream.
* Dock infrastucture
    I wanted to know if there is any electric or telemetry system in our docking stations ?

    