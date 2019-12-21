## AdEngine - SOW
Document prepared by Kartik Arora

## Table of Content

* Executive Summary
* Project Definition
* Devices
* Web/Soft-ware
* Maintenance
* Exclusions
* Deliverables
* Customer Responsibilities
* Investment and Cost
* Acceptance Criteria
* Assumptions
* IPR
* Approvals


## Executive Summary
This documentation is to serve as a 'Statement of Work' or SOW for the design and development of AdEngine POC to enable and enhance targeted advertising on TVs. 

The advancement in the field of IoT  Networks, Computing and Data Science has made possible Integrated systems which enable new experiences and solutions possible in the Digital Media space.
Such a system would include a means to capture, catalogue and analyze data, along with tools to enforce 'business logic'.

This SOW summarizes an AdEngine system, with our own `on-premise` Hardware devices running AdEngine edge device firmware, which would include (at least) the following:
* Local content management
* Realtime stream processing for markers (Module no 1.4)
* Uplinking with AdEnging cloud services
* Local sensor controller

Akriya Technologies will work with AdEngine to:

* Designing and Development of the AdEngine Devices Infrastructure
* Designing and Development the AdEngine Content Distribution Architecture
* Designing and Development of on-premise devices
* Deploy said systems for AdEngine
* Provide documentation of the new system
* Knowledge Transfer/Integrate 

Akriya Technologies proposes to design, develop and provide installation of v1.0 of the proposed system to cater for 5 personas.
This activity will require 8-10 weeks. The estimated cost for this activity would be 4 lakhs INR plus additional charges including travel, server rental and hardware costs.

The Value Proposition of using Akriya Technologies for this project are:
* Proven engineering techniques for making Integrated systems.
* Leveraging our experience in working with IoT toolkit (ESP).
* Data Architecture and Solution experience
* Using our subject matter experts to complete the project quickly. Rapid project completion minimizes disruptions and allows organizations to realize cost-saving quickly.

## Project Definition
The AdEngine project is broken down into the following 5 modules, which would be developed in the course of this work.
These modules are abstracted based on functional and operating hardware (cloud functions, user functions and on-premise functions).

### 1.1 DTH Piggybanking H/W 
This module is the Hardware device with Ad delivery firmware running which has to interface to the TV.
The module takes input from the DTH set-top box, AdEngine Cloud services and Local memory cache to render output to the TV.

The following two approaches have been discussed as of now for taking `INPUT` from a DTH set-top box:
* Leveraging USB-interface on DTH Setup boxes
* Bridging HDMI-out from DTH Setup box


