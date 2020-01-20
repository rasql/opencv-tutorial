"""Splitting into 3 channels"""
import cv2 as cv
import numpy as np

img = cv.imread('lego.png')
b, g, r = cv.split(img)
img2 = np.hstack([b, g, r])

cv.imshow('window', img2)
cv.waitKey(0)
cv.destroyAllWindows()