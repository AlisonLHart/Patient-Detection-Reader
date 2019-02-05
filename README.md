# Patient-Detection-Reader

A alert solution for hospital environments. This project aims to decrease staff response time through a patient wearable device, notifying staff of "at-risk of falling" patients before they hurt themselves. Using an RFID tag, the wearable will send an alarm and application-based alert if the patient crosses a threshold, created by an RFID reader field. 

## System Dependancies 

This system operates using:  
	- Python 3.6.7  
	- Kivy 1.10.1  
	- Rasbian  
	- A version of SQL. This is TBA
 
## Hardware

System hardware consists of:
- a Raspberry Pi 3b (his name is Dave =D )
- RC522 Antenna RFID Reader
- Associated RFID cards. 
    The RFID is wired to the Pi through use of a breadboard. The wiring documentation can be found under: https://pimylifeup.com/raspberry-pi-rfid-rc522/
- A button for manual reset

## Source Files

### signin.py/kv

This is a sign in page for nurses, it will reference a database of users

###User database Schema:
- usr_Name: user name
- passw: password (this will be hashed and salted)
- priv_level: priviledge level (this will determine what a user can do)


usr_Name|passw|priv_level

jdoe    |***  | 1

dbainter|***  | 2

### Operation.py.kv

This is the main view for the program, for prototyping it will only allow you to interact with a single patient, in the future we would like it to integrate with a patient database

###Patient database Schema:
- pat_Name: patient name
- codition: condition of patient
- room: room patient is in
- risk: how likely they are to get up based on sensors (1-4, 4 sets off alarm)

pat_Name|condition|room |risk

jdoe    |brokenarm|1234 |1 

dbainter|apendix  | 234 |2


