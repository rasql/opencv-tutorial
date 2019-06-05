"""Template for making OpenCV apps."""
from cvlib import *

L = ['Rectangle', 'Line', 'Ellipse', 'Polygon', 'Circle', 'Text']

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)

if __name__ == '__main__':
    Demo().run()