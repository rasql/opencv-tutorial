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
        self.obj = None
        self.obj_id = 0
        self.obj_visible = True
        cv.imshow(win, img)
        self.overlay = 'Keys: '
        self.shortcuts = {  'o':'self.show_object()',
                            'd':'self.objects.pop(self.obj_id)', 
                            'v':self.toggle_visible,
                            '\b':self.delete_selected,
        }
        cv.setMouseCallback(win, self.mouse)

    def draw(self):
        """Reset the image and add graphics objects."""
        self.img[:] = self.img0[:]  

        for obj in self.objects:
            if obj.visible:
                obj.draw()

        cv.imshow(self.win, self.img)
    
    def key(self, k):
        """Handle key press event by selected object or as shortcut."""
        if self.obj != None:
            self.obj.key(k)
        else:
            self.do_shortcut(k)
        self.draw()

    def mouse(self, event, x, y, flags, param):
        """Mouse callback."""
        
        if event == cv.EVENT_LBUTTONDOWN:
            # draw_selection objects under mouse click
            self.select_obj_at(event, x, y, flags, param)

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
        self.obj_id %= n
        self.objects[self.obj_id].selected = False
        self.obj_id += 1
        self.obj_id %= n
        self.objects[self.obj_id].selected = True
        text = str(self.objects[self.obj_id])
        cv.displayOverlay(self.win, text, 1000)
        cv.imshow(self.win, self.img)

    def toggle_visible(self):
        """Toggle visibility of all objects."""
        self.obj_visible = not self.obj_visible
        for obj in self.objects:
            obj.visible = self.obj_visible

    def delete_selected(self):
        """Delete selected objects."""
        for obj in self.objects:
            if obj.selected:
                self.objects.remove(obj)

    def do_shortcut(self, k):
        """Execute key-cmd shortcut as cmd() or exec(cmd)."""
        if k in self.shortcuts.keys():
            cmd = self.shortcuts[k]
            if isinstance(cmd, str):
                try:
                    exec(cmd)
                except:
                    print('Shortcut error:', sys.exc_info()[0], cmd)
            else:
                cmd()

    def select_obj_at(self, event, x, y, flags, param):
        """Select objects at (x, y)."""
        self.obj = None
        for obj in self.objects:
            obj.selected = False
            if obj.is_inside(x, y):
                obj.selected = True
                obj.mouse(event, x, y, flags, param)
                self.obj = obj


