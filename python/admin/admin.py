from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

from collections import OrderedDict
from pymongo import MongoClient
from utills.datatable import datatableWindow
from datetime import datetime
import hashlib

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        client = MongoClient()
        db = client.database #I named the database 'database' like a dum dum.
        self.users = db.users # The collections of the database are users and patients
        self.patients = db.patients

        #print(self.get_users())

        #users
        content = self.ids.scrnContents
        users = self.get_users()
        usersTable = datatableWindow(table=users)
        content.add_widget(usersTable)

        #patients
        patientScrn = self.ids.scrnPatientContents
        patients = self.get_patients()
        patientsTable = datatableWindow(table=patients)
        patientScrn.add_widget(patientsTable)


    def add_user_fields(self):
        target = self.ids.opsFields
        target.clear_widgets()

        crud_first = TextInput(hint_text = 'First Name')
        crud_last = TextInput(hint_text = 'Last Name')
        crud_user = TextInput(hint_text = 'User Name')
        crud_pwd = TextInput(hint_text = 'Password')
        crud_des = Spinner(text='Operator', values = ['Operator', 'Administator'])

        crud_submit = Button(text='Add',size_hint_x=None,width=100,on_release=lambda x: self.add_user(crud_first.text,crud_last.text,crud_user.text,crud_pwd.text,crud_des.text))

        target.add_widget(crud_first)
        target.add_widget(crud_last)
        target.add_widget(crud_user)
        target.add_widget(crud_pwd)
        target.add_widget(crud_des)
        target.add_widget(crud_submit)

    def add_patient_fields(self):
        target = self.ids.opsFieldsP
        target.clear_widgets()

        crud_checkin = TextInput(hint_text = 'Check in date')
        crud_pid = TextInput(hint_text = 'patient ID')
        crud_rn = TextInput(hint_text = 'Room Number')
        crud_emg = TextInput(hint_text = 'Emergancy Number')
        crud_risk = Spinner(text='Risk', values = ['Low', 'High'])
        crud_rfid = TextInput(hint_text = 'Rfid Tag Number')

        crud_submit = Button(text='Add',size_hint_x=None,width=100,on_release=lambda x: self.add_patient(crud_checkin.text,crud_pid.text,crud_rn.text,crud_emg.text,crud_risk.text,crud_rfid.text))

        target.add_widget(crud_checkin)
        target.add_widget(crud_pid)
        target.add_widget(crud_rn)
        target.add_widget(crud_emg)
        target.add_widget(crud_risk)
        target.add_widget(crud_rfid)
        target.add_widget(crud_submit)

    def update_user_fields(self):
        target = self.ids.opsFields
        target.clear_widgets()

        crud_first = TextInput(hint_text = 'First Name')
        crud_last = TextInput(hint_text = 'Last Name')
        crud_user = TextInput(hint_text = 'User Name')
        crud_pwd = TextInput(hint_text = 'Password')
        crud_des = Spinner(text='Operator', values = ['Operator', 'Administator'])

        crud_submit = Button(text='Update',size_hint_x=None,width=100,on_release=lambda x: self.update_user(crud_first.text,crud_last.text,crud_user.text,crud_pwd.text,crud_des.text))

        target.add_widget(crud_first)
        target.add_widget(crud_last)
        target.add_widget(crud_user)
        target.add_widget(crud_pwd)
        target.add_widget(crud_des)
        target.add_widget(crud_submit)

    def remove_user_fields(self):
        target = self.ids.opsFields
        target.clear_widgets()

        crud_user = TextInput(hint_text='User Name')
        crud_submit = Button(text='Remove',size_hint_x=None,width=100,on_release=lambda x: self.remove_user(crud_user.text))

        target.add_widget(crud_user)
        target.add_widget(crud_submit)

    def remove_user(self, user):
        content = self.ids.scrnContents
        content.clear_widgets()

        self.users.remove({'user_name':user})

        users = self.get_users()
        usersTable = datatableWindow(table=users)
        content.add_widget(usersTable)

    def add_user(self, first, last, user, pwd, des):
        content = self.ids.scrnContents
        content.clear_widgets()

        pwd = hashlib.sha256(pwd.encode()).hexdigest()
        
        self.users.insert_one({'first_name': first, 'last_name':last, 
        'user_name':user, 'password':pwd, 'designation':des, 'date':datetime.now()})

        users = self.get_users()
        usersTable = datatableWindow(table=users)
        content.add_widget(usersTable)
        #print('is this working?')

    def add_patient(self, checkin, pid, rn, emg, risk, rfid):
        content = self.ids.scrnPatientContents
        content.clear_widgets()

        self.patients.insert_one({'checkin': checkin, 'pid':pid, 
        'rn':rn, 'emg':emg, 'risk':risk, 'rfid':rfid})

        pats = self.get_patients()
        patientsTable = datatableWindow(table=pats)
        content.add_widget(patientsTable)
        #print('is this working?')

    def update_user(self, first, last, user, pwd, des):
        content = self.ids.scrnContents
        content.clear_widgets()

        pwd = hashlib.sha256(pwd.encode()).hexdigest()

        self.users.update_one({'user_name':user},{'$set':{'first_name': first, 'last_name':last, 
        'user_name':user, 'password':pwd, 'designation':des, 'date':datetime.now()}})

        users = self.get_users()
        usersTable = datatableWindow(table=users)
        content.add_widget(usersTable)

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