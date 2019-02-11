from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from pymongo import MongoClient
from collections import OrderedDict

Builder.load_string('''
<datatable>:
    id: main_win
    RecycleView:
        viewclass: 'Label'
        id: table_floor
        RecycleGridLayout:
            id: table_floor_layout
            cols: 6
            default_size: (None, 250)
            default_size_hint: (1,None)
            size_hint_y: None
            height: self.minimum_height
            spacing: 5
''')
class datatableWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        patients = self.get_patients()

        colTitle = [k for k in patients.keys()]
        rowsLen = len(patients[colTitle[0]])
        self.columns = len(colTitle)
        print(colTitle)
        print(rowsLen)
        table_data = []
        for t in colTitle:
            table_data.append({'text':str(t)})
        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data

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
class datatableApp(App):
    def build(self):

        return datatableWindow()

if __name__ =='__main__':
    datatableApp().run()