"""Display different font thickness."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        for t in (1, 2, 4, 8):
            text = 'thickness={}'.format(t)
            Text(text, thickness=t, color=YELLOW)

        Text('ABC', pos=(250, 20), fontScale=6, thickness=1, 
            fontFace=cv.FONT_HERSHEY_DUPLEX)

if __name__ == '__main__':
    Demo().run()