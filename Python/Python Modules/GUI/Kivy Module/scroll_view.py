from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class Scroll_ViewApp(App):
    pass

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        for i in range(100):
            self.add_widget(Button(text=str(i), size_hint=(None, None), width="100dp", height="100dp"))

class ScrollViewExample(ScrollView):
    pass


Scroll_ViewApp().run()
