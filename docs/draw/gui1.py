"""GUI buttons, input fields, listviews."""
from cvlib import *

L = 'Rectangle;Line;Circle;Ellipse;Polygon;Text'.split(';')
print(L)

def myfunction():
    print('This is myfunction')

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)
        Window('original', img)

        Button('Button 123', 'print(123)') 
        Button('hello', 'print("hello")')
        Button('myfunction', myfunction)
        Button('Button', Button)
        Button('Window', Window)
        Text('OpenCV', (100, 100), WHITE, 1)

        Combobox('Days', 'Mon;Tue;Wed', 'print(self.get())', (300, 100))
        Combobox('Options', 'A;B;C', 'print(self.get())')

        Listbox('A;B;C;D;E', '')

        
if __name__ == '__main__':
    Demo().run()