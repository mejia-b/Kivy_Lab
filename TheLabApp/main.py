from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp


class WidgetsExample(GridLayout):
    # defines a variable of type string with a default value of "Hello"
    my_text = StringProperty("Hello")
    count = 0
    def on_button_click(self):
        self.count += 1
        print("You have clicked the button! :)")
        if self.count == 1:
            self.my_text = f"You have clicked the button {self.count} time"
        else:
           self.my_text = f"You have clicked the button {self.count} times" 

class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        for i in range(1,101):
            #size = dp(100) + i * 10
            size = dp(100)
            b = Button(text=str(i),size_hint=(None,None), size=(size, size))
            self.add_widget(b)
        # for i in range():
        #     pass


# class GridLayoutExample(GridLayout):
#     pass
class AnchorLayoutExample(AnchorLayout):
    pass
class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

TheLabApp().run()