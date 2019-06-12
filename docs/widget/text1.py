"""Display different font scales."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        for scale in (0.5, 1, 2, 3):
            text = 'fontScale={}'.format(scale)
            Text(text, fontScale=scale, thickness=1, color=YELLOW)

if __name__ == '__main__':
    Demo().run()