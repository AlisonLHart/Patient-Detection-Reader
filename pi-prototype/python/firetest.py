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


    def scanner(self):
        try:
            patient = self.getPatient()


            print("Please scan the appropriate tag")
            tag, text = self.reader.read()
            tagID = str(tag)
             
            print("PATIENT ID: " + str(self.patientID) + "\nTAG ID: " + tagID)

            result = self.fb.put('/patientTest/'+ patient,'RFID', tagID)
        finally:
            GPIO.cleanup()

    
    def getPatient(self):
        self.patientID = input("Enter the Patient ID: ")
        print(self.jsondata)
        for obj in self.jsondata:
            if(self.jsondata[obj]["PID"]==str(self.patientID)):
                print("FOUND IT\n")
                return obj
            else:
                print("NOT FOUND\n")



fire = Fireconnector()
fire.scanner()
