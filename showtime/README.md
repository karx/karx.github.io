## ShowTimeSynd - SOW
Document prepared by 

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
This documentation is to serve as a 'Statement of Work' or SOW for the ShowTimeSynd to create and enable a digital marketplace. 

Such a system would include a means for
 - sellers onboarding 
 - sellers to list their offerings
 - verification of sellers and offerings
 - buyers onboarding
 - buyers to browse through the offerings
 - bid submissions and approval
 - agreement and fulfilment 

Akriya Technologies will work on ShowTimeSynd to:

* Designing the ShowTimeSynd Architecture
* Design and Develop ShowTimeSynd Sellers app
* Design and Develop ShowTimeSynd Buyer app
* Design and Develop ShowTimeSynd Admin app
* Deploy said systems for ShowTimeSynd
* Provide documentation of the new system
* Knowledge Transfer/Integrate 

Akriya Technologies proposes to design, develop and provide installation of v1.0 of the proposed system to cater for up to 1000 Distinct Seller with up to 10000 distinct buyers.
This activity will require x weeks. The estimated cost for this activity would be x (specs x).

The Value Proposition of using Akriya Technologies for this project are:
* Proven engineering techniques for making Integrated systems.
* Data Architecture and Solution experience
* Using our subject matter experts to complete the project quickly. Rapid project completion minimizes disruptions and allows organizations to realize cost-saving quickly.

## Project Definition
ShowTimeSynd aims to build/design to develop a marketplace for digital assets. This platform would allow us to onboard, then curate offers from multiple sellers, provide a frontend for buyers to browse through and bid to buy.

The proposed system would have the following modules:
### The Frontpage: _www.`domainofchoice`.com_
This web presence, SEO friendly to tell people about ShowTimeSynd.

### Seller Endpoint: _seller.`domainofchoice`.com_
This module comprises of the FE exposed to the sellers, this involves:
* Seller onboarding
We collect the following data when we onboard a seller

|   Data Type             |  Stage      |
|-------------------------|-------------|
|   Seller Phone number     | (Primary)   |
|   Seller Name             | (Stage 1)   |
|   Seller email-address    | (Stage 0)   |
|   Business Name           | (Stage 2)   |
|   Buisness GST           | (Stage 3)   |
|   mobile number Verify  | (Stage 3)   |
|   email address Verify  | (Stage 3)   |
|   His profile (*)       | (Stage 4)   |

```
Stage 0: first interaction with the Seller
Stage 1: User visits one of our site/modules
Stage 2: User visits one of our onboarding modules
Stage 3: User visits to verify himself
Stage 4: User visits to build identity (Optional)
```
* Add/Edit Product
We provide an option for sellers to add/update an offering.
This would include the following data:

|   Data Type             |  Stage      |
|-------------------------|-------------|
|   - | (Primary)   |
|   - | (Stage 1)   |
|   - | (Stage 0)   |
|   - | (Stage 2)   |
|   - | (Stage 3)   |
|   - | (Stage 3)   |
|   - | (Stage 3)   |
|   - | (Stage 4)   |
    
* Incoming Bids
This will show him incoming bids from sellers, here he can revert with
`approve`,`reject` or `counter`.
 
* History
Log of all incoming bids and their final fulfilment status on the platform.

* Profile/Settings page
This page is used by the seller to provide/update information and documents needed to get approval for their profile.
Also to control what is visible to the buyers (IF).

### Buyer Endpoint: _buyer.`domainofchoice`.com_
This module comprises of the FE exposed to the buyers, this involves:
* Browse all
* Submit Bid
* Ongoing Deals
* History

### Admin Endpoint: admin.`domainofchoice`.com
To be consumed by superusers. 
* Help create reports, logs, etc.
* Approval list of sellers.
* Approval list of offerings
* Approval list of Bids
* Contact creation list

### Sample Viewer Endpoint: viewer.`domainofchoice`.com/<digital-asset-id>
This is a viewer-created for when a buyer wants to see a sample/demo of the digital asset.

