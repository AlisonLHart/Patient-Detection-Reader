from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from collections import OrderedDict
from pymongo import MongoClient

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        client = MongoClient()
        db = client.database
        users = db.users

        for user in users.find():
            print(user['first_name'])

class AdminApp(App):
    def build(self):

        return AdminWindow()

if __name__=='__main__':
    AdminApp().run()