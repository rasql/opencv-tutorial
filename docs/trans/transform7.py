"""Change the color space."""
import cv2 as cv
import numpy as np

img = cv.imread('fish.jpg')
img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
M = np.ones(img.shape, dtype='uint8') * 40

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
img2 = np.hstack([img, hsv, lab])

cv.imshow('window', img2)
cv.waitKey(0)
cv.destroyAllWindows()