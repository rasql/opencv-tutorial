"""Add optional parameters to ellipse."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)

        win = Window('window', img)
        
        Ellipse((200, 100), (200, 100), CYAN, 2)
        Ellipse((200, 200), (200, 100), BLUE, 2, a0=45)
        Ellipse((200, 300), (200, 100), RED, -1, a0=-45, a1=45, a2=270)

        win.draw()

if __name__ == '__main__':
    Demo().run()