#!/usr/bin/env python

from firebase import firebase
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class Fireconnect():

    def __init__(self):
        self.fb =  firebase.FirebaseApplication('https://patient-detection-reader.firebaseio.com')
        self.reader = SimpleMFRC522()
        self.patientID = "123"
        self.jsondata = self.fb.get('/patientTest', None)


    def scanner(self):
        try:
            print("DEBUG: WAITING FOR SCAN\n")
            tag, text = self.reader.read()
            tagID = str(tag)
             
            print("DEBUG: TAG ID: " + tagID+"\n")

            
            for obj in self.jsondata:
                if(self.jsondata[obj]["RFID"]==tagID):
                    print("FOUND IT\n")
                    result = self.fb.put('patientTest/'+obj,'Risk', "HIGH")
                else:
                    print("NOT FOUND\n")
        
        finally:
            GPIO.cleanup()


while True:

    fire = Fireconnect()
    fire.scanner()
