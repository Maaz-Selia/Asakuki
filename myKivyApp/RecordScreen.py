from datetime import datetime
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.app import App


class RecordScreen(Screen):
    def __init__(self, **kwargs):
        super(RecordScreen, self).__init__(**kwargs)

        self.diffuser = App.get_running_app().get_diffuser()
        self.db = App.get_running_app().get_db()

        self.window = GridLayout()

        records = self.db.load_records()

        self.recordsGrid = GridLayout(cols=2, spacing=20, padding=10)
        
        if records != []:
            for r in records:
                tObj = datetime.strptime(str(r['timestamp']), "%Y-%m-%d %H:%M:%S")
                self.rec = Label(text = str(r['ml']) + "ml, " + str(r['drops']) + " drops")
                self.time = Label(text = tObj.strftime("%B %d at %I:%M %p"))
                self.recordsGrid.add_widget(self.rec)
                self.recordsGrid.add_widget(self.time)
        
        self.window.add_widget(self.recordsGrid)
        
        button = Button(text="Go to Home Screen")
        button.bind(on_release=self.go_to_home_screen)
        self.window.add_widget(button)

        self.add_widget(self.window)

    def go_to_home_screen(self, instance):
        self.manager.current = 'home_screen'

    def add_record(self, instance):
        """Add a new record from user input."""
        ml = self.ml.text
        drops = self.drops.text
        if ml.isdigit() and drops.isdigit():
            self.db.add_record(int(ml), int(drops))
            self.ml.text = ""
            self.drops.text = ""