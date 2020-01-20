"""Numpy indexing."""
import cv2 as cv
import numpy as np

img = cv.imread('lego.png')
blue = img.copy()
green = img.copy()
red = img.copy()

blue[:, :, 1:] = 0
green[:, :, 0] = 0
green[:, :, 2] = 0
red[:, :, :2] = 0

img2 = np.hstack([blue, green, red])

cv.imshow('window', img2)
cv.waitKey(0)
cv.destroyAllWindows()