"""Show the different markers."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Window()
        markers = cv_dir('MARKER.*')

        for marker in markers:
            Text(marker, fontScale=0.5, thickness=1)

        for m in range(7):
            Marker(pos=(300, m*25+20), markerType=m)

if __name__ == '__main__':
    Demo().run()