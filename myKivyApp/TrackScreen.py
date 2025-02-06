import logging
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen


class TrackScreen(Screen):
    def __init__(self, **kwargs):
        super(TrackScreen, self).__init__(**kwargs)

        self.diffuser = App.get_running_app().get_diffuser()
        self.db = App.get_running_app().get_db()

        self.window = GridLayout()

        self.maxDuration = 16 * 60
        self.maxDrops = 30

        # 500ml 16
        # 300ml 12
        # 100ml 6

        # User input of ml
        self.quantity = TextInput(multiline=False, input_filter='int', hint_text="Enter a number (0-500)")
        self.window.add_widget(self.quantity)

        self.button = Button(text="Calculate")
        self.button.bind(on_press=self._calculate)
        self.window.add_widget(self.button)

        self.answer = Label(text="")
        self.window.add_widget(self.answer)

        # keep track of values

        self.ml = TextInput(multiline=False, input_filter='int', hint_text="Enter ml")
        self.ml.rowspan = 1
        self.window.add_widget(self.ml)
        self.drops = TextInput(multiline=False, input_filter='int', hint_text="Enter drops")
        self.window.add_widget(self.drops)

        button = Button(text="Add record")
        button.bind(on_press=self.add_record)
        self.window.add_widget(button)




        button = Button(text="Go to Home Screen")
        button.bind(on_press=self.go_to_home_screen)
        self.window.add_widget(button)

        self.add_widget(self.window)

    def go_to_home_screen(self, instance):
        self.manager.current = 'home_screen'

    def _calculate(self, instance):

        if self.quantity.text != "":
            intermittenceValue = App.get_running_app().get_intermittance()
            duration = self.maxDuration if intermittenceValue is 0 else self.maxDuration * 2

            remDuration = int(self.quantity.text) / 500 * duration
            reqDrops = (0.03 * (int(self.quantity.text))) + 3

            hours, mins = divmod(remDuration, 60)

            self.answer.text = f"{int(hours):02d}:{int(mins):02d}" + ' | ' + str(int(reqDrops))
        else:
            self.answer.text = "Enter a value"

    def add_record(self, instance):
        """Add a new record from user input."""
        ml = self.ml.text
        drops = self.drops.text
        if ml.isdigit() and drops.isdigit():
            self.db.add_record(int(ml), int(drops))
            self.ml.text = ""
            self.drops.text = ""