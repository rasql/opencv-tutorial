"""translate an image with a mouse click."""
import cv2 as cv
import numpy as np

def mouse(event, x, y, flags, param):
    if flags == 1:
        M = np.float32([[1, 0, x], [0, 1, y]])
        shifted = cv.warpAffine(img, M, (w, h))
        cv.imshow('window', shifted)

img = cv.imread('fish.jpg')
h, w = img.shape[:2]
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()