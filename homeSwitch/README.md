# Statement of Work - homeSwitches (Protoype Development for Initial User Behavior Testing)



## Table of Content

* Executive Summary
* Project Defination
* Devices
* Web/Soft-ware
* Maintance
* Exclusions
* Deliverables
* Customer Responsibilities
* Investment and Cost
* Acceptance Criteria
* Assumptions
* IPR
* Approvals



## Executive Summary
This documentation is to serve as a 'Statement of Work' or SOW for developing and implementing a homeSwitch System for Abacus Services, to enable them goto Market Product. The advancement in the field of IoT, Networks, Computing and Data Science has made possible Integrated systems that can really help business.
Such a system would include a means to capture, catalog and analyze data, along with tools to enforce 'business logic'.

Akriya Technologies will work with Abacus Services to:

* Designing the homeSwitch System
* Design and Develop a Mobile Application
* Desing and Develop firmware for homeSwitch devices.
* Documentation of homeSwitch System


The Value Proposition of using Akriya Technologies for this project are:
* Proven engineering techniques for making Integrated systems.
* Leveraging our experience in working with IoT toolkit (ESP) to bootstrap your effort. 
* Using our subject matter experts to complete the project quickly. Rapid project completion minimizes disruptions and allows organizations to realize cost saving quickly.

## Delivery Scope
The scope of this project is to design, implement and deliver an end-user consumable product/system for homeSwitches. This would include
 - A interface for the end-user: A mobile App
 - In-wall devices: Arduino based devices
 - Process definations for Installation, mantaince and debugging

The homeSwitch system is proposed to have no dependencies to the internet, and should be a full-funtional system while offline.
The feasibility of few techniques to have such a system, would be conducted while the designing and development of the system.

## Devices

* Offline - Indivisual Hotspot Devices

```
    Max connected devices to App: 1
```
To connect to this device, we hop into the indivisual operating channel of the device.


* In-Facility Device

```
Data to Capture:    Humidity
                    Temperature
                    Number of people*
                    
```

* Equipment Interfaces

    * Heatpump Controller:

    ``` 
    Data to Capture:    In-let temprature of water
                        Outlet temperature of the water
                        Operating hours
    ``` 


    * Geyser:

    ```
    Data to Capture:    Operating hours
                        In-let temprature of water
                        Outlet temprature of water
    ```


    * Water Motors:

    ```
    Data to Capture:    Operating hours
    ```


    * Filter Unit

    ```
    Data to Capture:    Operating hours
                        Operating state*
    ```

## Web/Software
* Admin SDK / APIs for Devices
Native packages to interact with the devices. 

* Dashboard
A user interface exposed as a PWA on any domain required by Fitso. 
(It would be recommended to use Admin SDK or APIs in Fitso's existing dashboards.)
Design/Requirements for this dashboard to be agreed upon prior to any further development.

* On Premise Portal
()
A UI to be displayed on a screen/system inside the facility for the on-premise staff.

## Maintenance
To be maintained for 6 months and then rediscuss based on new requirements and learnings.

## Exclusions
The followings are excluded from the project scope
* The packages used and maintained by Akriya Technologies for interfacing with IoT Devices.

## Deliverables
The deliverables are listed below.
* Devices. 
To be installed in 1 Fitso facility, and 50% spare**.

* Software
Access top level Git repositories for the Dashboard, on-premise portal, and admin interface package.

* Documentation and graphical depictions of the new proposed Smart Fitso Facility System.


## Customer Responsibilities
* The nature of this engagement dictates that Akriya Technologies receive a frequent and enthusiastic response from the appropriate personnel.
* A weekly review between the Akriya Technologies consultant and the Fitso project lead or his designate will ensure that the expectations of this engagement are met.
* Client will assign a key contact who will be responsible for providing Akriya Technologies with information, access to personnel, and facility access.
* Client will provide a work area space with desk, chair, Internet access for use by Akriya Technologies to conduct project business while working on-site.

## Investment and Cost
* Man-hour required: 2 months: 2 lakh INR

* Hardware required: On Cost  : 
    * In Pool Device : 25,000 INR
    * In Facility Device : 5,000 INR
    * Heatpump Controller: 5,000 INR
    * Geyser : 2,000 INR
    * Water Motors : 2,500 INR
    * Filter Unit : 5,000 INR
    * On premise Wifi/Internet Router : 2,000 INR
    
* Server/Web hosting charges:
    * 60$ / month = 4000 INR

*Bill separately for travel costs will be billed at actual cost and will not exceed 10,000 INR for the entire project.

 * Payment Schedule

| Milestone                                 | Percentage    | Amount    |
| -------------                             |:-------------:| -----:    |
| Requirement Finalization                  | 0%            | 50,000 INR|
| First 3 device Installation               | 33%           | 50,000 INR|
| Dashboard + Software handoaver            | 66%           | 50,000 INR|
| Final Delivery                            | 100%          | 50,000 INR|

Devices cost to be paid on the day of installation.
Server cost to be paid directly or at the start of each month.
Travel reimbursements as and when declared.

## Acceptance Criteria
At the conclusion of this evaluation, all deliverables for this phase will be presented to Fitso for review.

Fisto or its representative will have five business days from the date of delivery of any document that is a deliverable to review it and request any changes.  If Akriya Technologies does not receive notification of any required changes within this period, the document will be deemed to have been accepted without modification and will be reissued as a final copy.

If Akriya Technologies is notified by Fitso, within the above time frame, of any changes required, Akriya Technologies will within two business days of such notification implement those changes as have been agreed between the parties.  A final copy of the document will then be submitted to Fitso.

## Assumptions
* General
    * All documentation created for this project will be available in hard copy and electronic format.
    * Any modifications to the scope of work will be handled through a change control process and will be agreed to by both parties.

* Commercial
    * Additional costs may be incurred where any delay not under the control of Akriya Technologies that causes Akriya Technologies personnel to not fulfill their scheduled tasks.
    * An authorized delegate of Fitso will be available at the time of completion of the build phase so that all documentation can be accepted and signed.
    * Additional costs may be incurred where any work scheduled to be undertaken by Akriya Technologies is postponed by Fitso after 24 hours of its commencement.
    * All changes to the schedule or technical requirements must be provided to Akriya Technologies in written format. Email is included as written format. Receipt of all correspondence should be confirmed by phone wherever possible.
    * Fitso has accepted the costs/times estimate as detailed in this document
    * Fitso has accepted the Akriya Technologies standard terms and conditions linked.

## Intellectual Property
Unless otherwise agreed in writing, Fitso acknowledges that all intellectual property rights attaching to the products or arising out of the provision of services are and will remain the property of Akriya Technologies (or its suppliers, where such rights are owned by that supplier).

The software will be licensed to Fitso on the terms of the relevant license agreement provided with the product or as otherwise agreed between Akriya Technologies and Fitso in writing.


## Approved by
Name:   
Date:   
Position:   
