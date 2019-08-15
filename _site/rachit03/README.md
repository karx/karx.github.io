## beyouID - SOW
Document prepared by Kartik

## Table of Content

* Executive Summary
* Project Definition
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
This documentation is to serve as a 'Statement of Work' or SOW for the redesign and development efforts for the beyouID App and web view.

Networks, Computing and Data Science has made possible Integrated systems that can really empower business.
Such a system would include a means to capture, catalogue and analyze data, along with tools to enforce 'business logic'.

Akriya Technologies will work with beyouID to:

* Designing the beyouID Services Architecture
* Design and Development of beyouID Customer Endpoints
* Develop and Engineer the beyouID Operational Toolkit
* Deployments of beyouID infrastructure
* Provide documentation of the new system
* Knowledge Transfer of beyouID 

Akriya Technologies proposes to design, develop and deploy v1.0 of the proposed system to cater for 1000-2000 Facilities +and 10,000+ users.
This activity will require 3 months (~12 weeks). The estimated cost for this activity would be 5 lakhs INR.

The Value Proposition of using Akriya Technologies for this project are:
* Proven engineering techniques for making Integrated systems.
* Leveraging our experience in working with Web and Mobile Technologies.
* Data Architecture and Solution experience
* Using our subject matter experts to complete the project quickly. Rapid project completion minimizes disruptions and allows organizations to realize cost saving quickly.

## Project Definition
Based on the project overview, the project can be divided into the following modules for abstractions:

* beyouID Services Module
    This is to include the Facilities, Services, and or any Events happening at an affiliated beyouID Facility.
    - Viewing, Filtering and Exploring feature for end-users to explore available beyouID facilities
    - Event management features like - Bookings, reminders and RSVP.

* beyouID Products Module
    This would include e-commerce like facilities to facilitate sales of beyouID branded products

* beyouID e-Trainer Module
    A bot system that helps users throughout the beyouID experience. It would take care of the following responsibilities
    - Onboarding of users
    - Daily reporting
    - Live training instructions
    - FAQs
    - Feedback and Escalations

* beyouID Subcription + Identity Management
    The module is responsible for managing different users on our platform, ranging for different customer categories to operational staff.


## Software

* Data SDK / APIs for beyouID
The beyouID Engine would expose all the APIs and endpoints used for creating the beyouID System.
This would include a query endpoint, to query facilities, events and products.
Also, these APIs would make possible to have realtime bot responses.

* Dashboard - Admin
The admin dashboard would be exposed as a Web App, with identity management.
Admin Interface to overlook and manage the system.
    * User View
    * Facilites Management
    * Products Management
    * Booking Management
    * Finance Management


* User App
This would be exposed as a Mobile App on both Android and iOS.
The mobile app would include the following
    * Onboarding (exposed as a bot)
    * Facilities exploration with geolocation
    * Events exploration and booking
    * e-commerce experience to buy Products
    * Reporting and companion for beyouID system (exposed as a bot)
    * Subscription management


## Maintenance
To be maintained for 6 months and then rediscuss based on new requirements and learnings.

## Exclusions
The followings are excluded from the project scope
* The packages used and maintained by Akriya Technologies for interfacing with IoT Devices.

## Deliverables
The deliverables are listed below.

* Software
Access top level Git repositories for the Dashboard, mobile Apps, and admin interface package.

* Documentation and graphical depictions of the new proposed beyouID system.


## Customer Responsibilities
* The nature of this engagement dictates that Akriya Technologies receive a frequent and enthusiastic response from the appropriate personnel.
* A weekly review between the Akriya Technologies consultant and the beyouID project lead or his designate will ensure that the expectations of this engagement are met.
* Client will assign a key contact who will be responsible for providing Akriya Technologies with information, access to personnel, and facility access.
* Client will provide a work area space with desk, chair, Internet access for use by Akriya Technologies to conduct project business while working on-site.

## Investment and Cost
* Man-hour required: 3 months: 5 lakh INR

* Hardware cost (if required) to be paid by beyouID
    
* Server/Web hosting charges:
    * 60$ / month = 4000 INR

* Travel Cost
    * Local travel : Rs 10/km
    * Outstation: On actuals

 * Payment Schedule

| Milestone                                 | Time    | Amount    |
| -------------                             |:-------------:| -----:    |
| Requirement Finalization                  | Week 1           | 25,000 INR|
| Digital Flow Approval                     | Week 2           | 50,000 INR|
| Mobile + Admin app schematic approval     | Week 3           | 50,000 INR|
| Bot schematic approval (~Month 1 end)     | Week 4           | 50,000 INR|
| Month 2 Review (Facility Service + Identity Mangement)    | Week 5-6-7-8 | 1,50,000 INR|
| Month 3 Review (e-Trainer + Product Module)               | Week 9-10-11-12 | 1,50,000 INR|
| Final Review + Knowledge Transfer                         | Week 13             | 25,000 INR|

