"""Add graphics objects to current window."""
from cvlib import *

L = ['Rectangle', 'Line', 'Ellipse', 'Polygon', 'Circle', 'Text']

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)

        win = Window('window', img)
        Arrow((50, 50), (250, 50))
        Line((50, 100), (250, 150), thickness=3)
        Marker((50, 150))
        Marker((100, 150), markerType=cv.MARKER_DIAMOND, thickness=2)
        
        Rectangle((50, 200), (250, 250), thickness=-1)
        Rectangle((50, 200), (250, 250), thickness=3, color=YELLOW)
        
        Circle((100, 250), 50, thickness=-1)
        Circle((100, 250), 50, thickness=5, color=RED)
        
        win.draw()

if __name__ == '__main__':
    Demo().run()