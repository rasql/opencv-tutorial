"""Display instances of the Object class."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
                
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)
        win = Window('window', img)

        Object()
        Object()
        Object(size=(140, 60))
        Object()

        Object(pos=(200, 50))
        Object()
        Object(size=(50, 50), dir=(1, 0))
        Object()
        Object()
        Object()
        
        Window('win2', img)
        Object()
        Object()
        Object(size=(140, 60))
        Object()

        Object(pos=(200, 50))
        Object()
        Object(dir=(1, 0))
        Object()

        App.win.draw()

if __name__ == '__main__':
    Demo().run()