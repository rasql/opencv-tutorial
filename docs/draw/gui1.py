"""GUI buttons, input fields, listviews."""
from cvlib import *

L = 'Rectangle;Line;Circle;Ellipse;Polygon;Text'.split(';')
print(L)


class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('draw/sudoku.jpg', 0)
        Window('original', img)

        Button('Button 2', 'print(123)', (100, 100))
        Button('Button 2', 'print("hello")')

        Combobox('Days', 'Mon;Tue;Wed', 'print(self.get())', (300, 100))
        Combobox('Options', 'A;B;C', 'print(self.get())')

        Listbox('A;B;C;D;E')
        
if __name__ == '__main__':
    Demo().run()