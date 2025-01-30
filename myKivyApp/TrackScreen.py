from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class TrackScreen(Screen):
    def __init__(self, **kwargs):
        super(TrackScreen, self).__init__(**kwargs)

        self.diffuser = App.get_running_app().get_diffuser()

        self.window = GridLayout()

        button = Button(text="Go to Home Screen")
        button.bind(on_press=self.go_to_home_screen)
        self.window.add_widget(button)

        self.add_widget(self.window)

    def go_to_home_screen(self, instance):
        self.manager.current = 'home_screen'