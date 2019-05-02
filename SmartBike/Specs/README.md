## SmartBike
## System Design Document

The System Design Document is a required document for every project. It should include a high-level description of why the System Design Document has been created, provide what the new system is intended for or is intended to replace and contain detailed descriptions of the architecture and system components.

## Introduction

This System Design Document has been created to outline the proposed system design for new SmartBike System (SBS). The SBS is intended to help run e-bike renting operations by Intactual and Instinct E-bikes. By designing, testing, and deploying the SBS, Akriya Technologies will improve its capabilities in maintenance management, tracking, and reporting. This document and the technical specifications listed herein comply with all Akriya Technologies technical standards and infrastructure.

## Purpose

The purpose of this System Design Document is to provide a description of how the new SBS will be constructed. The Systems Design Document was created to ensure that the SBS design meets the requirements specified in the SBS project requirements documentation. The System Design Document provides a description of the system architecture, software, hardware, database design, and security.

### System Overview

Based on the market research and brief, we have seen that to run a successful e-bike renting solution, we need to focus on customer delight, ease-of-use, tracking, and reporting. The proposed SBS system will utilize our toolkit in hardware and software to provide a solution which will help run and improve the efficiency of an e-bike renting operation.

The SBS system is also compatible with and/or utilizes 3rd party services for services like payments, user authentication, emailing and tracking. The SBS system includes 2 user interfaces which will allow end-user experience, tracking, report generation, and operational control. It will also allow for real-time reporting and operational infrastructure to exist.

The new SBS system will provide the following capabilities:

* Portal to view and maintain current e-bike system data.
* End-user experience - Mobile app
    * Andriod + iOS + Web
    * Payment Support
    * KYC verification
    * Integrations with maps for Navigation control
    * Bike booking
    * On-ride experience
* Real-time SmartBike Services
* Bike Simulator
To test and work the SBS.

### Design Constraints

This section should describe the constraints associated with the system design. Constraints are the result of various conditions beyond the scope of the project that affect and limit the system design. These may be due to hardware, software, business processes, organizational/industry standards, or other conditions which affect the system design. This section should provide a description of what the constraints are and how they affect or limit the system design.

The SBS Project Team identified several constraints which will impact and limit the design of the tool. These constraints are beyond the scope of the SBS Project but must be carefully factored into the system design. To date, the following constraints have been identified:

* Project deadline is 1 month from the start of the project. 30 days
* SBS must comply with all industry regulatory policies and guidelines. These policies and guidelines will impact the tool by requiring certain standards of coding, user interfaces, security, and management of the tool.

## Roles and Responsibilities

The following table defines the SBS System Design roles and responsibilities. This matrix also serves as the list of points of contact for issues and concerns relating to the SBS System Design.

* Kartik Arora     Project Manager     (91)-8437166272     kartik@akriya.co.in
* Sarthak Verma     Tech Lead    (91) 8979080101     sarthak@artiosys.com
* Rahul     Lead Designer – Architecture     (777) 555-1214     rahul@artiosys.com
* Ashtam     Lead Designer – IoT     (777) 555-1215     ashtam@artiosys.com

## Project References
> TBD



## System Architecture

This section should describe the architecture necessary to achieve the system design for the project. This will usually consist of both hardware and software architecture. Additionally, it may be that the existing architecture (either hardware or software) is already in place, in which case the requirements should still be documented. The description of the architecture should include a list and summary of each component and, depending on the complexity of the design, it may be beneficial to include diagrams showing the relationship/connectivity between these components.

#### Hardware:

The SBS design is based on existing hardware architecture already deployed by TBD. This hardware consists of the following components:

> TBD. Discussions with Pingzee no results. 

#### Software:

The SBS design is based on the individual design of all components based on the type of user interacting with it. The software architecture is designed to incorporate different scenarios and challenges into a web-based app which help runs an e-bike renting operation in real-time. The components which comprise the software architecture include:

* End-User App Module: This component provides the user interfaces to all end-users of the renting service. This component consists of several sub-components to include:
    – Onboarding mechanism
    - Training mechanism
    - Scanning/Renting Module
    - In-Ride mode
    - Payment module
    - Personal Tracking and reporting
    
* Real-time SmartBike Module: This component is responsible for maintaining the state of the system. This also exposes ways to consume and update the state.

* Automated Reporting Module: This component provides all of the pre-built automated reporting capabilities. These are reports that are generated regularly and repetitively at known intervals.

* Admin/Operation Module: This component provides a superuser interface to view, update and maintain the SBS system. 


## Database/Server Design

> This section should describe the design of the database or data hosting environment. 


## Hardware and Software Detailed Design
> This portion of the system design document should describe the design of the hardware and software in more detailed terms. 

### Hardware:

TBD

### Software:

TBD