## GHealth - SOW
Document prepared by Kartik

## Table of Content

* Executive Summary
* Project Defination
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
This documentation is to serve as a 'Statement of Work' or SOW for implementing the Digital infrastucture and products required for GHealth opertaions.

Networks, Computing and Data Science has made possible Integrated systems that can really empower business.
Such a system would include a means to capture, catalog and analyze data, along with tools to enforce 'business logic'.

Akriya Technologies will work with GHealth to:

* Designing the GHealth Services Architecture
* Design and Development of GHealth Customer Endpoints
* Develop and Engineer the GHealth Operational Toolkit
* Deployments of GHealth infrstucture
* Provide documentation of the new system
* Knowledge Transfer of GHealth 

Akriya Technologies proposes to design, develop and deploy v1.0 of the proposed system to cater for 1000-2000 Facilities +and 10,000+ users.
This activity will require 3 months (~12 weeks). The estimated cost for this activity would be 6 lakhs INR.

The Value Proposition of using Akriya Technologies for this project are:
* Proven engineering techniques for making Integrated systems.
* Leveraging our experience in working with Web and Mobile Technologies.
* Data Architecture and Solution experience
* Using our subject matter experts to complete the project quickly. Rapid project completion minimizes disruptions and allows organizations to realize cost saving quickly.

## Project Defination
Based on the project overview, the project can be devided into the following modules for abstractions:

* GHealth Services Module
    This is to include the Facilites, Services, and or any Events happening at an affiliated GHealth Facility.
    - Viewing, Filtering and Exploring feature for end-users to explore available GHealth facilties
    - Event management features like - Bookings, reminders and RSVP.

* GHealth Products Module
    This would include an e-commerce like facilities to faciliate sales of GHealth branded products

* GHealth e-Trainer Module
    A bot system that helps users through out the GHealth experience. It would take care of the following responsibilites
    - Onboarding of users
    - Daily reporting
    - Live training instructions
    - FAQs
    - Feedback and Escalations

* GHealth Subcription + Identity Management
    Module responsible for managing diffrent users on our platfrom, ranging for different customer categories to operational staff.


## Software



## Web/Software
* Data SDK / APIs for GHealth
We will be recording and cataloging the real time telemetry of the SmartBike.
This would include a query endpoint, to query this set.
Also, APIs that we would consume to make the User Journey possible (like number of bikes available around a geolocations)

* Dashboard - Admin
Admin Interface to overlook and manage the system.
    * Views
        * User View
        * Bike view
        * Dashboard page
        * Transactions Page

    * Notifications
        * Bike fencing
        * Requirements if any

    * Admin privleges
        * Options to block users
        * Options to manage status of Bikes

Design/Requirements for this dashboard to be agreed upon prior to any further development.
![Admin App Flow](/images/SmartBikeAdmin.png)

* User App
![User App Flow](/images/SmartBikeUser.png)


## Maintenance
To be maintained for 6 months and then rediscuss based on new requirements and learnings.

## Exclusions
The followings are excluded from the project scope
* The packages used and maintained by Akriya Technologies for interfacing with IoT Devices.

## Deliverables
The deliverables are listed below.
* Devices. 
To be installed in 1 SmartBike facility, and 50% spare**.

* Software
Access top level Git repositories for the Dashboard, mobile Apps, and admin interface package.

* Documentation and graphical depictions of the new proposed SmartBike system.


## Customer Responsibilities
* The nature of this engagement dictates that Akriya Technologies receive a frequent and enthusiastic response from the appropriate personnel.
* A weekly review between the Akriya Technologies consultant and the SmartBike project lead or his designate will ensure that the expectations of this engagement are met.
* Client will assign a key contact who will be responsible for providing Akriya Technologies with information, access to personnel, and facility access.
* Client will provide a work area space with desk, chair, Internet access for use by Akriya Technologies to conduct project business while working on-site.

## Investment and Cost
* Man-hour required: 1 months: 2 lakh INR

* Hardware cost (if required) to be paid by SmartBike
    
* Server/Web hosting charges:
    * 60$ / month = 4000 INR

*Bill separately for travel costs will be billed at actual cost and will not exceed 10,000 INR for the entire project.

 * Payment Schedule

| Milestone                                 | Percentage    | Amount    |
| -------------                             |:-------------:| -----:    |
| Requirement Finalization                  | 0%            | 50,000 INR|
| Telemetry Systems Demo           | 33%           | 50,000 INR|
| Dashboard + App shandoaver            | 66%           | 50,000 INR|
| Final Delivery   s                         | 100%          | 50,000 INR|

Devices cost to be paid on the day of installation.
Server cost to be paid directly or at the start of each month.
Travel reimbursements as and when declared.

## Acceptance Criteria
At the conclusion of this evaluation, all deliverables for this phase will be presented to SmartBike for review.

SmartBike or its representative will have five business days from the date of delivery of any document that is a deliverable to review it and request any changes.  If Akriya Technologies does not receive notification of any required changes within this period, the document will be deemed to have been accepted without modification and will be reissued as a final copy.

If Akriya Technologies is notified by SmartBike, within the above time frame, of any changes required, Akriya Technologies will within two business days of such notification implement those changes as have been agreed between the parties.  A final copy of the document will then be submitted to SmartBike.

## Assumptions
* General
    * All documentation created for this project will be available in hard copy and electronic format.
    * Any modifications to the scope of work will be handled through a change control process and will be agreed to by both parties.

* Commercial
    * Additional costs may be incurred where any delay not under the control of Akriya Technologies that causes Akriya Technologies personnel to not fulfill their scheduled tasks.
    * An authorized delegate of SmartBike will be available at the time of completion of the build phase so that all documentation can be accepted and signed.
    * Additional costs may be incurred where any work scheduled to be undertaken by Akriya Technologies is postponed by SmartBike after 24 hours of its commencement.
    * All changes to the schedule or technical requirements must be provided to Akriya Technologies in written format. Email is included as written format. Receipt of all correspondence should be confirmed by phone wherever possible.
    * SmartBike has accepted the costs/times estimate as detailed in this document
    * SmartBike has accepted the Akriya Technologies standard terms and conditions linked.

## Intellectual Property
Unless otherwise agreed in writing, SmartBike acknowledges that all intellectual property rights attaching to the products or arising out of the provision of services are and will remain the property of Akriya Technologies (or its suppliers, where such rights are owned by that supplier).

The software will be licensed to SmartBike on the terms of the relevant license agreement provided with the product or as otherwise agreed between Akriya Technologies and SmartBike in writing.


## Approved by
Name:   
Date:   
Position:   


[SmartBike system doc](/SmartBike/requirements)
