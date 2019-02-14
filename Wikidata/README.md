# Wikidata - Largest Crowd sources Knowledge Graph - Open Data
Wikidata is one of the many sister project of Wikimedia Foundation
![Wikimedia Foundation projects](../images/Screenshot_2019-02-14 Wikimedia.png)

## What is a Knowledge Graph 
Or a Knowledge Base to be more generic, but we tend to use Graph structure, hence many times used interchangebly as Knowledge Graph.
(Again, google calls it Knowledge Graph as Knowledge Graph)
When we refer to these, the following concepts are what we have in mind
* Some sort of formalization in terms of how we are representing our data (Ontology!)
* Data - in terms of Entities, events, relationships or any other formalization defined 
* Some Functions - in term of functions for maintaince, cleaning, freshness.
* Some Engine - in terms of a platform that helps us have these functions, make them run on the data we have


Some examples of these knowledge bases:
* Wikidata
* Google's Knowledge Graph
    * Freebase
* Microsft's Satori
* Wolfram Alpha


## Wikidata
> Wikidata is a document-oriented database, focused on items. Each item represents a topic (or an administrative page used to maintain Wikipedia) and is identified by a unique number, prefixed with the letter Q — for example, the item for the topic Douglas Adams is Q42 — known as a "QID". This enables the basic information required to identify the topic the item covers to be translated without favouring any language.

![wikidata sample](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Datamodel_in_Wikidata.svg/484px-Datamodel_in_Wikidata.svg.png)


As last update on this page, Wikidata has 54,905,015 data items!
If you want get started you self, learn more about how/what and even the why behind wikidata, I would strongly recommend [Wikidata Tour](https://www.wikidata.org/wiki/Wikidata:Tours) which is maintained by the community to help new people get started with Wikidata.


## Can we query it?
__SPARQL__,I mean Yes.
Yes you can query Wikidata using SPARQL. 

> SPARQL = An RDF Query Language

You could go as far as saying its like SQL for data in RDF specifications

Now what is RDF?
RDF is basically "Subject - Predicate - Object" triples.
RDF = Resource Description Framework
![RDF image](https://www.w3.org/2018/09/rdf-data-viz/test-ontology-visualization.svg)

Wikidata provides a beautiful tool for querying known as [Wikidata Query Service](https://query.wikidata.org/)

## Let build a query now.

* For the first query, lets simply get a count of people that have a spouse listed. (ever married)

```
#Query for Wikidata intro
SELECT (COUNT(?item) AS ?count) 
WHERE 
{
  ?item wdt:P31 wd:Q5.
  ?item wdt:P26 ?spouse.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
} 
```

You can do alot with these queries, [here](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples) is a list of examples queries listed. A must visit page of the internet.

\< A live query building session to follow \>



## Thanks and for further Communications
Thanks for going through this material, hope I was able to help in some form or way.

Any help, updating this page, or something broader would be highly appreciated.
Best place to communicate would be in order
* Contact me on Twitter @karx_brb
* Raise an issue on this Github repo, 
* Leave a message Discord. Our channel: [Akriya Discord](https://discord.gg/Ud5TuCr)
* Slack Channel Invite Link: [Invite](https://join.slack.com/t/akriya/shared_invite/enQtNDMwOTM2NjExMzQ0LTZmODYzZDUyNDYyMjhhNmNhMzk2MzVjY2NmZGM0YjNkYzViZTJjMDc2Nzg4MTA5NjAzOTQ1ZWZhMDc0OWI3OGU) 
* [Wikipedia Talk page](https://en.wikipedia.org/wiki/User_talk:Kaaro01)