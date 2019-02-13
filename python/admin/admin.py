from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from collections import OrderedDict
from pymongo import MongoClient
from utills.datatable import datatableWindow

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #print(self.get_users())

        #users
        content = self.ids.scrnContent
        users = self.get_users()
        usersTable = datatableWindow(table=users)
        content.add_widget(usersTable)

        #patients
        patientScrn = self.ids.scrnPatientContent
        patients = self.get_patients()
        patientsTable = datatableWindow(table=patients)
        patientScrn.add_widget(patientsTable)

    def get_users(self): 
            client = MongoClient()
            db = client.database
            users = db.users
            _users = OrderedDict()
            _users['first_names'] = {}
            _users['last_names'] = {}
            _users['user_names'] = {}
            _users['passwords'] = {}
            _users['designations'] = {}
            first_names = []
            last_names = []
            user_names = []
            passwords = []
            designations = []

            for user in users.find():
                first_names.append(user['first_name'])
                last_names.append(user['last_name'])
                user_names.append(user['user_name'])
                pwd = user['password']
                if len(pwd) > 10:
                    pwd = pwd[:10] + '...'
                passwords.append(pwd)
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
                rfidShort = patient['rfid']
                if len(rfidShort) > 10:
                        rfidShort = rfidShort[:10] + '...'
                rfid.append(rfidShort)
                
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

    def change_screen(self, instance):
        if instance.text == 'Manage Patients':
            self.ids.scrnMngr.current = 'scrnPatientContent'
        
        elif instance.text == 'Manage Users':
            self.ids.scrnMngr.current = 'scrnContent'
        
        else:
            self.ids.scrnMngr.current = 'scrnAnalysisContent'

class AdminApp(App):
    def build(self):

        return AdminWindow()

if __name__=='__main__':
    AdminApp().run()