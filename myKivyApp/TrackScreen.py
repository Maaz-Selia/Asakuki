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

        self.window = GridLayout()

        self.maxDuration = 16
        self.maxDrops = 24

        # User input of ml
        self.quantity = TextInput(multiline=False, input_filter='int', hint_text="Enter a number (0-500)", on_text=self._calculate)
        self.window.add_widget(self.quantity)

        self.button = Button(text="Calculate")
        self.button.bind(on_press=self._calculate)
        self.window.add_widget(self.button)

        self.answer = Label(text="")
        self.window.add_widget(self.answer)

        # keep track of values






        button = Button(text="Go to Home Screen")
        button.bind(on_press=self.go_to_home_screen)
        self.window.add_widget(button)

        self.add_widget(self.window)

    def go_to_home_screen(self, instance):
        self.manager.current = 'home_screen'

    def _calculate(self, instance):
        num = int(self.quantity.text) if self.quantity.text else 0
        if num < 0:
            self.quantity.text = "0"
            num = 0
        elif num > 500:
            self.quantity.text = "500"
            num = 500
        
        remDuration = num / 500 * self.maxDuration
        self.answer.text = str(remDuration)