"""Display instances of the Object class."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
                
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)
        win = Window('window', img)

        Object(color=MAGENTA, shift=2)
        Object(color=WHITE)
        Object(thickness=3)

        Object((300, 30), (200, 60), color=GREEN)
        Object(thickness=5)
        Object()

        App.win.draw()

if __name__ == '__main__':
    Demo().run()