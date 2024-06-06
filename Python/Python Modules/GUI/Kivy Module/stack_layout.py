from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button


class Stack_LayoutApp(App):
    pass


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.spacing = "0.5dp"

        ### Without fix size
        # for i in range(20):
        #     self.add_widget(Button(text=str(i), size_hint=(.2, .2)))

        ### Here the buttons will move acording to the screen size
        for i in range(20):
            self.add_widget(Button(text=str(i), size_hint=(None, None), width="100dp", height="100dp"))


Stack_LayoutApp().run()
