import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):

    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
<<<<<<< HEAD
    MyApp().run()
=======
    MyApp().run()
>>>>>>> 436c1227388c574a9bb8b2f1a40df8a73035c366
