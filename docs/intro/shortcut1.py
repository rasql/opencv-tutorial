"""Template for making OpenCV apps."""
from cvlib import *

shortcuts = {
    'h':'print("hello")',
    'w':'Window()',
    '1':'print(123)w',
}

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        self.shortcuts = shortcuts

        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)
        Window('window', img)
        Window('window2', img)
        Window()

if __name__ == '__main__':
    Demo().run()