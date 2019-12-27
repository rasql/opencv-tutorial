import cv2 as cv
import numpy as np
import os
import re
import sys
import math
import random

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
    """Create a basic node for a tree structure."""
    id = 0
    sep = '/'
    nodes = []
    path = []
    
    def __init__(self, parent=0, children=[]):
        """Create a node.
        parent = None (root)
        parent = Node()
        parent = 1 (increase level, node is child of last)
        parent = 0 (same level, node is sibling of last)
        parent = -1 (level decrease, node is oncle to last)
        """

        if Node.id == 0:
            self.parent = None
            Node.path = [self]
        elif isinstance(parent, int):
            if parent == 1:
                self.parent = Node.path[-1]
            else:
                self.parent = Node.path[-2+parent]
                Node.path = Node.path[:-1+parent]
            Node.path.append(self)
        else:
            self.parent = parent
            Node.path = parent.get_path()

        self.children = []
        
        if self.parent != None:
            self.parent.children.append(self)

        self.id = Node.id
        Node.id += 1
        Node.nodes.append(self)
        print(self, self.parent)
        return self

    def __str__(self):
        return 'node{}'.format(self.id)
        
    def print_tree(self, level=0):
        """Print a tree view."""
        print('    ' * level + str(self))
        level += 1
        for child in self.children:
            child.print_tree(level)

    def sibling(self, forward=True, wrap=True):
        d = 1 if forward else -1
        n = len(self.parent.children)
        i = self.parent.children.index(self)
        if wrap:
            i = (i+d) % n
        else:
            i = max(0, min(i+d, n-1))
        return self.parent.children[i]

    def is_root(self):
        return self.parent == None

    def walk(self, i=0):
        print(self)
        if i < len(self.children):
            walk(self.children[i], 0)
        else:
            walk(self)
              # TO 
    def get_breadth_first_nodes(self):
        """Get breath-first nodes."""
        nodes = []
        stack = [self]
        while stack:
            n0 = stack.pop(0)
            nodes.append(n0)
            stack.extend(n0.children)
        return nodes

    def get_depth_first_nodes(self):
        """Get depth-first nodes."""
        nodes = []
        stack = [self]
        while stack:
            n0 = stack.pop(0)
            nodes.append(n0)
            stack = n0.children + stack
        return nodes

    def get_path(node):
        """Return path list including node."""
        path = []
        while node != None:
            path.insert(0, node)
            node = node.parent
        return path

