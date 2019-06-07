"""Display different markers."""
from cvlib import *

markers = ( cv.MARKER_CROSS,
            cv.MARKER_DIAMOND,
            cv.MARKER_SQUARE,
            cv.MARKER_STAR,
            cv.MARKER_TILTED_CROSS,
            cv.MARKER_TRIANGLE_DOWN,
            cv.MARKER_TRIANGLE_UP)

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
    
        Window('window')

        x, y = 50, 50
        for m in markers:
            Marker((x, y), markerType=m)
            x += 50

        x, y = 50, 100
        for m in markers:
            Marker((x, y), markerType=m, thickness=3)
            x += 50

        App.win.draw()

if __name__ == '__main__':
    Demo().run()