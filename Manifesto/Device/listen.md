## The listener

## Summary
This device module is to act as an companion device for the Engagement Module
This will help capture and cataloge "knowledge"

## Functions
* Mapping of device to session.
    


### Session

gantt
    dateFormat  YYYY-MM-DD
    title Listen Device
    section Listen Device
        open                :active,    des0, 2014-01-06  ,2d
        Start session       :des1,      after des0 ,5d
        maintain session    :done,      after  des1, 50d
        Log Chunk-1         :des2,      after des1, 10d
        Log Chunk-2         :           des3, after des2, 10d
        Log Chunk-3         :           des4, after des3, 10d
        Log Chunk-4         :           des5, after des4, 10d
        Log Chunk-5         :           des6, after des5, 10d
        Close Session       :           des7, after des6, 5d
        open                :active,    des8, after des7, 2d
    section Engagement Module
        timer start         :crit,      desc0, 2014-01-08 ,5d
        maintain session    :done,      desc1,  after  desc0, 50d
        timer stop          :crit,      desc2, after desc1, 5d
        
        
###