### On-cloud Services
These are set of services deployed as a backend for the Onboarding and Ongound modules.
* Authentication
* User data management (Buyers and sellers)
* Data storage (digital assets, demos, etc) 
* Common Onboarding APIs - (new, update, delete, blacklist) 
* Common ShowTimeSynd APIs - (detect, fetch)

## Maintenance
To be maintained for 6 months and then rediscuss based on new requirements and learnings.

## Exclusions
The followings are excluded from the project scope
* The packages used and maintained by Akriya Technologies for interfacing with IoT Devices.

## Deliverables
The deliverables are listed below.
* Devices. 
To be installed in 1 ShowTimeSynd facility, and 50% spare**.

* Software
Access top-level Git repositories for the Dashboard, mobile Apps, and admin interface package.

* Documentation and graphical depictions of the new proposed ShowTimeSynd system.


## Customer Responsibilities
* The nature of this engagement dictates that Akriya Technologies receive a frequent and enthusiastic response from the appropriate personnel.
* A weekly review between the Akriya Technologies consultant and the ShowTimeSynd project lead or his designate will ensure that the expectations of this engagement are met.
* Client will assign a key contact who will be responsible for providing Akriya Technologies with information, access to personnel, and facility access.
* Client will provide a work area space with desk, chair, Internet access for use by Akriya Technologies to conduct project business while working on-site.

## Investment and Cost
* Man-hour required: y months: --xx-- INR

* Hardware cost (if required) to be paid by ShowTimeSynd
    
* Server/Web hosting charges:
    * 60$ / month = 4000 INR

*Bill separately for travel costs will be billed at actual cost and will not exceed 10,000 INR for the entire project.

 * Payment Schedule

| Milestone                                 | Percentage    | Amount    |
| -------------                             |:-------------:| -----:    |
| Requirement Finalization                  | 0%            | 1 INR|
| Telemetry Systems Demo           | 33%           | 1 INR|
| Dashboard + App shandoaver            | 66%           | 1 INR|
| Final Deliverys                         | 100%          | 1 INR|


```
From the old project
```

Devices cost to be paid on the day of installation.
Server cost to be paid directly or at the start of each month.
Travel reimbursements as and when declared.

## Acceptance Criteria
At the conclusion of this evaluation, all deliverables for this phase will be presented to ShowTimeSynd for review.

ShowTimeSynd or its representative will have five business days from the date of delivery of any document that is a deliverable to review it and request any changes.  If Akriya Technologies does not receive notification of any required changes within this period, the document will be deemed to have been accepted without modification and will be reissued as a final copy.

If Akriya Technologies is notified by ShowTimeSynd, within the above time frame, of any changes required, Akriya Technologies will within two business days of such notification implement those changes as have been agreed between the parties.  A final copy of the document will then be submitted to ShowTimeSynd.

## Assumptions
* General
    * All documentation created for this project will be available in hard copy and electronic format.
    * Any modifications to the scope of work will be handled through a change control process and will be agreed to by both parties.

* Commercial
    * Additional costs may be incurred where any delay not under the control of Akriya Technologies that causes Akriya Technologies personnel to not fulfil their scheduled tasks.
    * An authorized delegate of ShowTimeSynd will be available at the time of completion of the build phase so that all documentation can be accepted and signed.
    * Additional costs may be incurred where any work scheduled to be undertaken by Akriya Technologies is postponed by ShowTimeSynd after 24 hours of its commencement.
    * All changes to the schedule or technical requirements must be provided to Akriya Technologies in written format. Email is included as written format. Receipt of all correspondence should be confirmed by phone wherever possible.
    * ShowTimeSynd has accepted the costs/times estimate as detailed in this document
    * ShowTimeSynd has accepted the Akriya Technologies standard terms and conditions linked.

## Intellectual Property
Unless otherwise agreed in writing, ShowTimeSynd acknowledges that all intellectual property rights attaching to the products or arising out of the provision of services are and will remain the property of Akriya Technologies (or its suppliers, where such rights are owned by that supplier).

The software will be licensed to ShowTimeSynd on the terms of the relevant license agreement provided with the product or as otherwise agreed between Akriya Technologies and ShowTimeSynd in writing.


## Approved by
Name:   
Date:   
Position:   

