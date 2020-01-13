import cv2 as cv
import numpy as np
import tkinter as tk
from tkinter import filedialog, colorchooser
import os

root = tk.Tk()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

CYAN = (255, 255, 0)
MAGENTA = (255, 0, 255)
YELLOW = (0, 255, 255)


class Window:
    """Create a window with an image."""
    objs = []
    obj = None

    def __init__(self, win, img):
        self.win = win
        self.img = img
        cv.imshow(win, img)
        cv.setMouseCallback(self.win, self.mouse)

    def mouse(self, event, x, y, flags, params):
        print(event, x, y, flags, params)

class App:
    wins = []
    win = None

    def __init__(self):
        img = cv.imread('../intro/messi.jpg')
        Window('image', img)
        
    def run(self):
        """Run the main event loop."""
        k=0
        while k != ord('q'):
            k = cv.waitKey(0)
            print(k, chr(k))
            if chr(k) == 'o':
                self.load_img()
        
        cv.destroyAllWindows()
        tk.quit()

    def load_img(self):
        print('load image')
        file = tk.filedialog.askopenfilename(title='Please select an image')
        print(file)
        img = cv.imread(file)
        Window('window2', img)
        print(file)


if __name__ == '__main__':
    App().run()