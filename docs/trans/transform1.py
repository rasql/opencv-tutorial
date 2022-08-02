"""Translation of image using trackbar"""
import cv2 as cv
import numpy as np


def trackbar(x):
    M = np.float32([[1, 0, x], [0, 1, x]])
    shifted = cv.warpAffine(img, M, (w, h))
    cv.imshow('window', shifted)

img = cv.imread('fish.jpg')
h, w = img.shape[:2]

cv.imshow('window', img)
cv.createTrackbar('x', 'window', 0, 180, trackbar)


cv.waitKey(0)
cv.destroyAllWindows()
