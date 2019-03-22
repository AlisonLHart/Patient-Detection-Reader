#!/usr/bin/env python

from firebase import firebase
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import json


class Fireconnector():


    def __init__(self):
        self.user = "default@gmail.com"
        self.fb =  firebase.FirebaseApplication('https://patient-detection-reader.firebaseio.com')
        self.reader = SimpleMFRC522()
        self.patientID = "123"
        self.jsondata = self.fb.get('/patientTest', None)
        
        for obj in self.jsondata:
            print(self.jsondata[obj])
            print()


    def scanner(self):
        try:
            print("Please scan the appropriate tag")
            tag, text = self.reader.read()
            tagID = str(tag)
            
            print("PATIENT ID:" + self.patientID + "\nTAG ID: " + tagID)

            result = self.fb.put('/patientTest/-LaRrBsmee59KjKbEO9A','RFID', tagID)
        finally:
            GPIO.cleanup()

    
    def getPatient(self):
        self.patientID = input("Enter the Patient ID: ")
        for i in range (0, len(self.jsondata)):
            print(self.jsondata[i][PID])
            if(self.jsondata[i][PID]==patientID):
                print(self.jsondata[i])
                break
        



fire = Fireconnector()
#fire.getPatient()
