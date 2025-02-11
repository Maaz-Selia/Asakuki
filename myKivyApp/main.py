from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.gridlayout import GridLayout
from HomeScreen import HomeScreen
from SprayScreen import SprayScreen
from LightScreen import LightScreen
from TrackScreen import TrackScreen
from RecordScreen import RecordScreen
from JSONDatabase import JSONDatabase
from DiffuserDevice import DiffuserDevice

class Diffuser(App):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        Window.size = (360, 640)

        #Initialise Diffuser Object
        self.diffuser = DiffuserDevice(
            dev_id='bf0b43e24218f44c8axniv',
            address='Auto',      # Or set to 'Auto' to auto-discover IP address
            local_key='t~Yb#8Y\'d1fh<fFi',
            version=3.4)
        
        self.db = JSONDatabase()

    def build(self):

        self.screen_manager = ScreenManager()

        for screen in [HomeScreen(name='home_screen'),
                SprayScreen(name='spray_screen'),
                LightScreen(name='light_screen'),
                TrackScreen(name='track_screen'),
                RecordScreen(name='record_screen')]:
            screen.window.cols = 1
            screen.window.spacing = 20
            screen.window.padding = 20
            #screen.window.orientation = 'tb-lr'
            #screen.window.size_hint = (0.5, 0.5)
            #screen.window.size_hint=(1, 1)
            #screen.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

            self.screen_manager.add_widget(screen)

        return self.screen_manager
    
    def get_diffuser(self):
        return self.diffuser
    
    def get_db(self):
        return self.db
    
    def get_intermittance(self):
        sprayScreen = self.screen_manager.get_screen('spray_screen')
        if sprayScreen.intermittence:
            return 1
        else:
            return 0

if __name__ == "__main__":
    Diffuser().run()