from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView

from pymongo import MongoClient
from collections import OrderedDict

#This is the .kv file, but if you make a seperate .kv file it breaks when you
#integrate it in admin.py
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

#class datatableApp(App):
#    def build(self):
#        return datatableWindow()

#if __name__ =='__main__':
#    datatableApp().run()