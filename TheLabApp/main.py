from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.graphics import Rectangle, Ellipse
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color


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

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100,100,400,500), width=2)
            Color(0,1,0)
            Line(circle=(400,200,80))
            Line(rectangle=(500,300,80,100), width=2)
            self.rect = Rectangle(pos=(700,200), size=(150,100))
    def on_button_a_click(self):
        # unpacked the x and y coordinates of rectangle
        x,y = self.rect.pos
        # unpacked the widht and height of the rectangle
        w,h = self.rect.size
        # inc variable will allow the rectangle to move 10 units to the right
        inc = dp(10)
        diff = self.width - (x+w)
        if diff < inc:
            inc = diff
        
        x += inc
        self.rect.pos = (x,y)

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            Color(.5,.2,.6)
            self.ball = Ellipse(pos=(100,100), size=(self.ball_size,self.ball_size))
        # This schedule_interval function takes a function(st parameter) and amount of time in seconds(2nd parameter)
        # Every n seconds the function passed as the first arguments will be called
        Clock.schedule_interval(self.update,1/60)
    # this funtion gets called once the window is running
    def on_size(self,*args):
        # print(f"on size: {self.width}, {self.height}")
        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)
    # every function call that got called from the Clock.schedule_interval function needs to have a parameter
    # dt -> delta time
    # The point of this update function is to be able to update the position of the ball every n seconds
    def update(self,dt):
        # print("Update")
        x,y = self.ball.pos
        x += self.vx
        y += self.vy

        # Here the first rebound will happen at the top of the screen
        # so we must keep the ball below the height of the screen by setting the 
        # y position which is the lower left point of the circle back below the height of the screen
        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            self.vy = -self.vy
        # For this condition the ball will rebound against the right side of the screen
        # therefoere the x position needs to be updated so that the ball remains in the screen 
        # and does not pass the right side
        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = -self.vx
        # The following two conditions check for lower part of the screen and, left side of screen
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx    

        self.ball.pos = (x,y)

class CanvasExample6(Widget):
    pass

class CanvasExample7(BoxLayout):
    pass 
TheLabApp().run()