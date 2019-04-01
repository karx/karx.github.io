
#Smart Bike Deliverables

By default: logging each step

Setting up real time telemetery of all the devices 

##First Start
- Language Selection 
- Walk-thorugh (How it works)

##On Boarding
- All required Permision (location, internet, etc)
- Login via OTP
- KYC Details
    - Indian > Aadhar (can use indiastack api)
    - Foreign > Passport (requires verification)

##Booking a ride
- Nearest available station (with Navigaiton)
- On reaching station 
    - Display available bikes (via indicators on bikes) (to display available bike either no. or status)
    - check balance in wallet
    - scan the QR code of available bike
    - Bike get assosicated with user profile and gets unlocked (requires lock and dock specs)
    - happy riding

##During ride
- Display user parameters
    - Estimated remaining time
    - remaining battery percentage
    - Est. remaing distance
    - Current Speed
    - Est. remaining balance in wallet
- Park (Pause) toggle

##Pause ride
- Timer to indicate remaining standby time
- Lock the bike untill it's activated again (requires lock specs)
- Add elements in billing as per standby time
- Switch back to ride state by again scaning QR code

##Stop ride
- Once the bike is docked and is in GeoFence enable stop button (requires lock and dock specs)
- Generate the bill
- Ask for feedback