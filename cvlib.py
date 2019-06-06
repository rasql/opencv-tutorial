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
    """Create a window with an image and add graphics objects."""
    def __init__(self, win='window', img=[]):
        App.wins.append(self)
        App.win = self

        self.win = win
        if len(img) == 0:
            img = np.zeros((200, 600, 3), np.uint8)
        self.img = img
        self.img0 = img.copy()
        
        self.objects = []
        self.obj_id = 0
        cv.imshow(win, img)
        self.overlay = 'Keys: '
        self.shortcuts = {  'o':'self.show_object()',
                            'd':'self.objects.pop(self.obj_id)', 
        }

        cv.setMouseCallback(win, self.mouse)

    def draw(self):
        """Reset the image and add graphics objects."""
        self.img[:] = self.img0[:]  

        for obj in self.objects:
            obj.draw()

        cv.imshow(self.win, self.img)
    
    def key(self, k):
        """Handle key press event."""

        # add key character to overlay
        if k == '\b':
            self.overlay = self.overlay[:-1]
        else:
            self.overlay += k
        cv.displayOverlay(self.win, self.overlay, 1000)
        
        if k == '\b':  # backspace
            for obj in self.objects:
                if obj.selected:
                    self.objects.remove(obj)    

        if k in self.shortcuts.keys():
            cmd = self.shortcuts[k]
            try:
                exec(cmd)
            except:
                print('Shortcut error:', sys.exc_info()[0], cmd)
        
        self.draw()

    def mouse(self, event, x, y, flags, param):
        """Mouse callback."""
        
        if event == cv.EVENT_LBUTTONDOWN:
            # draw_selection objects under mouse click
            for obj in self.objects:
                obj.selected = obj.is_inside(x, y)

            App.win = self
            self.p0 = x, y
            self.p1 = x, y
            self.text = 'p0 = ({}, {})'.format(x, y)
            cv.displayStatusBar(self.win, self.text, 2000)
            cv.displayOverlay(self.win, self.text, 1000)

            # draw rectangle if ALT key is pressed
            if flags == cv.EVENT_FLAG_ALTKEY:
                rect = Rectangle(self.img, (x, y), (x, y), RED, 3)
                self.objects.append(Rectangle(rect))
            
        elif event == cv.EVENT_MOUSEMOVE:
            if flags == cv.EVENT_FLAG_ALTKEY:
                self.objects[-1].set_p1(x, y)
                    
        elif event == cv.EVENT_LBUTTONUP:
            cv.displayOverlay(self.win, 'Mouse released', 1000)

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
        self.objects[self.obj_id].selected = False
        self.obj_id += 1
        self.obj_id %= n
        self.objects[self.obj_id].selected = True
        text = str(self.objects[self.obj_id])
        cv.displayOverlay(self.win, text, 1000)
        cv.imshow(self.win, self.img)


class Object():
    """General-purpose object."""
    def __init__(self, pts, col, d=1):
        App.win.objects.append(self)
        self.img = App.win.img
        self.pts = pts
        self.col = col
        self.d = d
        self.selected = False
        self.set_bbox()

    def __str__(self):
        x0, y0, x1, y1 = self.bbox
        return self.__class__.__name__ + ' at ({}, {}, {}, {})'.format(x0, y0, x1, y1)

    def is_inside(self, x, y):
        """Check if point (x, y) is inside the object."""
        x0, y0, x1, y1 = self.bbox
        return x0 <= x <= x1 and y0 <= y <= y1

    def draw_selection(self):
        """Draw a bounding box around the object if it is selected."""
        x0, y0, x1, y1 = self.bbox
        if self.selected:
            cv.rectangle(self.img, (x0, y0),(x1, y1), BLUE, 1)

    def set_bbox(self):
        """Set bounding box, size and center from point list."""
        xmin = xmax = self.pts[0][0]
        ymin = ymax = self.pts[0][1]
        for (x, y) in self.pts[1:]:
            if x > xmax:
                xmax = x
            if x < xmin:
                xmin = x
            if y > ymax:
                ymax = y
            if y < ymin:
                ymin = y
        w = xmax - xmin
        h = ymax - ymin
        self.size = w, h
        self.center = xmin + w//2, ymin + h//2
        self.bbox = xmin, ymin, xmax, ymax

    def set_p1(self, p1):
        self.p1 = p1
        self.set_bbox([self.p0, p1])


class Line(Object):
    """Create a line object."""
    def __init__(self, p0, p1, col, d):
        pts = [p0, p1]
        super(Line, self).__init__(pts, col, d)

    def draw(self):
        cv.line(self.img, self.pts[0], self.pts[1], self.col, self.d)
        self.draw_selection()


class Rectangle(Object):
    """Create a rectangle object."""
    def __init__(self, p0, p1, col, d):
        pts = [p0, p1]
        super(Rectangle, self).__init__(pts, col, d)

    def draw(self):
        cv.rectangle(self.img, self.pts[0], self.pts[1], self.col, self.d)
        self.draw_selection()


class Circle(Object):
    def __init__(self, center, r, col, d):
        self.r = r
        x, y = center
        pts = [[x-r, y-r], [x+r, y+r]]
        super(Circle, self).__init__(pts, col, d)
    
    def draw(self):
        cv.circle(self.img, self.center, self.r, self.col, self.d)
        self.draw_selection()


class Ellipse(Object):
    def __init__(self, center, axes, col, d, a0=0, a1=0, a2=360):
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.center = center
        self.axes = axes
        x, y = center
        a, b = axes
        pts = [(x-a, y-b), (x+a, y+b)]
        super(Ellipse, self).__init__(pts, col, d)

    def draw(self):
        cv.ellipse(self.img, self.center,  self.axes, self.a0, self.a1, self.a2, self.col, self.d)
        self.draw_selection()


class Polygon(Object):
    def __init__(self, pts, col, d):
        super(Polygon, self).__init__(pts, col, d)

    def draw(self):
        cv.polylines(self.img, [self.pts], True, self.col, self.d)
        self.draw_selection()


class Text(Object):
    def __init__(self, text, p0, col, scale=1, **kwargs):
        self.text = text
        self.scale = scale
        self.font = cv.FONT_HERSHEY_SIMPLEX
        ((w, h), b) = cv.getTextSize(text, self.font, scale, 1)
        x, y = p0
        p1 = x + w, y - h
        pts = [p0, p1]
        super(Text, self).__init__(pts, col, self.scale)

    def draw(self):
        cv.putText(self.img, self.text, self.pts[0], self.font, self.scale, self.col, 2, cv.LINE_AA)
        self.draw_selection()

    def set_text(self, text):
        self.text = text
        ((w, h), b) = cv.getTextSize(self.text, self.font, self.scale, self.d)
        x, y = self.pts[0]
        self.pts[1] = x + w, y - h
        self.set_bbox()


class App:
    wins = []
    def __init__(self):
        self.shortcuts = {'i':'self.inspect()'}
        Window()

    def run(self):
        """Run the main event loop."""
        k = ''
        while k != 'q':
            k = chr(cv.waitKey(0))

            # Send key event to active window
            App.win.key(k)

            if k in self.shortcuts.keys():
                cmd = self.shortcuts[k]
                try:
                    exec(cmd)
                except:
                    print('Shortcut error:', sys.exc_info()[0], cmd)
            
        cv.destroyAllWindows()

    def inspect(self):
        print('---inspect---', )
        print('App.wins:', App.wins)
        print('App.win:', App.win)

        for obj in App.win.objects:
            print(obj)

if __name__ == '__main__':
    App().run()