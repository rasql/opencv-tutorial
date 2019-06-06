"""Add optional parameters to graphics objects."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)

        win = Window('window', img)
        
        Text('OpenCV', (0, 100), GREEN, 1)
        t = Text('OpenCV', (100, 100), RED, 2)
        Text('OpenCV', (300, 100), BLUE, 3)

        t.set_text('CV')
        win.draw()

if __name__ == '__main__':
    Demo().run()