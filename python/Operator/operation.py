from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file('operation.kv')

class operatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def update_patient(self):
        PID = self.ids.PID_inp.text
        patients_container = self.ids.patients
        if PID == '1234':
            details = BoxLayout(size_hint_y=None,height=30,pos_hint={'top':1})
            patients_container.add_widget(details)

            checkIn = Label(text='00/00/0000', size_hint_x=.1)
            PID = Label(text=PID, size_hint_x=.2)
            RN = Label(text='1234', size_hint_x=.1)
            EMG = Label(text='1-111-111-1111', size_hint_x=.2)
            risk= Label(text='risk_level', size_hint_x=.2)
            reset= Button(text='reset', size_hint_x=.2)

            details.add_widget(checkIn)
            details.add_widget(PID)
            details.add_widget(RN)
            details.add_widget(EMG)
            details.add_widget(risk)
            details.add_widget(reset)

            #Update Preview
            preview = self.ids.reset_preview
class operatorApp(App):
    def build(self):
        return operatorWindow()

if __name__=="__main__":
    oa = operatorApp()
    oa.run()