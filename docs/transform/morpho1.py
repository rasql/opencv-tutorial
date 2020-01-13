"""Morphological transformation: erosion."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('draw/letter_j.png', 0)
        Window('original', img)
        print(img)
        print(img.shape)

        kernel = np.ones((5, 5), np.uint8)

        erosion = cv.erode(img, kernel, iterations = 1)
        Window('erosion', erosion)
        
        dilation = cv.dilate(img, kernel, iterations = 1)
        Window('dilation', dilation)

if __name__ == '__main__':
    Demo().run()