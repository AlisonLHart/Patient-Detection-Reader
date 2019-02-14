from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('signin.kv')

class signInWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        #this is currently hard coded and doesn't actually do anything
        if uname == '' or passw == '':
            info.text = '[color=#FF0000] please enter username and password [/color]'
        else:
            if uname == 'admin' and passw == 'admin':
                info.text = '[color=#00FF00] Logged In [/color]'
            else:
                info.text = '[color=#FF0000] invalid username or password [/color]'

class signApp(App):
    def build(self):
        return signInWindow()

if __name__=="__main__":
    sa = signApp()
    sa.run()