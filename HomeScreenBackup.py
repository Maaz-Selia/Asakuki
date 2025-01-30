from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import time
import tinytuya
import logging


class Diffuser(App):
    def build(self):

        #Initialise Diffuser Object
        self.d = tinytuya.DiffuserDevice(
            dev_id='bf0b43e24218f44c8axniv',
            address='Auto',      # Or set to 'Auto' to auto-discover IP address
            local_key='t~Yb#8Y\'d1fh<fFi', 
            version=3.4)
        
        #Initialise Window
        self.window = GridLayout()
        self.window.cols = 1

        # Power Button
        self.button = Button(text="Power")
        self.button.bind(on_press=self._toggle_power)
        self.window.add_widget(self.button)

        # Spray Buttons
        self.button = Button(text="off")
        self.button.bind(on_press=self._set_spray)
        self.window.add_widget(self.button)

        self.button = Button(text="small")
        self.button.bind(on_press=self._set_spray)
        self.window.add_widget(self.button)

        self.button = Button(text="big")
        self.button.bind(on_press=self._set_spray)
        self.window.add_widget(self.button)

        # Colour Picker
        currentColour = self.d.colour[0:6]
        self.colourpicker = ColorPicker(hex_color=currentColour)
        self.colourpicker.hex_color = currentColour
        self.colourpicker.bind(color=self._set_colour)
        self.window.add_widget(self.colourpicker)

        #Brightness Slider
        currentBrightness = self.d.brightness
        self.slider = Slider(min=-0, max=255, step=5, value=currentBrightness, value_track=True)
        self.slider.bind(value=self._set_brightness)
        self.window.add_widget(self.slider)

        #Intermittent mode
        self.intermittence = False

        self.interval = TextInput(multiline=False, text="2.5")
        self.window.add_widget(self.interval)

        self.button = Button(text="Intermittent Mode")
        self.button.bind(on_press=self._toggle_intermittence)
        self.window.add_widget(self.button)

        return self.window

    def _toggle_power(self, instance):
        return self.d.toggle_power()
    
    def _set_spray(self, instance):
        if self.intermittence:
            Clock.unschedule(self._intermittence_task)
            self.intermittence = False
        return self.d.set_spray(str(instance.text))
    
    def _set_colour_mode(self, instance):
        return self.d.set_colour_mode(str(instance.text))
    
    def _set_colour(self, instance, value):
        return self.d.set_colour(str(instance.hex_color), self.slider.value)

    def _set_brightness(self, instance, touch):
        return self.d.set_brightness(int(instance.value))
    
    def _toggle_intermittence(self, instance):
        if not self.intermittence:
            self.intermittence = True
            interval = int(float(self.interval.text) * 60)
            #logging.debug(interval)
            self.d.set_spray("small")
            Clock.schedule_interval(self._intermittence_task , interval)
        else:
            Clock.unschedule(self._intermittence_task)
            self.intermittence = False
            
    def _intermittence_task(self, instance=None):
        if self.d.spray is "off":
            self.d.set_spray("small")
            #logging.debug("Spray turned on")
        else:
            self.d.set_spray("off")
            #logging.debug("Spray turned off")
   
if __name__ == "__main__":
    Diffuser().run()