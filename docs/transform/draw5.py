"""Display Text objects."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)

        win = Window('window', img)
        
        Text('OpenCV', (0, 100))
        Text('OpenCV', (0, 200), color=GREEN)
        Text('OpenCV', (0, 300), fontScale=2, thickness=2)
        
        win.draw()

if __name__ == '__main__':
    Demo().run()