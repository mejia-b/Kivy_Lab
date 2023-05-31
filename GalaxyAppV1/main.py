from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.graphics import Color,Line
class MainWidget(Widget):
    # create these properties in order to be able to update each x and y coordinate dynamically
    # in order to view the value of each property as the window is resized we can define a function as such:
    # on_<propname> -> Ex. def on_perspective_point_x(self,widget,value):
    # Documentation on this can be found here: https://kivy.org/doc/stable/api-kivy.properties.html#kivy.properties.OptionProperty
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    
    V_NUM_LINES = 7
    V_LINES_SPACING = .1 # percentage of width size
    vertical_lines = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # print(f"Initial W: {self.width} H: {self.height}")
        self.init_vertical_lines()

    def on_parent(self, widget, parent):
        # print(f"On Parent W: {self.width} H: {self.height}")
        pass
        
    # in order to dynamically view the size property values 
    # we use the on_<propname> syntax for function name
    def on_size(self,*args):
        # print(f"On size W: {self.width} H: {self.height}")
        # self.perspective_point_x = self.width/2
        # self.perspective_point_y = self.height * 0.75
        self.update_vertical_lines()

    def on_perspective_point_x(self, widget, value):
        # print(f"PX: {value}")
        pass

    def on_perspective_point_y(self, widget, value):
        # print(f"PY: {value}")
        pass

    def init_vertical_lines(self):
        with self.canvas:
            Color(1,1,1)
            #self.line = Line(points=(100,0,100,100))
            for i in range(0,self.V_NUM_LINES):
                self.vertical_lines.append(Line())
    
    def update_vertical_lines(self):
        # x value will be middle of the screen 
        central_line_x = int(self.width/2)
        spacing = self.V_LINES_SPACING * self.width
        offset = -int(self.V_NUM_LINES/2)
        # print(f"Screen width: {self.width}, Screen height: {self.height}")
        # print(f"central_line: {central_line_x}")
        # print(f"spacing: {spacing}")
        # print(f"offset: {offset}")
        for i in range(0,self.V_NUM_LINES):
            line_x = int(central_line_x + offset * spacing)
            
            x1, y1 = self.transform(line_x, 0)
            x2, y2 = self.transform(line_x, self.height)
            self.vertical_lines[i].points = (x1,y1,x2,y2)
            # print(f"Line {i+1} points: {self.vertical_lines[i].points}")
            offset += 1

    def transform(self, x, y):
        # return self.transform_2D(x, y)
        return self.transfrom_perspective(x, y)
    
    def transform_2D(self, x, y):
        return int(x), int(y)
    
    def transfrom_perspective(self, x, y):
        tr_y = y * self.perspective_point_y / self.height
        if tr_y > self.perspective_point_y:
            tr_y = self.perspective_point_y

        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - tr_y
        proportion_y = diff_y / self.perspective_point_y

        tr_x = self.perspective_point_x + diff_x * proportion_y
        return int(tr_x), int(tr_y)


class GalaxyApp(App):
    pass

GalaxyApp().run()