Choice of Hardware is to be determined based on compute and network consumption. Current development to start from Raspberry Pi Zero interfaced with [HDMI to CSI-2 Bridge](https://www.mouser.in/Embedded-Solutions/Interface-Modules/_/N-5g1o?P=1y9f2kt)

### 1.2 Device and Identity Management
This module is responsible for providing a super-set of communication and access provisioning systems that provide easy management of user devices and their accounts, and others those who need that information.
This would include:
* Implementations and deployment of Communication channel for devices (MQTT)
* User account management ( Firebase )

### 1.3 Content Distribution System
This module is responsible for collecting and storing Ad data, and distributing to all `on-premise` devices, based on user, geographic position, and AdEngine specific preferences.

* This would include a web-based app for uploading and managing content.
* Current approach uses S3 bucket to house large media files.
* Media transcoding (Out-of-scope) 

### 1.4 Real-time Stream Processing
The module is responsible for taking Real-time decisions of which add to play, based on factors like, user persona, location, time, demand, geographic and demographic data.

This Module would be running only on `on-premise` devices, without sharing customer sensitive information to the cloud.
For the POC we would be targeting 5 distinct personas.

### 1.5 Marker Based Ad placement
This module is a collection of marker-based interrupt mechanisms that would facilitate handshake for where and when to place content.

There are a few proposed mechanisms for the current POC
* inaudible ultrasonic signals - sound markers
* on-screen overlay banners
* fixed timetables

## Delivery Scope
### Devices/HW

* On-Premise Module

```
Data to Capture:    NIL

```


## Web/Software
* Data SDK / APIs for AdEngine Telemetry
We will be recording and cataloguing the real-time telemetry of the AdEngine, AdEngine on-premise devices and Users.
This would include a query endpoint, to query this set.

* Dashboard - Admin (Barebones)
Admin Interface to overlook and manage the system.
    * Views
        * User View
        * Devices view
        * Content page

* User App (Out-of-scope)

## Maintenance
To be maintained for 2 months and then rediscuss based on new requirements and learnings.

## Exclusions
The followings are excluded from the project scope
* The packages used and maintained by Akriya Technologies for interfacing with IoT Devices.
* Open Source Software means publicly available software that may be utilized pursuant and subject to the terms of an "open source" or similar license, including without limitation the "Ruby License," the "MIT License," the "Apache License" and the "GNU General Public License." Company understands and agrees that Consultant may, at Consultant's discretion, make use of libraries from various Open Source Software products during the course of work. We may submit back to such libraries any improvements ("patches") made to the Open Source Software during the course of work, as long as the submission of such patches violates neither the conditions in this Section nor the Confidentiality provisions.

## Deliverables
The deliverables are listed below.
* Devices. 
To be installed in 4 AdEngine facilities, and 50% spare**.

* Software
Access top-level Git repositories for the SDK, on-premise firmware, and admin interface package.

* Documentation and graphical depictions of the new proposed AdEngine system.


## Customer Responsibilities
* The nature of this engagement dictates that Akriya Technologies receive a frequent and enthusiastic response from the appropriate personnel.
* A weekly review between the Akriya Technologies consultant and the AdEngine project lead or his designate will ensure that the expectations of this engagement are met.
* Client will assign a key contact who will be responsible for providing Akriya Technologies with information, access to personnel, and facility access.
* Client will provide a work area space with desk, chair, Internet access for use by Akriya Technologies to conduct project business while working on-site.

## Investment and Cost
* Man-hour required: 2 months: 4 lakh INR

* Hardware cost (if required) to be paid by AdEngine
    
* Server/Web hosting charges:
    * 60$ / month = 4000 INR

*Bill separately for travel costs will be billed at actual cost and will not exceed 10,000 INR for the entire project.

 * Payment Schedule

| Milestone                                 | Percentage    | Amount    |
| -------------                             |:-------------:| -----:    |
| Requirement Finalization                  | 25%            | 1,00,000 INR|
| Module 1.1 + Module 1.5          | 50%           | 1,00,000 INR|
| Module 1.3 + Module 1.2            | 75%           | 1,00,000 INR|
| Modele 1.4                   | 100%          | 1,00,000 INR|


Devices cost to be paid on the day of installation.
Server cost to be paid directly or at the start of each month.
Travel reimbursements as and when declared.

## Acceptance Criteria
At the conclusion of this evaluation, all deliverables for this phase will be presented to AdEngine for review.

AdEngine or its representative will have five business days from the date of delivery of any document that is a deliverable to review it and request any changes.  If Akriya Technologies does not receive notification of any required changes within this period, the document will be deemed to have been accepted without modification and will be reissued as a final copy.

If Akriya Technologies is notified by AdEngine, within the above time frame, of any changes required, Akriya Technologies will within two business days of such notification implement those changes as have been agreed between the parties.  A final copy of the document will then be submitted to AdEngine.

## Assumptions
* General
    * All documentation created for this project will be available in hard copy and electronic format.
    * Any modifications to the scope of work will be handled through a change control process and will be agreed to by both parties.

* Commercial
    * Additional costs may be incurred where any delay not under the control of Akriya Technologies that causes Akriya Technologies personnel to not fulfil their scheduled tasks.
    * An authorized delegate of AdEngine will be available at the time of completion of the build phase so that all documentation can be accepted and signed.
    * Additional costs may be incurred where any work scheduled to be undertaken by Akriya Technologies is postponed by AdEngine after 24 hours of its commencement.
    * All changes to the schedule or technical requirements must be provided to Akriya Technologies in written format. Email is included as written format. Receipt of all correspondence should be confirmed by phone wherever possible.
    * AdEngine has accepted the costs/times estimate as detailed in this document
    * AdEngine has accepted the Akriya Technologies standard terms and conditions linked.

## Intellectual Property
Unless otherwise agreed in writing, AdEngine acknowledges that all intellectual property rights attaching to the products or arising out of the provision of services are and will remain the property of Akriya Technologies (or its suppliers, where such rights are owned by that supplier).

The software will be licensed to AdEngine on the terms of the relevant license agreement provided with the product or as otherwise agreed between Akriya Technologies and AdEngine in writing.


## Approved by
Name:   
Date:   
Position:   

[AdEngine system doc](/AdEngine/requirements)
