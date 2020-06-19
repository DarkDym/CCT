from kivy.app import App
from kivy.uix.label import Label

class ScreenM(App):
    def build(self):
        return Label(text="Hello World!")

ScreenM().run()
