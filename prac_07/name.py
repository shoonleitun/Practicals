from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class NameApp(App):
    @property
    def name(self):
        return self._name

    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Name"
        self.root = Builder.load_file('name.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for i in self.name:
            temp_button = Button(text=i, id=i)
            self.root.ids.entries_box.add_widget(temp_button)

    def press_entry(self, instance):

        name = instance.id
        self.status_text = "Name: {}".format(name, self.name[name])

    @name.setter
    def name(self, value):
        self._name = value


NameApp().run()
