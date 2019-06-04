"""Display an image in a Tk label."""
from tklib import *
# from cvlib import *
import cv2 as cv
from PIL import Image, ImageTk

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        Label('Change Colorspace of OpenCV image', font='Arial 24')

        img0 = cv.imread('messi.jpg', cv.IMREAD_COLOR)

        img1 = cv.cvtColor(img0, cv.COLOR_BGR2RGB)
        img1 = Image.fromarray(img1)
        img1 = ImageTk.PhotoImage(img1)
        self.lb = Label(image=img1)
        self.lb.img = img1

        # hsv = cv.cvtColor(img0, cv.COLOR_BGR2HSV)
        hsv = cv.cvtColor(img0, cv.COLOR_BGR2GRAY)
        hsv1 = Image.fromarray(hsv)
        hsv1 = ImageTk.PhotoImage(hsv1)
        self.lb2 = Label(image=hsv1)
        self.lb2.grid(column=1, row=1)
        self.lb2.img = hsv1
       
if __name__ == '__main__':
    Demo().run()