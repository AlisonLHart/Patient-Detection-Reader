# Patient-Detection-Reader

A alert solution for hospital environments. This project aims to decrease staff response time through a patient wearable device, notifying staff of "at-risk of falling" patients before they hurt themselves. Using an RFID tag, the wearable will send an alarm and application-based alert if the patient crosses a threshold, created by an RFID reader field. 

## System Dependancies 

This system operates using:  
	- Python 3.6.7  
	- Kivy 1.10.1  
	- Rasbian  
	- MongoDB 4.0.6
 
## Hardware

System hardware consists of:
- a Raspberry Pi 3b (his name is Dave =D )
- RC522 Antenna RFID Reader
- Associated RFID cards. 
    The RFID is wired to the Pi through use of a breadboard. The wiring documentation can be found under: https://pimylifeup.com/raspberry-pi-rfid-rc522/
- A button for manual reset

## Source Files

### signin.py/kv

Sign in page for nurses, it will reference a database of users

### Operation.py/kv

Main view for the program for nurses. From this screen you can view patients and their information and will allow you to reset their status from High to Low

### admin.py/kv

Main view for the program for administratos. From this screen you can view and edit users and modify or add patient data.

### datatable.py

The datatable is the view and controller for the database. It's integrated into the admin.py file.

## Database
#### User collection:
- first_names / last names: names of users
- usr_Name: user name
- passwords: password (this will be hashed and salted)
- designations: priviledge level (this will determine what a user can do)

	_users['first_names'] = {}
	_users['last_names'] = {}
	_users['user_names'] = {}
	_users['passwords'] = {}
	_users['designations'] = {}

#### Patient collection:
- checkin: date checked in
- pid: patient id
- emg: emergancy contact
- rn: room patient is in
- risk: how likely they are to get up based on sensors (1-4, 4 sets off alarm)
- rfid: rfid tag number

	checkin = {},
	pid = {},
	rn = {},
	emg = {},
	risk = {},
	rfid = {}


