## Discord
Modern communication app

## Introductions
I started to use discord, when PUBG was in the Early access for what felt like a decade. Found myself a group of players who were `connected` at least for 20-30% time during the day. A replacement for TeamSpeak, it initially felt like, later turned out to be the best communication platform, we currently have.

For teams, communities and groups of all sizes, discord presents itself as the best and most versatile platform. 
It has features and plugins that help with:
* Boost productivity (starting a little generic)
* Community Engagement toolkit
* Community Moderation toolkit
* Empower developers with commerce
* Automation flows using Bots
* Host digital meetups
* In-app premiums and merchandise (Like VIP lounges, special badges, etc)
* Embeddable sharable presence on the web
* Much much more...


A fun-loving and vibrant community of developers from the OS domain have chosen Discord as their HQ for discussion. There is no shortage of plugins and customizations that are possible on this platform.


## How we used Discord
#### *Our primary communication platform*
We have created separate channels for developers, bot-testing, bug-reports.

We also have spawned a couple extra guilds over the years, both those are for the projects that successfully turned into products.
This enables to use the discord guild as the primary support channel for the product as well. We can provide prompt response, the devs are always listening and the UI is amazing!

#### *Discord webhook for logging*
Logs are important. 

Discord webhooks enables me to push important events to our primary communication channel. 
KPIs like the following are always streamed to the team: 
* How many devices are online.
* On every server restart.
* Product Checkout
* Social tag


#### *Discord.js = Awesome Bots*
Discord API are exquisite.

discord.js is a JavaScript module to interact with Discord APIs in a Node.js Environment.

node.js environments means the web, and the web is everywhere.

This enabled us to build tools specific for on-ground operations. One nice example is the kaaroEvents bot we had to build manage our instaWend machines during the Events.

## How does discord work
So, as of this moment, on Discord, there are over `500M` users of the platform.

There are over `20M` active user on the platform.

Estimating approx `100K` active voice channels that are active with users.

Estimating over `100K` bots active on the platform.

Estimating over `2B` messages sent/received on the platform.

That is at this moment.

So what kind of infrastructure is required for this volume?

How do they manage so many concurrent threads?

And so smooth?

Well, it is the semantic web + modern JS technologies + Erlang based Exchange system

I tried looking up on the internet more about this infra.
Well, most of it is `awesome`.
They are using Cowboy for Erlang.

Flask for REST APIs.

They used to use Cassandra, but are migrating to Scylla according to [this](https://www.reddit.com/r/discordapp/comments/ewz9rf/discords_switch_from_cassandra/) Reddit thread on r/discordapp.

But these are just, tools, what make the product this amazing the *the people*, the people using it, the community, the developer forums, the executive team, are what makes it real.
And they work efficiently because their communication is sorted ;)


One of the best products I have used.

## What can you do we with Discord
Join a server



![Join a server](/assets/images/discord/server.png)


## Discussion, Support and Issues
For general support and discussion of this project, please join the Discord server: [Discord Invite Link](https://discord.gg/B2cERQ5)

[![Discord Server](https://discordapp.com/api/guilds/552881714196774953/widget.png?style=banner2)](https://discord.gg/B2cERQ5)

To check known bugs and see planned changes and features for this project, please see the GitHub issues.

Found a bug we don't already have an issue for? Please report it in a new GitHub issue with as much detail as you can!

## Credits
* Creative | Fan Art | 2nd Place: Hieronymus7Z
* Creative | Merch | 1st Place: Calucifer