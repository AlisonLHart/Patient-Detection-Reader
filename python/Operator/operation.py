from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class operatorWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class operatorApp(App):
    def build(self):
        return operatorWindow()

if __name__=="__main__":
    oa = operatorApp()
    oa.run()