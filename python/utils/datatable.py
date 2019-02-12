from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView

from pymongo import MongoClient
from collections import OrderedDict

#in case the .kv file stops loading, use these
    #Builder.load_string('''  ''') datatable.kv is what goes in the parenthases, nerd
    #Builder.load_file('datatable.kv') #This does ^ differently ... in theory

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
            table_data.append({'text':str(t), 'size_hint_y':None, 'height':50,'bcolor':(.06,.45,.45,1)})

        for r in range(rowsLen):
            for t in colTitle:
                table_data.append({'text':str(patients[t][r]), 'size_hint_y':None, 'height':30,'bcolor':(.06,.25,.25,1)})

        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data

#class datatableApp(App):
#    def build(self):
#        return datatableWindow()

#if __name__ =='__main__':
#    datatableApp().run()