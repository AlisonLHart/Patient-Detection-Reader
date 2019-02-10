from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from collections import OrderedDict
from pymongo import MongoClient

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        print(self.get_patients())

    def get_users(self): 
            client = MongoClient()
            db = client.database
            users = db.users
            _users = OrderedDict(
                first_names = {},
                last_names = {},
                user_names = {},
                passwords = {},
                designations = {}
            )
            first_names = []
            last_names = []
            user_names = []
            passwords = []
            designations = []

            for user in users.find():
                first_names.append(user['first_name'])
                last_names.append(user['last_name'])
                user_names.append(user['user_name'])
                passwords.append(user['password'])
                designations.append(user['designation'])
            #print(designations)
            users_length = len(first_names)
            idx = 0
            while idx < users_length:
                _users['first_names'][idx] = first_names[idx]
                _users['last_names'][idx] = last_names[idx]
                _users['user_names'][idx] = user_names[idx]
                _users['passwords'][idx] = passwords[idx]
                _users['designations'][idx] = designations[idx]

                idx += 1

            return (_users)

    def get_patients(self): 
            client = MongoClient()
            db = client.database
            patients = db.patients
            _patients = OrderedDict(
                checkin = {},
                pid = {},
                rn = {},
                emg = {},
                risk = {},
                rfid = {}
            )
            checkin = []
            pid = []
            rn = []
            emg = []
            risk = []
            rfid = []

            for patient in patients.find():
                checkin.append(patient['checkin'])
                pid.append(patient['pid'])
                rn.append(patient['rn'])
                emg.append(patient['emg'])
                risk.append(patient['risk'])
                rfid.append(patient['rfid'])
                
            #print(designations)
            patients_length = len(pid)
            idx = 0
            while idx < patients_length:
                _patients['checkin'][idx] = checkin[idx]
                _patients['pid'][idx] = pid[idx]
                _patients['rn'][idx] = rn[idx]
                _patients['emg'][idx] = emg[idx]
                _patients['risk'][idx] = risk[idx]
                _patients['rfid'][idx] = rfid[idx]

                idx += 1

            return (_patients)

class AdminApp(App):
    def build(self):

        return AdminWindow()

if __name__=='__main__':
    AdminApp().run()