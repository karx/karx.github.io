## THe MQTT Conventions Document
As prepared by Kartik Arora

## Summary
This document is to highlight, document and improve our practices while designing MQTT Topic in our Deployments, keeping in mind 
* Resource optimizations
* Use-case possibilities
* Empower Composability
* Provide Granularity
* Improve Verbosity

MQTT concepts and terminologies: https://docs.emqx.io/broker/v3/en/protocol.html

## Broad Categorization
These topics are broadly divided into two types. Administrative and Product Topics
### Administrative Topics
These are topics on which administrative, metadata flows.

Data and events that are essential for the upkeep of the infrastructure itself. In our case,
* our region-wise presence topics: Kento/presence
* OTA topics
* Reset topic

The general form of these Admin Topics will be:
`CURRENT_REGION`/presence/<`DEVICE_ID`>

The `CURRENT_REGION` would always be the first stub for a developer/custom created administrative topic.

### Product Topics
These are topics on which product specific information flow, the data/information that drives the features/utility of the product.

The message update topic: `ROOT_STUB`/`PRODUCT_STUB`/<`DEVICE_ID`>/`ACTION_STUB`

`ROOT_STUB`: Something that helps us easily identify the product line. example: digitalicon, homeswitch
`PRODUCT_STUB`: To identify the batch of the product line. Example: name of owner, name of usecase, mesh_id
`DEVICE_ID`: The unique id to each h/w device, can use: MAC address, or IMEI number. MAC prefered as on date.
`ACTION_STUB`: name of event/action to trigger or log.


## Recommendations/Best Practices
* Topics only lowercase, numbers and dashes.

* Topic stub from Left to Right:: General to specific

* While Subscribing, multi-level subscriptions (using #) are highly discouraged.

* Use MAC address as DEVICE_ID

## References
* https://d1.awsstatic.com/whitepapers/Designing_MQTT_Topics_for_AWS_IoT_Core.pdf
* https://docs.emqx.io/broker/v3/en/design.html#routing-layer
