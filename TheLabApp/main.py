from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp


# class WidgetsExample(GridLayout):
#     # defines a variable of type string with a default value of "Hello"
#     my_text = StringProperty("1")
#     count_enabled = BooleanProperty(False)
#     text_input_str = StringProperty("Kivy Tutorial")
#     count = 1
#     def on_button_click(self):
#         # only when the button is set to on will the label text be incremented
#         if self.count_enabled:
#             self.count += 1
#             self.my_text = str(self.count)
       
#     def on_toggle_button_state(self,widget):
#         print(f"toggle state: {widget.state}")
#         if widget.state == 'normal':
#             widget.text = "OFF"
#             self.count_enabled = False
#         else:
#             widget.text = "ON"
#             self.count_enabled = True
    
#     def on_switch_active(self,widget):
#         print(f"Switch: {widget.active}")

#     def on_slider_value(self,widget):
#         print(f"Slider value: {int(widget.value)}")
#     # This method executes when the textbox is set to be a single line
#     # then the logic behind this is that when text is entered on to the TextInput widget
#     # it will only update the labels text to the same text entered on the TextInput once 'enter' is pressed
#     def on_text_validate(self,widget):
#         self.text_input_str = widget.text

# class StackLayoutExample(StackLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         # self.orientation = "lr-bt"
#         for i in range(1,101):
#             #size = dp(100) + i * 10
#             size = dp(100)
#             b = Button(text=str(i),size_hint=(None,None), size=(size, size))
#             self.add_widget(b)
#         # for i in range():
#         #     pass


# # class GridLayoutExample(GridLayout):
# #     pass
# class AnchorLayoutExample(AnchorLayout):
#     pass
# class BoxLayoutExample(BoxLayout):
#     pass
#     # def __init__(self, **kwargs):
#     #     super().__init__(**kwargs)
#     #     self.orientation = "vertical"
#     #     b1 = Button(text="A")
#     #     b2 = Button(text="B")
#     #     b3 = Button(text="C")
#     #     self.add_widget(b1)
#     #     self.add_widget(b2)
#     #     self.add_widget(b3)

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

TheLabApp().run()