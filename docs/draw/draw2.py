"""Display instances of the Arrow class."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()

        Window()
        x, y = 30, 30
        for d in (1, 2, 5, 10):
            Arrow((x, y), (x+200, y), thickness=d)
            y += 40

        x, y = 250, 30
        for d in (50, 100, 200, 300):
            Arrow((x, y), (x+d, y), thickness=2, color=GREEN)
            y += 40

        App.win.draw()

if __name__ == '__main__':
    Demo().run()