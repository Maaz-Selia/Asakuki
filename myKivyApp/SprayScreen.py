from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

class SprayScreen(Screen):
    def __init__(self, **kwargs):
        super(SprayScreen, self).__init__(**kwargs)

        self.diffuser = App.get_running_app().get_diffuser()

        self.window = GridLayout()

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

        #Intermittent mode
        self.intermittence = False

        self.interval = TextInput(multiline=False, text="2.5")
        self.window.add_widget(self.interval)

        self.button = Button(text="Intermittent Mode")
        self.button.bind(on_press=self._toggle_intermittence)
        self.window.add_widget(self.button)

        self.button = Button(text="Go to Home Screen")
        self.button.bind(on_press=self.go_to_home_screen)
        self.window.add_widget(self.button)

        self.add_widget(self.window)

    def go_to_home_screen(self, instance):
        self.manager.current = 'home_screen'  # Switch to home screen

    def _set_spray(self, instance):
        if self.intermittence:
            Clock.unschedule(self._intermittence_task)
            self.intermittence = False
        return self.diffuser.set_spray(str(instance.text))
    
    def _toggle_intermittence(self, instance):
        try:
            if not self.intermittence:
                self.intermittence = True
                interval = int(abs(float(self.interval.text)) * 60)
                #logging.debug(interval)
                self.diffuser.set_spray("small")
                Clock.schedule_interval(self._intermittence_task , interval)
            else:
                Clock.unschedule(self._intermittence_task)
                self.intermittence = False
        except ValueError:
            return
            
    def _intermittence_task(self, instance):
        if self.diffuser.spray is "off":
            self.diffuser.set_spray("small")
            #logging.debug("Spray turned on")
        else:
            self.diffuser.set_spray("off")
            #logging.debug("Spray turned off")