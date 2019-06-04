"""Display an image in a Tk label."""
from tklib import *
# from cvlib import *
import cv2 as cv
from PIL import Image, ImageTk

class Demo(App):
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        Label('Display an OpenCV image', font='Arial 24')

        img0 = cv.imread('messi.jpg', cv.IMREAD_COLOR)
        img1 = cv.cvtColor(img0, cv.COLOR_BGR2RGB)

        img2 = Image.fromarray(img1)
        img3 = ImageTk.PhotoImage(img2)
        print(type(img3))

        self.lb = Label(image=img3)
        self.lb.img = img3
       
if __name__ == '__main__':
    Demo().run()