Server cost to be paid directly or at the start of each month.
Travel reimbursements as and when declared.

## Acceptance Criteria
At the conclusion of this evaluation, all deliverables for this phase will be presented to beyouID for review.

beyouID or its representative will have five business days from the date of delivery of any document that is a deliverable to review it and request any changes.  If Akriya Technologies does not receive notification of any required changes within this period, the document will be deemed to have been accepted without modification and will be reissued as a final copy.

If Akriya Technologies is notified by beyouID, within the above time frame, of any changes required, Akriya Technologies will within two business days of such notification implement those changes as have been agreed between the parties.  A final copy of the document will then be submitted to beyouID.

## Assumptions
* General
    * All documentation created for this project will be available in hard copy and electronic format.
    * Any modifications to the scope of work will be handled through a change control process and will be agreed to by both parties.

* Commercial
    * Additional costs may be incurred where any delay not under the control of Akriya Technologies that causes Akriya Technologies personnel to not fulfil their scheduled tasks.
    * An authorized delegate of beyouID will be available at the time of completion of the build phase so that all documentation can be accepted and signed.
    * Additional costs may be incurred where any work scheduled to be undertaken by Akriya Technologies is postponed by beyouID after 24 hours of its commencement.
    * All changes to the schedule or technical requirements must be provided to Akriya Technologies in written format. Email is included as written format. Receipt of all correspondence should be confirmed by phone wherever possible.
    * beyouID has accepted the costs/times estimate as detailed in this document
    * beyouID has accepted the Akriya Technologies standard terms and conditions linked.

## Intellectual Property
Unless otherwise agreed in writing, beyouID acknowledges that all intellectual property rights attaching to the products or arising out of the provision of services are and will remain the property of Akriya Technologies (or its suppliers, where such rights are owned by that supplier).

The software will be licensed to beyouID on the terms of the relevant license agreement provided with the product or as otherwise agreed between Akriya Technologies and beyouID in writing.


## Approved by
Name:   
Date:   
Position:   


beyouID_Redesign_07.09.19.sketch
Here's the final design.

Please note there are two pieces -- the app, and the web profile view. Please look to the current app for what is currently implemented. There is VERY LITTLE NEW functionality in these designs. Almost everything here already exists in the existing app, but the user interface is very much redesigned.

These are new functionality that I noticed when comparing with the existing app. I make every effort to be thorough but you should do your own comparison to be sure, and I have not detailed out things which have moved from, say, 1 step to 3 steps. For example, login and sign-up now have separate flows instead of being on the same screen.

All aspects of Criminal Background Check feature
Email address verification (current app uses email for sign-up but doesn't verify it)
Phone number collection
Phone number verification (current app does not collect phone number)
Tutorial
Settings screen (report a bug, request a feature, terms and conditions, privacy policy, rate the app)
LinkedIn verification of Profession and Employer. LinkedIn verification currently can only verify username. We are awaiting approval for additional permissions for LinkedIn that will make this possible. If we don't get that approval, LinkedIn verification will only be full name.
Hometown information

Other than these items which are new, everything else is reorganizing functionality that's already there -- splitting things into separate screens, changing layouts, etc..

Firebase is used for all data storage. Data already exists in firebase for all fields except the new ones being added.

Regarding the criminal background check, we have identified CrimCheck.net as a service provider and are working on getting the API. What we've learned is that they have an API we can use. For the API, we request a new criminal background check. Crimcheck returns us a URL. We give this URL to the user or open a web view to it. They then complete the criminal background check with Crimcheck. When it's done, Crimcheck posts a result back to a URL endpoint. This could be asynchronous, so we need a web endpoint that will post this to Firebase.

When considering the project, don't forget that you have the React Native project, the web view, and the Crimcheck to deal with.

Also, completion of the app also includes making the app on both iOS and Android apps stores.

Completion also includes walking us through and documenting the build process, so we can do it without help later.

If you're chosen for the project, we'll need:

regular communication via Upwork messages (every other day at longest)
Push code updates to git repository regularly (twice per week minimum)
Create an iOS test build weekly so all project owners can easily test
Voice calls regularly, as requested
All source code obviously

Please review everything. Take your time to understand it. In the design doc there are lots of arrows and comments which help explain the flow. If you have questions, don't hesitate to ask them. Then, come back to me with the following:

1- How much will it cost to make all of the updates, as a flat fee? We can break it into milestones if/once you are accepted, but initially we are just looking for total cost.

2- When can you start?

3- From the day you start, how long will it take to finish completely, including all steps listed above?

If you haven't already checked out the original app, you can see it via TestFlight on iOS here:

https://testflight.apple.com/join/GK0xvJra