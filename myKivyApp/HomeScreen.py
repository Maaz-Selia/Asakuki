from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        self.diffuser = App.get_running_app().get_diffuser()

        self.window = GridLayout(rows = 5)

        # Power Button
        self.button = Button(text="Power")
        self.button.bind(on_press=self._toggle_power)
        self.window.add_widget(self.button)


        button = Button(text="Spray Control")
        button.bind(on_press=self.go_to_spray_screen)
        self.window.add_widget(button)

        button = Button(text="Light Control")
        button.bind(on_press=self.go_to_light_screen)
        self.window.add_widget(button)

        button = Button(text="Calculate Control")
        button.bind(on_press=self.go_to_track_screen)
        self.window.add_widget(button)

        button = Button(text="Records")
        button.bind(on_press=self.go_to_record_screen)
        self.window.add_widget(button)

        self.add_widget(self.window)

    def go_to_spray_screen(self, instance):
        self.manager.current = 'spray_screen'

    def go_to_light_screen(self, instance):
        self.manager.current = 'light_screen'

    def go_to_track_screen(self, instance):
        self.manager.current = 'track_screen'

    def go_to_record_screen(self, instance):
        self.manager.current = 'record_screen'

    def _toggle_power(self, instance):
        return self.diffuser.toggle_power()