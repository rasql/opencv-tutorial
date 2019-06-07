"""Add optional parameters to ellipse."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)

        win = Window('window', img)
        
        Ellipse((200, 100), (100, 50))
        Ellipse((200, 200), (100, 50), angle=30, color=RED)
        Ellipse((200, 300), (100, 50), angle=60)

        x, y = 450, 60
        Ellipse.options['angle'] = 0
        Ellipse.options['thickness'] = 5
        Ellipse.options['color'] = MAGENTA
        for i in range(5):
            Ellipse((x, y + i*120), (100, 50), startAngle=i*90)

        win.draw()

if __name__ == '__main__':
    Demo().run()