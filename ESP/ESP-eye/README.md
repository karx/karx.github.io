## ESP-Eye | SOW
Document prepared by Kartik Arora and Ashtam Singh

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
This documentation is to serve as a 'Statement of Work' or SOW for the design and development of ESP-Eye POC to enable Finger Print Reader and Recognition System.

The advancement in the field of IoT  Networks, Computing and Data Science has made possible Integrated systems which enable new experiences and solutions possible in the *Digital Media* space.
Such a system would include a means to capture, catalogue and analyze data, along with tools to enforce 'business logic'.

This SOW summarizes an ESP Camera module for the POC, with a firmware to enable the following:
* Camera Interface with SP9250
* 3fps streaming output
* Transcoding of image to RAW-8

Akriya Technologies will work with ESP-Eye to:

* Designing and Development of the ESP-Eye device
* Provide documentation of the module
* Knowledge Transfer/Integrate 

Akriya Technologies proposes to design and develop this module, with ESP32 using SP9250 output on Serial at 3fps.
This activity will require 2 weeks. The estimated cost for this activity would be 50 thousand INR plus additional charges including travel, server rental and hardware costs.


The Value Proposition of using Akriya Technologies for this project are:
* Proven engineering techniques for making Integrated systems.
* Leveraging our experience in working with IoT toolkit (ESP).
* Data Architecture and Solution experience
* Using our subject matter experts to complete the project quickly. Rapid project completion minimizes disruptions and allows organizations to realize cost-saving quickly.

## Project Definition
The ESP Eye project is broken down into the following 3 modules, which would be developed in the course of this work.
These modules are abstracted based on functional and operating hardware.

### 1.1 Camera Interface with SP9250
This module is responsible for interfacing with the Camera Module.
It should allow:
* Using I2S Interface
* No FIFO configration

[DataSheet fo SP9250](http://www.superpix.com.cn/en/xiazai/SP9250.pdf)

![Image of SP9250](http://www.superpix.com.cn/upload/2016012751295425.jpg)

### 1.2 streaming output
This module is responsible for providing a steady 3fps output from the Camera Module to 
* Option 1: Serial
* Option 2: Simple Web Server

### 1.3 Transcoding to RAW-8
This module is responsible for Transcoding the MIPI 1 lane data stream from camera to RAW-8 encoding before sending on wire.

## Delivery Scope
### Devices/HW

* On-Premise Module

```
Data to Capture:    Camera Input (SP9250)


Output: Serial Streaming Output (Raw-8 at 3fps)

```


## Web/Software
* Device Firmware
ESP32 firmware which used modules 1.1, 1.2 and 1.3 as described above.

## Maintenance
To be maintained for 1 months and then rediscuss based on new requirements and learnings.

## Exclusions
The followings are excluded from the project scope
* The packages used and maintained by Akriya Technologies for interfacing with IoT Devices.
* Open Source Software means publicly available software that may be utilized pursuant and subject to the terms of an "open source" or similar license, including without limitation the "Ruby License," the "MIT License," the "Apache License" and the "GNU General Public License." Company understands and agrees that Consultant may, at Consultant's discretion, make use of libraries from various Open Source Software products during the course of work. We may submit back to such libraries any improvements ("patches") made to the Open Source Software during the course of work, as long as the submission of such patches violates neither the conditions in this Section nor the Confidentiality provisions.

## Deliverables
The deliverables are listed below.
* Devices. 
To demo and handover 2 ESP-Eye, with latest firmware build.

* Software
Access top-level Git repositories for the SDK and device firmware.

* Documentation and graphical depictions of the new ESP-Eye system.


## Customer Responsibilities
* The nature of this engagement dictates that Akriya Technologies receive a frequent and enthusiastic response from the appropriate personnel.
* A weekly review between the Akriya Technologies consultant and the ESP-Eye project lead or his designate will ensure that the expectations of this engagement are met.
* Client will assign a key contact who will be responsible for providing Akriya Technologies with information, access to personnel, and facility access.
* Client will provide a work area space with desk, chair, Internet access for use by Akriya Technologies to conduct project business while working on-site.

## Investment and Cost (revised)
* Time required: 2 weeks: 50 thousand INR (estimated 80 man-hours)

<!-- * Hardware cost (if required) to be paid by ESP-Eye -->
    
<!-- * Server/Web hosting charges:
    * 60$ / month = 4000 INR -->

<!-- * Bill separately for travel costs will be billed at actual cost and will not exceed 10,000 INR for the entire project for movement within NCR. (upto 10 meetings) -->

 * Payment Schedule

| Milestone                                 | Percentage    | Amount    | Time period from Start
| -------------                             |:-------------:| -----:    | ----- | 
| Requirement Finalization + SOW acceptance                 | 40%            | 20,000 INR| 0 day | 
| Module 1.1 + 1.2 + 1.3         | 60%           | 30,000 INR| 15 days |  


Devices cost to be paid on the day of installation.
Server cost to be paid directly or at the start of each month.
Travel reimbursements as and when declared.

## Acceptance Criteria
At the conclusion of this evaluation, all deliverables for this phase will be presented to ESP-Eye for review.

ESP-Eye or its representative will have five business days from the date of delivery of any document that is a deliverable to review it and request any changes.  If Akriya Technologies does not receive notification of any required changes within this period, the document will be deemed to have been accepted without modification and will be reissued as a final copy.

If Akriya Technologies is notified by ESP-Eye, within the above time frame, of any changes required, Akriya Technologies will within two business days of such notification implement those changes as have been agreed between the parties.  A final copy of the document will then be submitted to ESP-Eye.

## Assumptions
* General
    * All documentation created for this project will be available in hard copy and electronic format.
    * Any modifications to the scope of work will be handled through a change control process and will be agreed to by both parties.

* Commercial
    * Additional costs may be incurred where any delay not under the control of Akriya Technologies that causes Akriya Technologies personnel to not fulfil their scheduled tasks.
    * An authorized delegate of ESP-Eye will be available at the time of completion of the build phase so that all documentation can be accepted and signed.
    * Additional costs may be incurred where any work scheduled to be undertaken by Akriya Technologies is postponed by ESP-Eye after 24 hours of its commencement.
    * All changes to the schedule or technical requirements must be provided to Akriya Technologies in written format. Email is included as written format. Receipt of all correspondence should be confirmed by phone wherever possible.
    * ESP-Eye has accepted the costs/times estimate as detailed in this document
    * ESP-Eye has accepted the Akriya Technologies standard terms and conditions linked.
    * Any deviationns, technical or commercial , shall be mutually discussed and agreed before implementation.

## Intellectual Property
Unless otherwise agreed in writing, ESP-Eye acknowledges that all intellectual property rights attaching to the products or arising out of the provision of services are and will remain the property of Akriya Technologies (or its suppliers, where such rights are owned by that supplier).

The software will be licensed to ESP-Eye on the terms of the relevant license agreement provided with the product or as otherwise agreed between Akriya Technologies and ESP-Eye in writing.


## Approved by
Name:   
Date:   
Position:   

[ESP-Eye system doc](/ESP-Eye/requirements)
