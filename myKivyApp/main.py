from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from HomeScreen import HomeScreen
from SprayScreen import SprayScreen
from LightScreen import LightScreen
import tinytuya

class Diffuser(App):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        #Initialise Diffuser Object
        self.diffuser = tinytuya.DiffuserDevice(
            dev_id='bf0b43e24218f44c8axniv',
            address='Auto',      # Or set to 'Auto' to auto-discover IP address
            local_key='t~Yb#8Y\'d1fh<fFi', 
            version=3.4)

    def build(self):

        screen_manager = ScreenManager()

        home_screen = HomeScreen(name='home_screen')
        spray_screen = SprayScreen(name='spray_screen')
        light_screen = LightScreen(name='light_screen')


        screen_manager.add_widget(home_screen)
        screen_manager.add_widget(spray_screen)
        screen_manager.add_widget(light_screen)

        return screen_manager
    
    def get_diffuser(self):
        return self.diffuser # Method to access the variable from MyApp

if __name__ == "__main__":
    Diffuser().run()