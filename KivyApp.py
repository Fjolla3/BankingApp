from kivy.app import App
from kivy.uix.label import Label 

class BasicApp(App):
    def build(self):
        label = Label(text="BankingApp!")
        return label

app = BasicApp()
app.run()