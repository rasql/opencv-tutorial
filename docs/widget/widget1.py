"""Add a trackbar."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Window()
        Text('Trackbar')
        cv.createTrackbar('x', App.win.win, 50, 100, self.trackbar)
            
    def trackbar(self, pos):
        print(pos)

if __name__ == '__main__':
    Demo().run()