class Shape(Node):
    """Create a shape node to add graphic objects to a window.
    * parent
    * children
    * id

    * win
    * img

    * pos
    * size
    * dir
    * gap
    """

    def __init__(self, **options):
        if App.win == None:
            Window()
        super().__init__(App.win)  # Create child of current window

        self.win = App.win
        self.img = App.win.img

        level = options.get('level', 0)
        self.cmd = options.get('cmd', None)

        # set Shape class options
        self.set_node_options(options)
        self.set_class_options(options)

        # select insertion (parent) node
        if level == 0:
            self.parent = self.win.current_parent
        elif level == 1:
            self.parent = self.win.current_parent.children[-1]
            self.win.current_parent = self.parent
        else:
            for i in range(-level):
                self.goto_parent()

        self.selected = False
        self.frame = True

        # create instance attributes
        self.pos = None
        self.size = None
        self.gap = None
        self.dir = None
        self.id = None

        # update instance attributes from node options
        self.__dict__.update(Shape.options)
        Shape.options['id'] += 1

        if 'pos' not in options:
            self.set_pos()

        self.win.draw()

    # def __str__(self):
    #     obj = self.__class__.__name__
    #     return '{} at {}'.format(obj, self.pos)

    def set_node_options(self, options):
        """Update Shape class options."""
        for k, v in options.items():
            if k in Shape.options:
                if isinstance(v, tuple):
                    v = np.array(v)
                Shape.options[k] = v

    def set_class_options(self, options):
        """Update class options and set instance options."""
        for k, v in options.items():
            if k in self.__class__.options:
                self.__class__.options[k] = v
            elif k in Shape.options:
                pass
            else:
                cname = self.__class__.__name__
                options = ', '.join(self.__class__.options.keys())
                spec = "'{}' is not a valid option for '{}'\n   Valid options are: {}"
                msg = spec.format(k, cname, options)
                raise TypeError(msg)
        self.options = self.__class__.options.copy()

    def draw(self, pos=np.array((0, 0))):

        x, y = pos + self.pos
        w, h = self.size
        if self.win.frame and self.frame:
            cv.rectangle(self.img, (x, y, w, h), RED, 1)
            label = 'n{}'.format(self.id)
            cv.putText(self.img, label, (x, y-1), 0, 0.4, RED, 1)
        if self.selected:
            cv.rectangle(self.img, (x-2, y-2, w+4, h+4), GREEN, 1)

        for child in self.children:
            child.draw(pos+self.pos)

    def is_inside(self, pos):
        """Check if the point (x, y) is inside the object."""
        pos = np.array(pos)
        return all(self.pos < pos) and all(pos < self.pos+self.size)

    def mouse(self, event, pos, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            if callable(self.cmd):
                self.cmd()
            for child in self.children:
                child.selected = False
                if child.is_inside(pos-self.pos):
                    child.selected = True
                    child.mouse(event, pos, flags, param)

    def key(self, k):
        print('key', k, 'in', self)

    def enclose_children(self):
        p = np.array((0, 0))
        for node in self.children:
            p = np.maximum(p, node.pos+node.size)
        self.size = p + self.gap

    def goto_parent(self):
        """Enclose children of current and go to parent."""
        self.win.current_parent.enclose_children()
        self.parent = self.win.current_parent.parent
        self.win.current_parent = self.parent

    def set_pos_size(self, pts):
        """Set position and size from the list of points."""
        min = np.amin(pts, axis=0)
        max = np.amax(pts, axis=0)

        self.pts = pts-min
        self.pos = min
        self.size = max-min

    def set_pos(self):
        """Set the new position based on preceding sibling."""
        if len(self.parent.children) == 1:  # is first child
            if len(self.win.nodes) != 1:
                self.pos = self.gap
        else:
            prev = self.parent.children[-2]  # preceding sibling
            self.pos = prev.pos + self.dir * (prev.size + self.gap)


class Node2(Shape):
    """Shape based on multiple points."""

    def __init__(self, *pts, **options):
        # super().__init__(**options)

        n = len(pts)
        if n == 0:
            pts = [self.pos, self.pos+self.size]

        self.pts = np.array(pts)
        self.set_pos_size(self.pts)

        if len(pts) == 1:
            self.pos -= np.array((10, 10))
            self.pts += np.array((10, 10))
            self.size = np.array((20, 20))

        super().__init__(**options)
        # print(self.pts, *self.pts[:2])

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        self.pts_ = pos + self.pos + self.pts  # abs position
        if self.win.frame and self.frame:
            for p in self.pts_:
                pos = tuple(p)
                print(pos)

                # cv.drawMarker(self.img, pos, color=RED, markerSize=10,
                #               markerType=cv.MARKER_SQUARE)
                cv.drawMarker(self.img, pos, RED)


class Marker(Shape):
    options = dict(color=GREEN,
                   markerType=cv.MARKER_CROSS,
                   markerSize=20,
                   thickness=1,
                   line_type=cv.LINE_8)

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
    options = dict(color=GREEN,
                   thickness=1,
                   lineType=cv.LINE_8,
                   shift=0)

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        p = pos + self.pos + self.pts
        cv.line(self.img, tuple(p[0]), tuple(p[1]), **self.options)


class Arrow(Node2):
    options = dict(color=RED,
                   thickness=1,
                   line_type=cv.LINE_8,
                   shift=0,
                   tipLength=0.1)

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        cv.arrowedLine(self.img, tuple(self.pts_[0]), tuple(
            self.pts_[1]), **self.options)


class Rectangle(Node2):
    options = dict(color=GREEN,
                   thickness=1,
                   lineType=cv.LINE_8,
                   shift=0)

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        cv.rectangle(self.img, tuple(self.pts_[0]), tuple(
            self.pts_[1]), **self.options)


class Circle(Shape):
    def __init__(self):
        super().__init__()


class Ellipse(Node2):
    options = dict(angle=0,
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


class Polygon(Node2):
    options = dict(isClosed=True,
                   color=MAGENTA,
                   thickness=1,
                   lineType=cv.LINE_8,
                   shift=0)

    def draw(self, pos=np.array((0, 0))):
        super().draw(pos)
        cv.polylines(self.img, [self.pts_], **self.options)


class Text(Shape):
    options = dict(fontFace=cv.FONT_HERSHEY_SIMPLEX,
                   fontScale=1,
                   color=GREEN,
                   thickness=2,
                   lineType=cv.LINE_8,
                   bottomLeftOrigin=False)

    def __init__(self, text='Text', **options):
        self.text = text
        super().__init__(**options)
        self.set_class_options(options)
        # self.text = text
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


class Button(Shape):
    def __init__(self, text='Button', cmd=None):
        super().__init__()
        Text(text, level=1, cmd=cmd)
        self.goto_parent()


class Listbox(Shape):
    options = dict(fontScale=0.5, thickness=1)

    def __init__(self, items='Item1;Item2;Item3', **options):
        if isinstance(items, str):
            items = items.split(';')
        self.items = items

        options.update(dict(gap=np.array((0, 0))))
        super().__init__(**options)

        Text(self.items[0], level=1, thickness=1, fontScale=0.5, cmd=self.cb)
        for item in self.items[1:]:
            Text(item)
        self.goto_parent()

    def cb(self):
        print('Listbox callback', self, self.id)


class Window(Node):
    """Create a window for the app."""
    node_options = dict(pos=np.array((20, 20)),
                        size=np.array((100, 20)),
                        gap=np.array((10, 10)),
                        dir=np.array((0, 1)),
                        id=0,
                        level=0,
                        cmd=None)

    def __init__(self, win=None, img=None):
        super().__init__(App.root)  # Create child of app
        App.win = self  # Make it active window

        Shape.options = Window.node_options.copy()
        self.children = []  # children
        self.current_parent = self  # inital parent
        self.nodes = []  # list of all nodes
        self.node = None  # currently selected node
        self.pos = np.array((0, 0))

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
        self.frame = True
        self.visible = True

        self.shortcuts = {'\t': self.select_next_node,
                          chr(27): self.unselect_node,
                          chr(0): self.toggle_shift,
                          'f': self.toggle_frame,
                          'v': self.toggle_visible}

        cv.imshow(win, img)
        cv.setMouseCallback(win, self.mouse)

    def __str__(self):
        return 'Window(n{})'.format(self.id)

    def mouse(self, event, x, y, flags, param):
        pos = np.array((x, y))

        text = 'mouse event {} at {} with flags {}'.format(
            event, pos, flags)
        cv.displayStatusBar(self.win, text, 1000)

        if event == cv.EVENT_LBUTTONDOWN:
            App.win = self

            if flags & cv.EVENT_FLAG_SHIFTKEY:
                self.new(pos=(x, y))
            else:
                self.select_node(pos)

        if event == cv.EVENT_MOUSEMOVE:
            if flags == cv.EVENT_FLAG_ALTKEY and self.node != None:
                self.node.pos = pos

        if self.node != None:
            self.node.mouse(event, pos, flags, param)

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

        if self.visible:
            for child in self.children:
                child.draw()

        cv.imshow(self.win, self.img)

    def select_node(self, pos):
        """Select oblect at position (x, y)."""
        self.node = None
        for child in self.children:
            child.selected = False
            if child.is_inside(pos):
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

        n = self.node
        msg = 'pos=({}, {}), size=({}, {})'.format(*n.pos, *n.size)
        self.status(msg)

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

    def toggle_frame(self):
        self.frame = not self.frame

    def toggle_visible(self):
        self.visible = not self.visible

    def status(self, msg):
        cv.displayStatusBar(self.win, msg, 1000)


class App(Node):
    """Create the app class."""
    wins = []
    win = None
    win_id = 0
    options = dict(win_color=BLACK, obj_color=YELLOW, sel_color=BLUE)

    def __init__(self):
        """Create the app singleton."""
        App.root = super().__init__()  # Create the root node
        print(App.root)
        
        self.shortcuts = {'h': help,
                          'i': self.inspect,
                          'w': Window,
                          'n': Shape,
                          't': Text,
                          'b': Button,
                          'l': Listbox,
                          'e': self.edit_mode}

        self.classes = [Marker, Line, Arrow, Rectangle, Shape, Text]
        self.class_id = 0
        self.new = Marker

    def run(self):
        """Run the app event loop."""
        while True:
            key = cv.waitKey(0)
            if key >= 0:
                k = chr(key)
                if not App.win.key(k):
                    self.key(k)

    def key(self, k):
        """Handle an app key press."""
        if k in self.shortcuts:
            self.shortcuts[k]()

    def inspect(self):
        """Print app info to the console."""
        print('--- INSPECT ---')
        print('App.wins', App.wins)
        # print('App.win', App.win)
        if App.win.node != None:
            d = vars(App.win.node)
            d.pop('img')
            print(d)

    def edit_mode(self):
        self.class_id += 1
        self.class_id %= len(self.classes)
        App.win.new = self.classes[self.class_id]
        print(App.win.new)
        text = 'Insert new {}'.format(App.win.new.__name__)
        cv.displayStatusBar(App.win.win, text, 1000)


if __name__ == '__main__':
    app = App()
    Window()   
    app.run()
