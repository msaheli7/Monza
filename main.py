from kivy.app import App
from kivy.uix.label import Label

class MonzaApp(App):
    def build(self):
        return Label(text='Hello Monza!')

if __name__ == '__main__':
    MonzaApp().run()
