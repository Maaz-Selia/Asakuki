import logging
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.app import App

class RecordScreen(Screen):
    def __init__(self, **kwargs):
        super(RecordScreen, self).__init__(**kwargs)

        self.diffuser = App.get_running_app().get_diffuser()
        self.db = App.get_running_app().get_db()

        self.window = GridLayout()

        # keep track of values

        self.ml_input = TextInput(hint_text="Enter ml", input_filter="int", multiline=False)
        self.add_widget(self.ml_input)
        
        self.drops_input = TextInput(hint_text="Enter drops", input_filter="int", multiline=False)
        self.add_widget(self.drops_input)

        self.button = Button(text="Add Record", on_press=self.add_record)
        self.add_widget(self.button)

        button = Button(text="Go to Home Screen")
        button.bind(on_press=self.go_to_home_screen)
        self.window.add_widget(button)

        self.add_widget(self.window)

    def go_to_home_screen(self, instance):
        self.manager.current = 'home_screen'

    def add_record(self, instance):
        """Add a new record from user input."""
        ml = self.ml_input.text
        drops = self.drops_input.text
        if ml.isdigit() and drops.isdigit():
            self.db.add_record(int(ml), int(drops))
            self.rv.update_records(self.db.load_records())
            self.ml_input.text = ""
            self.drops_input.text = ""