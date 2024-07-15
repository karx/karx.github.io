Hey all, I have been really enjoying the vibrant community we have around AoE. The tooling, the support, the discussions, the creators and ofcource the GGs. I have also been streaming my POV games, casting some 2v2 silver league and doing AoE 2 related streams in general.

While doing so, I started to work on some overlay tools that I feel could be useful.

I started with the most fundamental and used scoreboard, and moved on to AoE2-profile cards, and recent match history (using aoe2.net as the data source).



### kaaroscorebaord 
You can create multiple rooms for each `type` of stream. Each room has multiple customizable layouts that you can use (as OBS browser source) while streming. Each room has a control page, that has all the options for updating the overlay conveniently. 

(Pro tip: Add the control page of your page as a custom DOCK in OBS for quick access)

* The scoreboard
As of now it is just head-up 2 player board, but can be customized for a n-player layout.


* AoE-2 Profile Card
Powered by last 60 matches worth of data pulled using aoe2.net API using stream profile-ID. There is a quick search built into the control page to help search for players using their in-game name.

* AoE-2 Match History
Shows the last 5 matches played.


