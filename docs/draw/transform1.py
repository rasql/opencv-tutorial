"""Translation."""
from cvlib import *

class MyWindow(Window):
    def __init__(self, win, img):
        super(MyWindow, self).__init__(win, img)

    def mouse(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN: 
            self.x = x
            self.y = y

            M = np.float32([[1, 0, x], [0, 1, y]])
            img = cv.warpAffine(self.img0, M, (self.w, self.h))
            Window('result', img)
            self.draw()   

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)
        MyWindow('image', img)
        
if __name__ == '__main__':
    Demo().run()