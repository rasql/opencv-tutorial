"""Perspective Transformation."""
from cvlib import *
import math

class MyWindow(Window):
    def __init__(self, win, img):
        super(MyWindow, self).__init__(win, img)
        self.pts1 = []
        self.pts2 = []
        
    def mouse(self, event, x, y, flags, param):
        n = len(self.objects)
        if event == cv.EVENT_LBUTTONDOWN:
            self.x = x
            self.y = y
            if n >= 12:
                self.objects = []
                self.pts1 = []
                self.pts2 = []
            if n%3 == 0:
                self.objects.append(Circle(self.img, (x, y), 10, GREEN, 2))
                self.pts1.append([x, y])
            if n%3 == 1:
                p0 = self.objects[-1].p0
                self.objects.append(Line(self.img, p0, (x, y), GREEN, 2))
                self.objects.append(Circle(self.img, (x, y), 10, RED, 2))
                self.pts2.append([x, y])

            if n == 10:

                self.objects.append(Text(self.img, 'Perspective Transform', (100, 100), BLUE))
                p1 = np.float32(self.pts1)
                p2 = np.float32(self.pts2)

                M = cv.getPerspectiveTransform(p1, p2)
                dst = cv.warpPerspective(self.img, M, (self.w, self.h))
                Window('result', dst)

        self.draw()   

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('draw/sudoku.jpg', cv.IMREAD_COLOR)
        MyWindow('image', img)
        
if __name__ == '__main__':
    Demo().run()