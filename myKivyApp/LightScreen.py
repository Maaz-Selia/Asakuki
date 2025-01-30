from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.slider import Slider
from kivy.uix.colorpicker import ColorPicker

class LightScreen(Screen):
    def __init__(self, **kwargs):
        super(LightScreen, self).__init__(**kwargs)

        self.diffuser = App.get_running_app().get_d()

        self.window = GridLayout()
        self.window.cols = 1

        # Colour Picker
        currentColour = self.diffuser.colour[0:6]
        self.colourpicker = ColorPicker(hex_color=currentColour)
        self.colourpicker.hex_color = currentColour
        self.colourpicker.bind(color=self._set_colour)
        self.window.add_widget(self.colourpicker)

        #Brightness Slider
        currentBrightness = self.diffuser.brightness
        self.slider = Slider(min=-0, max=255, step=5, value=currentBrightness, value_track=True)
        self.slider.bind(value=self._set_brightness)
        self.window.add_widget(self.slider)


        button = Button(text="Go to Home Screen")
        button.bind(on_press=self.go_to_home_screen)
        self.window.add_widget(button)

        self.add_widget(self.window)

    def go_to_home_screen(self, instance):
        self.manager.current = 'home_screen'  # Switch to home screen

    def _set_colour_mode(self, instance):
        return self.diffuser.set_colour_mode(str(instance.text))
    
    def _set_colour(self, instance, value):
        return self.diffuser.set_colour(str(instance.hex_color), self.slider.value)

    def _set_brightness(self, instance, touch):
        return self.diffuser.set_brightness(int(instance.value))