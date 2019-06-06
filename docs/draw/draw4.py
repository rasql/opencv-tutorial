"""Add graphics objects to current window."""
from cvlib import *

L = ['Rectangle', 'Line', 'Ellipse', 'Polygon', 'Circle', 'Text']

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)

        win = Window('window', img)
        Rectangle((20, 20), (100, 100), YELLOW, -1)
        Ellipse((200, 120), (100, 60), CYAN, -1)
        Line((20, 20), (200, 100), BLUE, 5)
        Line((330, 20), (550, 190), GREEN, 5)
        Circle((130, 220), 100, GREEN, 5)
        
        Text('hello', (220, 220), GREEN)
        Text('OpenCV', (220, 320), RED, 3)
        
        pts = np.array([[10,5],[220,30],[70,320],[350,310]], np.int32)
        Polygon(pts, RED, 2)

        win.draw()

if __name__ == '__main__':
    Demo().run()