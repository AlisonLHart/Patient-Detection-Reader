from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner

from collections import OrderedDict

from pymongo import MongoClient

from kivy.lang import Builder

Builder.load_file('operation.kv')

class operatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        client = MongoClient()
        self.db = client.database
        self.patients = self.db.patients


        # this is the datatable info 
        patientScrn = self.ids.scrnPatientContents
        patients = self.get_patients()
        patientsTable = datatableWindow(table=patients)
        patientScrn.add_widget(patientsTable)

    def reset(self, button):
        #That feel when you get to the point where you need a database
        print("I'm a sexy seahorse")

    #Sooooooo, this is not the proper way to do this
    def update_patient(self):
        PID = self.ids.PID_inp.text
        patients_container = self.ids.patients

        target_code = self.patients.find_one({'pid':PID})
        if target_code == None:
            pass
        else:
            details = BoxLayout(size_hint_y=None,height=30,pos_hint={'top':1})
            patients_container.add_widget(details)

            checkIn = Label(text=target_code['checkin'], size_hint_x=.1)
            PID = Label(text=PID, size_hint_x=.2)
            RN = Label(text=target_code['rn'], size_hint_x=.1)
            EMG = Label(text=target_code['emg'], size_hint_x=.2)
            risk= Label(text=target_code['risk'], size_hint_x=.2)
            reset= Button(text='reset', size_hint_x=.2,)
            reset.bind(on_press=self.reset)

            details.add_widget(checkIn)
            details.add_widget(PID)
            details.add_widget(RN)
            details.add_widget(EMG)
            details.add_widget(risk)
            details.add_widget(reset)

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

    def update_patient_fields(self):
        target = self.ids.opsFieldsP
        target.clear_widgets()

        crud_checkin = TextInput(hint_text = 'Check in date')
        crud_pid = TextInput(hint_text = 'patient ID')
        crud_rn = TextInput(hint_text = 'Room Number')
        crud_emg = TextInput(hint_text = 'Emergancy Number')
        crud_risk = Spinner(text='Risk', values = ['Low', 'High'])
        crud_rfid = TextInput(hint_text = 'Rfid Tag Number')

        crud_submit = Button(text='Update',size_hint_x=None,width=100,on_release=lambda x: self.update_patient(crud_checkin.text,crud_pid.text,crud_rn.text,crud_emg.text,crud_risk.text,crud_rfid.text))

        target.add_widget(crud_checkin)
        target.add_widget(crud_pid)
        target.add_widget(crud_rn)
        target.add_widget(crud_emg)
        target.add_widget(crud_risk)
        target.add_widget(crud_rfid)
        target.add_widget(crud_submit)

    def update_patient(self, checkin, pid, rn, emg, risk, rfid):
        content = self.ids.scrnPatientContents
        content.clear_widgets()

        self.patients.update_one({'pid':pid}, {'$set':{'checkin': checkin, 'pid':pid, 
        'rn':rn, 'emg':emg, 'risk':risk, 'rfid':rfid}})

        pats = self.get_patients()
        patientsTable = datatableWindow(table=pats)
        content.add_widget(patientsTable)
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

Builder.load_string(''' 
<datatableWindow>:
    id: main_win
    RecycleView:
        viewclass: 'CustLabel'
        id: table_floor
        RecycleGridLayout:
            id: table_floor_layout
            cols: 6
            default_size: (None, 250)
            default_size_hint: (1,None)
            size_hint_y: None
            height: self.minimum_height
            spacing: 5
<CustLabel@Label>:
    bcolor: (1,1,1,1)
    canvas.before:
        Color:
            rgba: root.bcolor
        Rectangle:
            size: self.size
            pos: self.pos 
''')

class datatableWindow(BoxLayout):
    def __init__(self, table='', **kwargs):
        super().__init__(**kwargs)

        #patients = self.get_patients()
        patients = table

        colTitle = [k for k in patients.keys()]
        rowsLen = len(patients[colTitle[0]])
        self.columns = len(colTitle)
        #print(colTitle)
        #print(rowsLen)
        table_data = []
        for t in colTitle:
            table_data.append({'text':str(t), 'size_hint_y':None, 'height':50,'bcolor':(.3,.3,.3,1)})

        for r in range(rowsLen):
            for t in colTitle:
                table_data.append({'text':str(patients[t][r]), 'size_hint_y':None, 'height':30,'bcolor':(.4,.4,.4,1)})

        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data

class operatorApp(App):
    def build(self):
        return operatorWindow()

if __name__=="__main__":
    oa = operatorApp()
    oa.run()