## Skin Viewer
Would be awesome to have a A-frame component for Minecraft Skins


## Existing Implimentations
* https://github.com/earthiverse/3D-Minecraft-Skin-Viewer
* https://github.com/avaer/skin-js
* https://github.com/bs-community/skinview3d



## Skin from Minecraft APIs
* Postman Collection: https://www.getpostman.com/collections/d230ad19be6693088738    
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/d230ad19be6693088738)


## Usecase
* The Button experiment on Hermitcraft S7 can be tracked using skin viewer
* On-site chatbot skin 

Sample Skin to use: [docm77 skin](http://textures.minecraft.net/texture/11474ce87cd6bfddaeec6b3ef58bb5e3fafb483c0bcd3adb14620866b93e2a4)


## Current Update
For live view of user stats, the best way would be to read stright from player NBT data file, which in Singleplayer world is same as `level.dat` in the root folder of the save.   
Or the `playerdata/<player-UUID>.dat` file in case for SMP servers.

* For reading this data in-game, command
  
```
/data get entry @s
```

Read more about /data: [/data get](https://minecraft.gamepedia.com/Commands/data#get)


* Aiming for a Browser only implementation   
Running a Script or additional app is the easier route to go, but does does not help usablilty and participation. Plus Web capabilities are required, having additional modules/systems at User End seems hastle more.

However, the Web File API does not allow us direct access to File or File System. For real-time reading of the NBT file, this is a problem, we cannot have the user repeatly upload - select the file we aiming for atleast like once 5-10 sec update (hopefully a lot more).


I could find https://github.com/WICG/native-file-system that can provide us a way to do this. Exploring this next.


