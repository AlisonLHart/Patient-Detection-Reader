from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('admin.kv')

class adminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class adminApp(App):
    def build(self):
        return adminWindow()

if __name__ =='__main__':
    adminApp().run