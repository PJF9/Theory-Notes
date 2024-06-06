from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Box_LayoutApp(App):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    ### The same code that we write here we can also instead write it inside the .kv file
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     ### Creating the buttons.
    #     b1 = Button(text="Hay", size_hint=(.6, .4))
    #     b2 = Button(text="There")
    #     b3 = Button(text="Sir")
    #     l1 = Label(text="Example", color=(0, 1, 1, 1))

    #     ### Change the orientation of the box layout (vertical, horizontal: default)
    #     self.orientation = "vertical"

    #     ### Adding the widget to the layout
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)
    #     self.add_widget(l1)


Box_LayoutApp().run()
