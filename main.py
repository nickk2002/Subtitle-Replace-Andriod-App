from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from subtitles import subtitles_diactritice_all
from kivy.uix.filechooser import FileChooserListView

class LoadDialog(FloatLayout):
    cancel = ObjectProperty(None)
    load = ObjectProperty(None)
    pass

class Root(FloatLayout):
    text = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.dismiss_popup()
        text = "Hei Acum se ruleaza"
        subtitles_diactritice_all(path)



class Editor(App):
    def build(self):
        return FileChooserListView()


Editor().run()