from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
import time
import tinytuya
import logging


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        self.diffuser = App.get_running_app().get_d()

        self.window = GridLayout()
        self.window.cols = 1

        # Power Button
        self.button = Button(text="Power")
        self.button.bind(on_press=self._toggle_power)
        self.window.add_widget(self.button)


        button = Button(text="Go to Spray Screen")
        button.bind(on_press=self.go_to_spray_screen)
        self.window.add_widget(button)

        button = Button(text="Go to Light Screen")
        button.bind(on_press=self.go_to_light_screen)
        self.window.add_widget(button)

        self.add_widget(self.window)

    def go_to_spray_screen(self, instance):
        self.manager.current = 'spray_screen'

    def go_to_light_screen(self, instance):
        self.manager.current = 'light_screen'

    def _toggle_power(self, instance):
        return self.diffuser.toggle_power()