"""Display a polygon object."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)

        win = Window('window', img)

        Text('hello', (0, 100))
        Text('world', (20, 200), fontScale=4, thickness=4)
        
        pts = np.array([[200, 100], [100, 350], [500, 400]])
        Polygon(pts, color=YELLOW, thickness=5, isClosed=True)
       
        win.draw()

if __name__ == '__main__':
    Demo().run()