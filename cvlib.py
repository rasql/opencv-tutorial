import cv2 as cv
import numpy as np
import os, re, sys, math, random

BLACK = (0, 0, 0)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 255)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)


def cv_dir(regex):
    """Return a list of OpenCV attributes which match a regex."""
    atts = dir(cv)
    return [s for s in atts if re.match(regex, s)]


def help():
    print('--- HELP ---')


class Node:
    """Create a tree node to add graphic objects to a window."""
    options = dict( pos=np.array((20, 20)),
                    size=np.array((100, 20)),
                    gap=np.array((10, 10)),
                    dir=np.array((0, 1)),)

    def __init__(self, level=0, **options):
        self.win = App.win
        self.img = App.win.img

        # set Node class options
        self.set_node_options(options)

        # select parent node
        if level == -1:
            self.level_up()
        elif level == +1:
            parent = self.win.stack[-1].children[-1]
            Node.options['pos'] = Node.options['gap']
            self.win.stack.append(parent)

        # attach node to parent
        self.parent = self.win.stack[-1]
        self.parent.children.append(self)
        self.children = []
        self.selected = False
        self.frame = True

        # create instance attributes
        self.pos = None
        self.size = None
        self.gap = None
        self.dir = None

        # update instance attributes from node options
        self.__dict__.update(Node.options)

        pos = self.pos + (self.size+self.gap)*self.dir
        Node.options['pos'] = pos
        # cv.imshow(self.win.win, self.img)

    def __str__(self):
        obj = self.__class__.__name__
        return '{} at {}'.format(obj, self.pos)

    def set_node_options(self, options):
        """Update Node class options."""
        for k, v in options.items():
            if k in Node.options:
                if isinstance(v, tuple):
                    v = np.array(v)
                Node.options[k] = v
 
    def set_class_options(self, options):
        """Update class options and set instance options."""
        for k, v in options.items():
            if k in self.__class__.options:
                self.__class__.options[k] = v
        self.options = self.__class__.options.copy()


    def level_up(self):
        """Enclose the current children and move up one level."""
        n = self.win.stack[-1]
        n.enclose_children()

        # update the position
        pos = n.pos + (n.size+n.gap)*n.dir
        self.win.node_options['pos'] = pos
        self.win.stack.pop()

    def draw(self, pos=np.array((0, 0))):

        x, y = pos + self.pos
        w, h = self.size
        if self.frame:
            cv.rectangle(self.img, (x, y, w, h), RED, 1)
        if self.selected:
            cv.rectangle(self.img, (x-2, y-2, w+4, h+4), GREEN, 1)

        for child in self.children:
            child.draw(self.pos)

    def is_inside(self, pos):
        """Check if the point (x, y) is inside the object."""
        pos = np.array(pos)
        return all(self.pos < pos) and all(pos < self.pos+self.size)

    def mouse(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            print('mouse in', self)

    def key(self, k):
        print('key', k, 'in', self)

    def enclose_children(self):
        p = np.array((0, 0))
        for node in self.children:
            p = np.maximum(p, node.pos+node.size)
        self.size = p + self.gap

    def set_pos_size(self, pts):
        """Set position and size from the list of points."""
        min = np.amin(pts, axis=0)
        max = np.amax(pts, axis=0)
        
        self.pts = pts-min
        self.pos = min
        self.size = max-min

class Node2(Node):
    """Node based on two points (p0, p1)."""
    def __init__(self, p0, p1, **options):
        super().__init__(**options)

        self.pts = np.array([p0, p1])
        self.set_pos_size(self.pts)

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        pts = pos + self.pos + self.pts
        self.abs_pts = tuple(map(tuple, pts))


class Marker(Node):
    options = dict( color=GREEN,
                    markerType=cv.MARKER_CROSS,
                    markerSize=20,
                    thickness=1,
                    line_type=8)

    def __init__(self, **options):
        super().__init__(**options)
        self.set_class_options(options)
        
        self.size = np.array((20, 20))
        self.frame = False
        cv.imshow(self.win.win, self.img)

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        x, y = pos + self.pos + (10, 10)
        cv.drawMarker(self.img, (x, y), **self.options)

class Line(Node2):
    options = dict( color=GREEN,
                    thickness=1,
                    lineType=cv.LINE_8,
                    shift=0)

    def __init__(self, p0, p1, **options):
        super().__init__(p0, p1, **options)
        self.set_class_options(options)

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        cv.line(self.img, *self.abs_pts, **self.options)


class Arrow(Node2):
    options = dict( color=RED,
                thickness=1,
                line_type=cv.LINE_8,
                shift=0,
                tipLength=0.1)
                    
    def __init__(self, p0, p1, **options):
        super().__init__(p0, p1, **options)
        self.set_class_options(options)

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        cv.arrowedLine(self.img, *self.abs_pts, **self.options)


class Rectangle(Node2):
    options = dict( color=GREEN,
                    thickness=1,
                    lineType=cv.LINE_8,
                    shift=0)

    def __init__(self, p0, p1, **options):
        super().__init__(p0, p1, **options)
        self.set_class_options(options)

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        cv.rectangle(self.img, *self.abs_pts, **self.options)


class Circle(Node):
    def __init__(self):
        super().__init__()


class Ellipse(Node2):
    options = dict( angle=0,
                    startAngle=0,
                    endAngle=360,
                    color=RED,
                    thickness=1,
                    lineType=cv.LINE_8,
                    shift=0)

    def __init__(self, p0, p1, **options):
        super().__init__(p0, p1, **options)
        self.set_class_options(options)

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        center = pos + self.pos + self.size//2
        axes = self.size//2
        cv.ellipse(self.img, tuple(center), tuple(axes), **self.options)


class Polygon(Node):
    options = dict( isClosed=True,
                    color=MAGENTA,
                    thickness=1,
                    lineType=cv.LINE_8,
                    shift=0)

    def __init__(self, pts, **options):
        super().__init__(**options)
        self.set_class_options(options)
        self.set_pos_size(pts)

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        pts = pos + self.pos + self.pts
        cv.polylines(self.img, [pts], **self.options)


class Text(Node):
    options = dict(fontFace=cv.FONT_HERSHEY_SIMPLEX,
                   fontScale=1,
                   color=GREEN,
                   thickness=2,
                   lineType=cv.LINE_8,)

    def __init__(self, text='TextNode', **options):
        super().__init__(**options)
        self.set_class_options(options)
        self.text = text
        (w, h), b = self.get_size()
        self.size = np.array((w, h+b))

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        (w, h), b = self.get_size()
        x, y = pos + self.pos
        cv.putText(self.img, self.text, (x, y+h), **self.options)

    def get_size(self):
        """Returns the text size and baseline under the forme (w, h), b."""
        d = self.options
        return cv.getTextSize(self.text, d['fontFace'], d['fontScale'], d['thickness'])

    def key(self, k):
        if k == '\b':
            self.text = self.text[:-1]
        elif k == '\r':
            print('Enter')
        elif ord(k) < 128:
            if App.win.shift:
                k = k.upper()
            self.text += k
        (w, h), b = self.get_size()
        self.size = w, h+b


class Button(Node):
    def __init__(self, text='Button', cmd=None):
        super().__init__()
        TextNode(text, level=1)
        self.level_up()


class Listbox(Node):
    def __init__(self, items='Item1;Item2;Item3'):
        self.items = items.split(';')

        super().__init__()
        TextNode(self.items[0], level=1)
        for item in self.items[1:]:
            TextNode(item)
        self.level_up()


class Window:
    """Create a window for the app."""
    node_options = dict(pos=np.array((20, 20)),
                        size=np.array((100, 20)),
                        gap=np.array((10, 10)),
                        dir=np.array((0, 1)),
                        )

    def __init__(self, win=None, img=None):
        App.wins.append(self)
        App.win = self

        self.node_options = Window.node_options.copy()
        self.children = []  # children
        self.stack = [self]  #  parent stack
        self.node = None  # currently selected node

        if img == None:
            img = np.zeros((200, 600, 3), np.uint8)
            img[:, :] = App.options['win_color']

        if win == None:
            win = 'window' + str(App.win_id)
        App.win_id += 1

        self.win = win
        self.img = img
        self.img0 = img.copy()
        self.shift = False

        self.shortcuts = {'\t': self.select_next_node,
                          chr(27): self.unselect_node,
                          chr(0): self.toggle_shift, }

        cv.imshow(win, img)
        cv.setMouseCallback(win, self.mouse)

    def __str__(self):
        return 'Window: ' + self.win

    def mouse(self, event, x, y, flags, param):
        text = 'mouse event {} at ({}, {}) with flags {}'.format(
            event, x, y, flags)
        cv.displayStatusBar(self.win, text, 1000)

        if event == cv.EVENT_LBUTTONDOWN:
            App.win = self
            
            if flags & cv.EVENT_FLAG_SHIFTKEY:
                self.new(pos=(x, y))
            else:
                self.select_node(x, y)

        if event == cv.EVENT_MOUSEMOVE:
            if flags == cv.EVENT_FLAG_ALTKEY and self.node != None:
                self.node.pos = np.array((x, y))

        if self.node != None:
            self.node.mouse(event, x, y, flags, param)

        self.draw()

    def key(self, k):
        """Handle key events and send them to the current object."""
        text = 'key {} ({})'.format(k, ord(k))
        cv.displayStatusBar(self.win, text, 1000)

        if k in self.shortcuts:
            self.shortcuts[k]()
            self.draw()
            return True

        elif self.node != None:
            self.node.key(k)
            self.draw()
            return True

        return False

    def draw(self):
        self.img[:] = self.img0[:]

        for child in self.children:
            child.draw()

        cv.imshow(self.win, self.img)

    def select_node(self, x, y):
        """Select oblect at position (x, y)."""
        self.node = None
        for child in self.children:
            child.selected = False
            if child.is_inside((x, y)):
                child.selected = True
                self.node = child

    def select_next_node(self):
        """Select the next object, or the first in none is selected."""
        try:
            i = self.children.index(self.node)
        except ValueError:
            i = -1
        self.children[i].selected = False
        if self.shift:
            i = (i-1) % len(self.children)
        else:
            i = (i+1) % len(self.children)
        self.children[i].selected = True
        self.node = self.children[i]

    def unselect_node(self):
        if self.node != None:
            self.node.selected = False
            self.node = None

    def toggle_shift(self):
        self.shift = not self.shift
        if self.shift:
            cv.displayStatusBar(self.win, 'SHIFT is ON', 1000)
        else:
            cv.displayStatusBar(self.win, 'SHIFT is OFF', 1000)


class App:
    """Create the app class."""
    wins = []
    win = None
    win_id = 0
    options = dict(win_color=BLACK, obj_color=YELLOW, sel_color=BLUE)

    def __init__(self):
        # cv.namedWindow('window0')
        self.shortcuts = {'h': help,
                          'i': self.inspect,
                          'w': Window,
                          'n': Node,
                          't': Text,
                          'b': Button,
                          'l': Listbox,
                          'e': self.edit_mode }

        self.classes = [Marker, Line, Arrow, Rectangle, Node, Text]
        self.class_id = 0
        self.new = Marker

    def run(self):
        while True:
            key = cv.waitKey(0)
            if key >= 0:
                k = chr(key)
                if not App.win.key(k):
                    self.key(k)

    def key(self, k):
        if k in self.shortcuts:
            self.shortcuts[k]()

    def inspect(self):
        print('--- INSPECT ---')
        print('App.wins', App.wins)
        print('App.win', App.win)

    def edit_mode(self):
        self.class_id += 1
        self.class_id %= len(self.classes)
        App.win.new = self.classes[self.class_id]
        print(App.win.new)
        text = 'Insert new {}'.format(App.win.new.__name__)
        cv.displayStatusBar(App.win.win, text, 1000)

if __name__ == '__main__':
    App().run()