class Object():
    """General-purpose object."""
    # options = dict(pos=(20, 20), size=(100, 40), dx=10)
    pos=(20, 20)
    size=(100, 40)
    dx=10
 
    def __init__(self, pos=None, size=None, **options):
        App.win.objects.append(self)
        self.img = App.win.img
        
        if pos == None:
            pos = Object.pos[:]
        else:
            Object.pos = list(pos)
        self.pos = pos[:]
        
        if size == None:
            size = Object.size[:]
        else:
            Object.size = list(size)
        self.size = size[:]

        Object.pos[1] += size[1] + Object.dx

        self.text = ''
        self.selected = False
        self.visible = True
        self.cmd = 'print(self)'

    def __str__(self):
        obj = self.__class__.__name__
        return '{} at ({}, {}) of size ({}, {})'.format(obj, *self.pos, *self.size)

    def draw(self):
        d = self.options
        cv.rectangle(self.img, (*self.pos, *self.size), d['color'], d['thickness'])
        self.draw_selection()
        
    def draw_selection(self):
        """Draw a bounding box around the object if it is selected."""
        if self.selected:
            cv.rectangle(self.img, (*self.pos, *self.size), BLUE, 1)

    def mouse(self, event, x, y, flags, param):
        """Execute cmd() or eval(cmd)."""
        if isinstance(self.cmd, str):
            try:
                exec(self.cmd)
            except:
                print('Shortcut error:', sys.exc_info()[0], self.cmd)
        else:
            self.cmd()

    def key(self, k):
        """Add key charactor to text field."""
        if k == '\b':
            self.text = self.text[:-1]
        elif k == '\r':
            self.obj = None
            self.selected = False
        elif k == '\0':
            pass
        else:
            self.text += k
        self.set_size_to_text()

    def set_size_to_text(self):
        """Set bounding box to text size."""
        # (w, h), b = cv.getTextSize(self.text, self.font, self.scale, 1)
        # self.size = w, h

    def is_inside(self, x, y):
        """Check if point (x, y) is inside the object."""
        x0, y0 = self.pos
        w, h = self.size
        return x0 <= x <= x0+w and y0 <= y <= y0+h

    def set_pos_size(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
        x0, y0 = p0
        x1, y1 = p1
        self.pos = min(x0, x1), min(y0, y1)
        self.size = abs(x1-x0), abs(y1-y0)


class Arrow(Object):
    """Create an arrowed line."""
    options = dict(color=CYAN)

    def __init__(self, p0, p1, **options):
        self.set_pos_size(p0, p1)
        super().__init__(self.pos, self.size)
        Arrow.options.update(options)
        self.options = Arrow.options.copy()

    def draw(self):
        cv.arrowedLine(self.img, self.p0, self.p1, **self.options)
        self.draw_selection()


class Line(Object):
    """Create a line object."""
    options = dict(color=RED)

    def __init__(self, p0, p1, **options):
        self.set_pos_size(p0, p1)
        super().__init__(self.pos, self.size)
        Line.options.update(options)
        self.options = Line.options.copy()

    def draw(self):
        cv.line(self.img, self.p0, self.p1, **self.options)
        self.draw_selection()


class Marker(Object):
    """Create a marker object."""
    options = dict(color=GREEN)

    def __init__(self, p0, **options):
        self.set_pos_size(p0, p0)
        super().__init__(self.pos, self.size)
        Marker.options.update(options)
        self.options = Marker.options.copy()

    def draw(self):
        cv.drawMarker(self.img, self.p0, **self.options)
        self.draw_selection()


class Rectangle(Object):
    """Create a rectangle object."""
    options = dict(color=BLUE)

    def __init__(self, p0, p1, **options):
        self.set_pos_size(p0, p1)
        super().__init__(self.pos, self.size)
        Rectangle.options.update(options)
        self.options = Rectangle.options.copy()

    def draw(self):
        cv.rectangle(self.img, (*self.pos, *self.size), **self.options)
        self.draw_selection()


class Circle(Object):
    """Create a circle object."""
    options = dict(color=MAGENTA)

    def __init__(self, center, r, **options):
        self.r = r
        self.center = center
        x, y = center
        self.pos = x-r, y-r
        self.size = 2*r, 2*r
        super().__init__(self.pos, self.size)
        Circle.options.update(options)
        self.options = Circle.options.copy()
    
    def draw(self):
        cv.circle(self.img, self.center, self.r, **self.options)
        self.draw_selection()


class Ellipse(Object):
    """Create an ellipse object."""
    options = dict(angle=0, startAngle=0, endAngle=360, color=GREEN)

    def __init__(self, center, axes, **options):

        self.center = center
        self.axes = axes
        x, y = center
        a, b = axes
        self.pos = x-a, y-b
        self.size = 2*a, 2*b
        super().__init__(self.pos, self.size)
        
        Ellipse.options.update(options)
        self.options = Ellipse.options.copy()

    def draw(self):
        cv.ellipse(self.img, self.center,  self.axes, **self.options)
        self.draw_selection()


class Polygon(Object):
    """Createa a polygon object."""
    options = dict(color=WHITE, isClosed=False)

    def __init__(self, pts, **options):
        self.pts = pts

        self.set_pos_size(pts) 
        super().__init__(self.pos, self.size)
        Polygon.options.update(options)
        self.options = Polygon.options.copy()

    def draw(self):
        print(self.pts)
        cv.polylines(self.img, [self.pts], **self.options)
        self.draw_selection()

    def set_pos_size(self, pts):
        xmin, ymin = xmax, ymax = pts[0]
        for (x, y) in pts[1:]:
            if x < xmin:
                xmin = x
            if x > xmax:
                xmax = x
            if y < ymin:
                ymin = y
            if y > ymax:
                ymax = y
        self.pos = xmin, ymin
        self.size = xmax-xmin, ymax-ymin
        

class Text(Object):
    options = dict( fontFace=cv.FONT_HERSHEY_SIMPLEX,
                    fontScale=1, thickness=1, color=RED)

    def __init__(self, text, p0, **options):
        self.text = text
        d=Text.options
        (w, h), b = cv.getTextSize(text, d['fontFace'], d['fontScale'], d['thickness'])
        x, y = p0
        p1 = x + w, y + h
        super().__init__(p0, (w, h))
        self.text = text
        Text.options.update(options)
        self.options = Text.options.copy()

    def draw(self):
        cv.putText(self.img, self.text, self.pos, **self.options)
        self.draw_selection()

    def set_text(self, text):
        self.text = text
        ((w, h), b) = cv.getTextSize(self.text, self.font, self.scale, self.d)
        x, y = self.pts[0]
        self.pts[1] = x + w, y - h
        self.set_bbox()

# class Vec2:
#     def __def__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Vec2(self.x + other.x, self.y, other.y)


class Button(Object):
    bg = YELLOW
    fg = RED
    size = [160, 50]
    font = cv.FONT_HERSHEY_SIMPLEX

    def __init__(self, label='Button', cmd='', pos=None, size=None):
        self.text = label
        self.font = Button.font
        self.scale = 1
        self.fg = Button.fg
        self.bg = Button.bg

        if pos == None:
            pos = App.pos[:]
        else:
            App.pos = list(pos)

        if size == None:
            size = Button.size
        else:
            Button.size = list(size)
        
        App.pos[1] += Button.size[1] + Object.dy
        
        x, y = pos
        w, h = size
        p1 = x+w, y+h

        super().__init__((pos, p1), Button.fg, 1)
        self.cmd = cmd

    def draw(self):
        x0, y0, x1, y1 = self.bbox
        cv.rectangle(self.img, (x0, y0),(x1, y1), self.bg, -1)
        cv.putText(self.img, self.text, (x0+5, y1-5), self.font, self.scale, self.fg, 2, cv.LINE_AA)
        self.draw_selection()

class Combobox(Object):
    def __init__(self, label, values, cmd, pos=None):
        # super().__init__
        pass

class Listbox(Object):
    def __init__(self, items, cmd, pos=None):
        # super().__init__():
        pass

class App:
    wins = []
    pos = [20, 20]
    # pos = np.array([20, 20])  # int64
    
    def __init__(self):
        self.shortcuts = {'i':'self.inspect()'}
        Window()

    def run(self):
        """Run the main event loop."""
        while True:
            key = cv.waitKey(0)
            k = chr(key)

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