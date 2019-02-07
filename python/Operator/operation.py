from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.lang import Builder

Builder.load_file('operation.kv')

class operatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def reset(self, button):
        #That feel when you get to the point where you need a database
        print("I'm a sexy seahorse")

    def update_patient(self):
        PID = self.ids.PID_inp.text
        patients_container = self.ids.patients
        if PID == (self.ids.PID_inp.text):
            details = BoxLayout(size_hint_y=None,height=30,pos_hint={'top':1})
            patients_container.add_widget(details)

            checkIn = Label(text=self.ids.Check_inp.text, size_hint_x=.1)
            PID = Label(text=PID, size_hint_x=.2)
            RN = Label(text=self.ids.RN_inp.text, size_hint_x=.1)
            EMG = Label(text=self.ids.EMG_inp.text, size_hint_x=.2)
            risk= Label(text=self.ids.rfid_inp.text, size_hint_x=.2)
            reset= Button(text='reset', size_hint_x=.2,)
            reset.bind(on_press=self.reset)

            details.add_widget(checkIn)
            details.add_widget(PID)
            details.add_widget(RN)
            details.add_widget(EMG)
            details.add_widget(risk)
            details.add_widget(reset)


class operatorApp(App):
    def build(self):
        return operatorWindow()

if __name__=="__main__":
    oa = operatorApp()
    oa.run()