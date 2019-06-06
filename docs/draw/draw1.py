"""Template for making OpenCV apps."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)

        win = Window('image', img)
        Rectangle((20, 20), (100, 100), YELLOW, -1)
        Rectangle((300, 200), (400, 250), CYAN, 5)
        Line((20, 20), (200, 100), BLUE, 5)
        win.draw()
        
        win2 = Window('image2', img)
        p0 = 300, 100        
        Circle(p0, 200, YELLOW, 1)
        Ellipse(p0, (100, 50), MAGENTA, 1)
        pts = np.array([[50, 50], [500, 20], [150, 190]], np.int32)
        Polygon(pts, MAGENTA, 4)
        Text('OpenCV', (100, 100), WHITE, 3)
        win2.draw()

if __name__ == '__main__':
    Demo().run()