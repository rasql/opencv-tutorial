"""Template for making OpenCV apps."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)

if __name__ == '__main__':
    Demo().run()