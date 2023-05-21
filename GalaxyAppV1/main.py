from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
class MainWidget(Widget):
    # create these properties in order to be able to update each x and y coordinate dynamically
    # in order to view the value of each property as the window is resized we can define a function as such:
    # on_<propname> -> Ex. def on_perspective_point_x(self,widget,value):
    # Documentation on this can be found here: https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties.OptionProperty
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # print(f"Initial W: {self.width} H: {self.height}")

    def on_parent(self, widget, parent):
        # print(f"On Parent W: {self.width} H: {self.height}")
        pass
        
    # in order to dynamically view the size property values 
    # we use the on_<propname> syntax for function name
    def on_size(self,*args):
        # print(f"On size W: {self.width} H: {self.height}")
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height * 0.75
        pass

    def on_perspective_point_x(self, widget, value):
        # print(f"PX: {value}")
        pass

    def on_perspective_point_y(self, widget, value):
        # print(f"PY: {value}")
        pass


class GalaxyApp(App):
    pass

GalaxyApp().run()