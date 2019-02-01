# Patient-Detection-Reader

A alert solution for hospital environments. This project aims to decrease staff response time through a patient wearable device, notifying staff of "at-risk of falling" patients before they hurt themselves. Using an RFID tag, the wearable will send an alarm and application-based alert if the patient crosses a threshold, created by an RFID reader field. 

## System Dependancies 

The below sections detail the central parts of the system, including Python source files and hardware component descriptions.

## Hardware

System hardware consists of a Raspberry Pi 3b, an RC522 Antenna RFID Reader, and associated RFID cards. The RFID is wired to the Pi through use of a breadboard. The wiring documentation can be found under: https://pimylifeup.com/raspberry-pi-rfid-rc522/

## patient-manager.py

Python source for managing patients based on data read from a .csv. This .csv includes the patient ID, name, date admitted, and assigned RFID ID. 

Data is read continuously from the sheet, in a loop. Patient objects are created with each new entry, and any changes to data is updated accordingly in the correct patient object. The .csv includes the patient at-risk status, which for now is simply "NO ALERT" and "ALERT." Patients by default have a NO ALERT status, which changes to ALERT when the corresponding RFID tag is read. This class interacts with the app.py class, which is explained below. 

## app.py

Python source for taking patient data from the patient-manager.py class and updating it in an application NUI (Natural User Interface) for user interaction. 

