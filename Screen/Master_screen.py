from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class ScreenM(App):
    def build(self):
        box = BoxLayout()

        lbl = Label(text="Hello World!")
        bt1 = Button(text="TESTE")

        box.add_widget(lbl)
        box.add_widget(bt1)

        return box

ScreenM().run()
