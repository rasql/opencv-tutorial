import cv2 as cv
import numpy as np
import os, sys, math

BLACK = (0, 0, 0)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)

class Window:
    """Create a window with an image."""
    def __init__(self, win='window', img=[]):
        App.wins.append(self)
        App.win = self

        self.mouse_down = lambda *args : None
        self.mouse_move = lambda *args : None
        self.mouse_up = lambda *args: None

        self.win = win
        if len(img) == 0:
            img = np.zeros((200, 600, 3), np.uint8)
        self.img = img
        self.img0 = img.copy()
        self.h = self.img.shape[0]
        self.w = self.img.shape[1]
        self.x = self.w // 2
        self.y = self.h // 2
        
        self.objects = []
        self.obj_id = 0
        cv.imshow(win, img)

        self.d = 2
        self.col = GREEN
        cv.setMouseCallback(win, self.mouse)
        self.text = 'Overlay of window: ' + self.win
        cv.displayOverlay(self.win, self.text, 2000)
        cv.displayStatusBar(self.win, 'Statusbar', 2000)

        cv.createButton('Button' + win, print)
        cv.createTrackbar('x', win, 100, 255, self.trackbar)

    def draw(self):
        self.img[:] = self.img0[:]
        
        # draw all obejcts
        for obj in self.objects:
            obj.draw()

        # draw a crosshair
        p = self.img[self.y, self.x, :]
        cv.line(self.img, (0, self.y), (self.w, self.y), RED, 1)
        cv.line(self.img, (self.x, 0), (self.x, self.h), RED, 1)
        self.img[self.y, self.x, :] = p[:]

        cv.imshow(self.win, self.img)

    def mouse(self, event, x, y, *args):
        """Mouse callback."""
        self.event = event
        self.x = x
        self.y = y
        global k
        print('mouse in', self.win, event, x, y, *args)
   
        # draw a shape (rectangle, circle, line)
        if event == cv.EVENT_LBUTTONDOWN:  # press left button
            App.win = self
            self.p0 = x, y
            self.p1 = x, y
            self.text = 'p0 = ({}, {})'.format(x, y)
            cv.displayStatusBar(self.win, self.text, 2000)
            cv.displayOverlay(self.win, self.text, 1000)
            print(self.mouse_down)
            self.mouse_down(self)
            
        elif event == cv.EVENT_MOUSEMOVE:  # mouse mouve
            k = App.k
            self.p1 = (x, y)
            if k == 'r':
                cv.rectangle(self.img, self.p0, self.p1, self.col, self.d)
            elif k == 'l':
                cv.line(self.img, self.p0, self.p1, self.col, self.d)
            elif k == 'c':
                dx = x - self.p0[0]
                dy = y - self.p0[1]
                r = int(math.sqrt(dx**2 + dy**2))
                cv.circle(self.img, self.p0, r, self.col, self.d)
        
        elif event == cv.EVENT_LBUTTONUP: # mouse release
            cv.displayOverlay(self.win, 'Mouse released', 1000)
            rect = Rectangle(self.img, self.p0, self.p1, self.col, self.d)
            self.objects.append(rect)

        self.draw()

    def trackbar(self, x):
        """Trackbar callback function"""
        self.x = x
        text = 'Trackbar = {}'.format(x)
        cv.displayOverlay(self.win, text, 1000)
        cv.imshow(self.win, self.img)

    def show_object(self):
        """Cycle through the objects and display in Overlay."""
        n = len(self.objects)
        self.obj_id += 1
        self.obj_id %= n
        print(n, self.obj_id)
        text = str(self.objects[self.obj_id])
        cv.displayOverlay(self.win, text, 1000)
        cv.imshow(self.win, self.img)

class Line:
    """Create a line object."""
    def __init__(self, img, p0, p1, col, d):
        self.img = img
        self.p0 = p0
        self.p1 = p1
        self.col = col
        self.d = d
    
    def __str__(self):
        return 'Line ({}, {})'.format(self.p0[0], self.p0[0])

    def draw(self):
        cv.line(self.img, self.p0, self.p1, self.col, self.d)

class Rectangle:
    """Create a rectangle object."""
    def __init__(self, img, p0, p1, col, d):
        self.img = img
        self.p0 = p0
        self.p1 = p1
        self.col = col
        self.d = d

    def __str__(self):
        return 'Rectangle({}, {})'.format(self.p0[0], self.p0[1])

    def draw(self):
        cv.rectangle(self.img, self.p0, self.p1, self.col, self.d)

class Circle:
    def __init__(self, img, p0, r, col, d):
        self.img = img
        self.p0 = p0
        self.r = r
        self.col = col
        self.d = d

    def draw(self):
        cv.circle(self.img, self.p0, self.r, self.col, self.d)

class Ellipse:
    def __init__(self, img, p0, size, col, d):
        self.img = img
        self.p0 = p0
        self.size = size
        self.col = col
        self.d = d

    def draw(self):
        cv.ellipse(self.img, self.p0, self.size, 0, 0, 360, self.col, self.d)

class Polygon:
    def __init__(self, img, pts, col, d):
        self.img = img
        self.pts = pts
        self.col = col
        self.d = d

    def draw(self):
        cv.polylines(self.img, [self.pts], True, self.col, self.d)

class Text:
    def __init__(self, img, text, p0, col):
        self.img = img
        self.text = text
        self.p0 = p0
        self.col = col
        self.font = cv.FONT_HERSHEY_SIMPLEX

    def draw(self):
        cv.putText(self.img, self.text, self.p0, self.font, 1, self.col, 2, cv.LINE_AA)


class App:
    k = ''
    wins = []
    def __init__(self):
        self.shortcuts = {}
        img = np.zeros((200, 600, 3), np.uint8)
        img[:] = 127
        self.overlay = ''
        Window()

    def run(self):
        """Run the main event loop."""
        while App.k != 'q':
            k = cv.waitKey(0)
            print(k, chr(k))
            App.k = chr(k)
            self.overlay += App.k
            cv.displayOverlay('window', self.overlay)

            if App.k == '\t':
                print('tab')

            if App.k == 'i':
                self.inspect()

            if App.k == 'o':
                App.win.show_object()

            if App.k == 'd':
                App.win.objects.pop(App.win.obj_id)
                App.win.draw()
                
            d = self.shortcuts
            if App.k in d.keys():
                try:
                    exec(d[App.k])
                except:
                    print('Shortcut error:', sys.exc_info()[0])
                    print(d[App.k])
                    # raise
            
        cv.destroyAllWindows()

    def inspect(self):
        print('---inspect---', )
        print('App.wins:', App.wins)
        print('App.win:', App.win)

        for obj in App.win.objects:
            print(obj)
        

if __name__ == '__main__':
    App().run()