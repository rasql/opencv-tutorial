import cv2 as cv
import numpy as np

BLACK = (0, 0, 0)
RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 255)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

def help():
    print('--- HELP ---')


class Object:
    """Add an object to the current window."""
    def __init__(self, **options):
        App.win.objs.append(self)
        App.win.obj = self
        self.img = App.win.img

        d = App.win.obj_options
        d.update(options)

        self.id = d['id']
        self.pos = x, y = d['pos']
        self.size = w, h = d['size']
        self.text = ''
        self.selected = False

        d['id'] += 1
        d['pos'] = x, y + h + 10

        App.win.draw()

    def __str__(self):
        return 'Object {} at ({}, {})'.format(self.id, *self.pos)

    def draw(self):
        x, y = self.pos
        w, h = self.size
        cv.rectangle(self.img, (x, y, w, h), App.options['obj_color'], 1)
        if self.selected:
            cv.rectangle(self.img, (x-2, y-2, w+2, h+2), App.options['sel_color'], 2)

    def is_inside(self, x, y):
        """Check if the point (x, y) is inside the object."""
        x0, y0 = self.pos
        w, h = self.size
        return x0 <= x <= x0+w and y0 <= y <= y0+h

    def mouse(self, event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            # print(self)
            pass

    def key(self, k):
        if k == '\b':
            self.text = self.text[:-1]
        elif k == '\r':
            print('Enter')
        elif ord(k) < 128:
            if App.win.capitals:
                k = k.upper()
            self.text += k
        (w, h), b = self.get_size()
        self.size = w, h+b

    def filter_options(self, keys):
        self.options = {k: v for k, v in self.options if k in keys}


class Text(Object):
    """Add a text object to the current window."""
    options = dict( fontFace=cv.FONT_HERSHEY_SIMPLEX,
                    fontScale=1,
                    color=BLUE,
                    thickness=1,
                    lineType=cv.LINE_8,)

    def __init__(self, text='Text', **options):

        for k, v in options.items():
            if k in Text.options:
                Text.options[k] = v

        self.text_options = Text.options.copy()
        super().__init__(**options)
        self.text = text
        (w, h), b = self.get_size()
        self.size = w, h+b

    def draw(self):
        super().draw()
        x, y = self.pos
        (w, h), b = self.get_size()
        cv.putText(self.img, self.text, org=(x, y+h), **self.text_options)

    def get_size(self):
        """Returns the text size and baseline under the forme (w, h), b."""
        d = self.text_options
        return cv.getTextSize(self.text, d['fontFace'], d['fontScale'],d['thickness'])


class Window:
    """Create a window for the app."""
    obj_options = dict(pos=(20, 20), size=(100, 30), id=0)

    def __init__(self, win=None, img=None):
        App.wins.append(self)
        App.win = self

        self.objs = []
        self.obj = None
        self.obj_options = Window.obj_options.copy()

        if img == None:
            img = np.zeros((200, 600, 3), np.uint8)
            img[:,:] = App.options['win_color']

        if win == None:
            win = 'window' + str(App.win_id)
        App.win_id += 1

        self.win = win
        self.img = img
        self.img0 = img.copy()
        self.capitals = False

        self.shortcuts = {  '\t': self.select_next_obj,
                            chr(27): self.unselect_obj,
                            chr(0): self.toggle_case, }

        cv.imshow(win, img)
        cv.setMouseCallback(win, self.mouse)

    def __str__(self):
        return 'Window: ' + self.win

    def mouse(self, event, x, y, flags, param):
        text = 'mouse event {} at ({}, {}) with flags {}'.format(event, x, y, flags)        
        cv.displayStatusBar(self.win, text, 1000)

        if event == cv.EVENT_LBUTTONDOWN:
            App.win = self

            self.obj = None
            for obj in self.objs:
                obj.selected = False
                if obj.is_inside(x, y):
                    obj.selected = True
                    self.obj = obj
                    
        if event == cv.EVENT_MOUSEMOVE:
            if flags == cv.EVENT_FLAG_ALTKEY:
                self.obj.pos = x, y

        if self.obj != None:
            self.obj.mouse(event, x, y, flags, param)
        
        self.draw()

    def key(self, k):
        """Handle key events and send them to the current object."""
        text = 'key {} ({})'.format(k, ord(k))        
        cv.displayStatusBar(self.win, text, 1000)
        
        if k in self.shortcuts:
            self.shortcuts[k]()
            self.draw()
            return True

        elif self.obj != None:
            self.obj.key(k)
            self.draw()
            return True
        
        return False

    def draw(self):
        self.img[:] = self.img0[:]

        for obj in self.objs:
            obj.draw()

        cv.imshow(self.win, self.img)

    def select_next_obj(self):
        """Select the next object, or the first in none is selected."""
        try:
            i = self.objs.index(self.obj)
        except ValueError:
            i = -1
        self.objs[i].selected = False
        i = (i+1) % len(self.objs)
        self.objs[i].selected = True
        self.obj = self.objs[i]
    
    def unselect_obj(self):
        if self.obj != None:
            self.obj.selected = False
            self.obj = None

    def toggle_case(self):
        self.capitals = not self.capitals
        if self.capitals:
            cv.displayStatusBar(self.win, 'UPPER case', 1000)
        else:
            cv.displayStatusBar(self.win, 'LOWER case', 1000)


class App:
    """Create the app class."""
    wins = []
    win = None
    win_id = 0
    options = dict( win_color=BLACK, obj_color=YELLOW, sel_color=BLUE)

    def __init__(self):
        # cv.namedWindow('window0')

        self.shortcuts = {'h': help,
                          'i': self.inspect,
                          'w': Window,
                          'o': Object, 
                          't': Text,}

        Window()
        Text(color=GREEN)
        Text('Hello', thickness=2)
        Text('ABC', fontScale=2)
        Text(pos=(200,20), color=RED)

        Window()
        Object()
        Text()
        Text()

    def run(self):
        while True:
            key = cv.waitKey(0)

            if key >= 0:
                k = chr(key)
                if not App.win.key(k):
                    self.key(k)


    def inspect(self):
        print('--- INSPECT ---')
        print('App.wins', App.wins)
        print('App.win', App.win)

    def key(self, k):
        if k in self.shortcuts:
            self.shortcuts[k]()

if __name__ == '__main__':
    App().run()