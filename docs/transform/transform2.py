"""Rotation."""
from cvlib import *
import math

class MyWindow(Window):
    def __init__(self, win, img):
        super(MyWindow, self).__init__(win, img)
        self.objects.append(Line(self.img, (0, 0), (0, 0), RED, 1))

    def mouse(self, event, x, y, flags, param):
        print(event, x, y)

        if event == cv.EVENT_LBUTTONDOWN:
            self.x = x
            self.y = y
            self.objects[-1].p0 = (x, y)

        elif event == cv.EVENT_MOUSEMOVE:
            self.objects[-1].p1 = (x, y)

            dx = x - self.x
            dy = y - self.y
            d = math.sqrt(dx**2 + dy**2)
            alpha = -math.degrees(math.atan2(dy, dx))
            M = cv.getRotationMatrix2D((self.x, self.y), alpha, d/100)

            img = cv.warpAffine(self.img0, M, (self.w, self.h))
            Window('result', img).draw()

        self.draw()   

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)
        MyWindow('image', img)
        
if __name__ == '__main__':
    Demo().run()