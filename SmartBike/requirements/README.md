
# Smart Bike Deliverables

## Actors and Entities in the System
* Users
    These are the consumers of the SmartBike system. These are the people who book and use the SmartBikes for transportation. Also refered to as App Users, Consumers.
* Bikes
    These are the actual e-cycles used. They are categorized as
     - Available
     - In-ride
     - Unavailable
* Admins
    These are the superusers of the system, and have operational responsibilites.
* Trip
    This is the Entity which represents indivisual trip of a user on a bike.
    This has information like start_time, distance travelled, etc.s

## First Start
- Walk-thorugh/Tutorial
    This would help user get fimiliar into the SmartBike ecosystem.
- All required Permision (location, internet, etc)

## On Boarding
- Login via OTP
- KYC Details
    - Aadhar (can use indiastack api)
    

## Booking/Starting a ride
- Nearest available station (with Navigaiton)
    These statations are entered/maintained in the system by Admins using the SmartBike Admin Panel
- On reaching station 
    - Display available bikes (via indicators on bikes)*
        This is subject to the infrastucture on the bike. We would fall back to displaying the unique Bike number.
    - check balance in wallet
    - scan the QR code of available bike
    - Bike get assosicated with user profile and gets unlocked 
    - Ride starts and transition to Riding Mode

## Riding Mode
- Display trip status
    - Estimated remaining time
    - remaining battery percentage
    - Est. remaing distance
    - Current Speed
    - Est. remaining balance in wallet
- Park (Pause) toggle

## Pause ride
- Timer to indicate remaining standby time
- Lock the bike untill it's activated again 
- Add elements in billing as per standby time
- Switch back to ride state by again scaning QR code

## Stop ride
- Once the bike is docked and is in GeoFence enable stop button (requires lock and dock specs)
- Generate the bill
- Ask for feedback

## Additional information
- Links to walkthrough, tutorials, about us, etc.
- Contact Support option 
    This would send direct notification to the superusers
