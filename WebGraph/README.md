# W3C Workshop on Web Standardization for Graph Data
Creating Bridges: RDF, Property Graph and SQL

## This document
This document is to created to submit/forward my understanding, views and experience on the topic. I will break this down, into indivisual encounters/chapters. 
Also, this is also a call for allowing me to if possible, digitally attend the [W3C Workshop on Web Standardization for Graph Data](https://www.w3.org/Data/events/data-ws-2019/cfp.html)

## Introduction
I am deeply pationate about the very core of the concept, of formalizing our knowledge/data in form of a graph, which I do not need to justify to anyone keen enough to read this document.

During my college years, we talked about moving from a 'wall of text' to 'traversable graph', which was a neat enough for us to win a few hackathons.

Then I was fortunate enough to work for Bing's Satori Team, which as the team responsible in Microsoft for maintaining the Knowledge Graph Engine for all Open Data. During my time there I worked under the Data Curation Team.
This was my first experince of looking under the hood of a huge Graph Data base.

Later, I spent a breif time in one of the leading logistics startup in India. One of the previous devs  had modeled, their entire locations repository on Neo4j, a novel task, but implementations lacked. I took up this talk over a weekend, and as always, modeling such stuctured data into a formal graph was a hit.
Since then, I have been refering to Schema.org, as the base ontology set, to store my data.
It is not always possible to maintain a Graph DB for all the projects that I do. But the intutiveness that makes you think in SPO format (Subject Predicate Object) is always a boon.

## EduGraph - The college days
This was our first attempt at formalizing a data set in terms of a Graph DB.
The use-case we had was for an Edu-Tech company, and we proposed them to store their Courses as a Dependecy Graphs. Also we generated a few quizes for live demo, given such structuring.

Our core ask was to move away from a 'Wall of Text'.
Best 2 days of College. Well maybe.

## Satori - Bing's Knowledge Graph
Knowledge Graph for Open data.
I worked for this team as an Intern, then as an Industrial Project and then finally after college got picked as a full time.
This exeprince was when I really got to know about whats what.

During my interniship, the project was to Clean data -> to detect Inconsistencies in the Graph, then remove or rectify them.
A 4TB graph, engine with almost no upper compute limit, and such a task. I had an amazing internship. 
We ran loop detections on different properties, depth approximations for certain type of entity-property pairs and much more!

Later, I was involved in development for Editor's tooling, freshness pipeline, Impression calculations, etc.
This was also the time when the Industry was moving from away (had to) from Freebase, which meant working on getting various new sources, new pipelines and all the fun stuff.


## Wikidata - The Open book for a Knowledge Graph
Wikidata, now that I am not working for the corporate world, Wikidata provides me with the 'under the hood' exposure.
Writing SPARQL queries for answering queries like 'does being married have a co-relation with how long you live?' became a favorite pass-time for me.

I would like to say, Wikidata, the development, the community efforts, the discussions and the data set itself, provides a great __OPEN__ view to how such a system evolves, its needs, etc. There are many questions that the community on a daily basis takes care of and it is an engine, worth more eyeballs.

I have been attempting to write a small [introduction/engager for Wikidata](https://karx.github.io/Wikidata) if anyone is interested.


## Current Open Tool Kit
So the following toolkit has really enabled me to fullfill my whim of modeling/structuring things in a Graph
* Schema.org - The govering ontology
* Neo4j - A great tool for those who are a little phobic towards this concept.
    This really helps people wrap their head around the concept and the possiblities. Their Graphical Language - Cypher is very fun to teach
* RDF syntax - Well the document would have been incomplete without mentioning either RDF or OWL. Getting the idea of structuring things as Triples.
* Wikidata - A complete end to end engine + data + develeopment which is Open for us to be involved.


## Conclutions
Storing or Stucturing or Modelling things in terms of a Graph Data base is something that is Needed, not invented.
The evolution that we are seeing in this domain is one of the most facinating ones. And the use-cases and applications of such well structured data with the current compute abilities are mind-blowing.

Appologies for this, but I could not help myself from creating this.

![Graph Data Meme](https://i.imgflip.com/2u5b0a.jpg)


## Thanks and for further Communications
Thanks for going through this material, hope I was able to help in some form or way.

Any help, updating this page, or something broader would be highly appreciated.
Best place to communicate would be in order
* Contact me on Twitter @karx_brb
* Raise an issue on this Github repo, 
* Leave a message Discord. Our channel: [Akriya Discord](https://discord.gg/Ud5TuCr)
* Slack Channel Invite Link: [Invite](https://join.slack.com/t/akriya/shared_invite/enQtNDMwOTM2NjExMzQ0LTZmODYzZDUyNDYyMjhhNmNhMzk2MzVjY2NmZGM0YjNkYzViZTJjMDc2Nzg4MTA5NjAzOTQ1ZWZhMDc0OWI3OGU) 
