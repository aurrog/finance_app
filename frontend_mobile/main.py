from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# import requests

class FinanceApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.type_input = TextInput(hint_text='Type (income/expense/wish)')
        self.amount_input = TextInput(hint_text='Amount')
        self.desc_input = TextInput(hint_text='Description')
        self.submit_button = Button(text='Submit', on_press=self.submit)
        self.layout.add_widget(self.type_input)
        self.layout.add_widget(self.amount_input)
        self.layout.add_widget(self.desc_input)
        self.layout.add_widget(self.submit_button)
        return self.layout

    def submit(self, instance):
        data = {
            'type': self.type_input.text,
            'amount': float(self.amount_input.text),
            'description': self.desc_input.text
        }
        # requests.post('http://127.0.0.1:5000/transactions', json=data)

if __name__ == '__main__':
    FinanceApp().run()