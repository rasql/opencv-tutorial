"""Draw a button to a window with a circle."""
from cvlib import *
import math

class Window:
    """Create a window with an image."""
    def __init__(self, win, img):
        self.win = win
        self.img0 = img.copy()
        self.img = img
        self.d = 2
        self.col = GREEN
        cv.imshow(win, img)
        cv.setMouseCallback(win, self.cb)
        self.text = 'Overlay of window: ' + self.win
        cv.displayOverlay(self.win, self.text, 2000)
        cv.displayStatusBar(self.win, 'Statusbar', 2000)

        cv.createButton('Button' + win, print)
        cv.createTrackbar('x', win, 50, 100, print)

    def cb(self, event, x, y, *args):
        """Mouse callback."""
        global k
        print('mouse in', self.win, event, x, y, *args)
        h, w = self.img.shape[:2]
        self.img = self.img0.copy()

        # draw a crosshair
        cv.line(self.img, (0, y), (w, y), RED, 1)
        cv.line(self.img, (x, 0), (x, h), RED, 1)

        # draw a shape (rectangle, circle)
        if event == 1:
            self.p0 = x, y
            self.text = 'p0 = ({}, {})'.format(x, y)
            cv.displayStatusBar(self.win, self.text, 2000)
            cv.displayOverlay(self.win, self.text, 1000)
            
        elif event == 0:
            if k == 'r':
                cv.rectangle(self.img, self.p0, (x, y), self.col, self.d)
            elif k == 'l':
                cv.line(self.img, self.p0, (x, y), self.col, self.d)
            elif k == 'c':
                dx = x - self.p0[0]
                dy = y - self.p0[1]
                r = int(math.sqrt(dx**2 + dy**2))
                cv.circle(self.img, self.p0, r, self.col, self.d)
        
        cv.imshow(self.win, self.img)
        

class Button:
    """Draw a button to a window."""
    def __init__(self, img, label='Button', pos=(100, 50), size=(100, 40), fg=RED, bg=BLUE):
        x0, y0 = pos
        w, h = size
        x1 = x0 + w
        y1 = y0 + h
        d = 10
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.rectangle(img, pos, (x1, y1), bg, -1)
        cv.putText(img, label, (x0+d, y1-d), font, 1, fg, 2, cv.LINE_AA)

file = 'messi.jpg'
img = cv.imread(file, cv.IMREAD_COLOR)
img1 = cv.cvtColor(img, cv.COLOR_BGR2HSV)

Button(img)
Button(img1)

Window('image_BGR',img)
Window('image_HSV',img1)

cv.displayOverlay('image_BGR', 'Hello')

k = 'r'
while True:
    k = cv.waitKey(0)
    print(k, chr(k))
    k = chr(k)

cv.destroyAllWindows()