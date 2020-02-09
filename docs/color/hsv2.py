# Trackbar to go through 1 axis
import cv2 as cv
import numpy as np

def trackbar(x):
    img[:, :, 2] = x
    rgb = cv.cvtColor(img, cv.COLOR_HSV2BGR)
    cv.imshow('window', rgb)

img = np.zeros((180, 256, 3), dtype=np.uint8)

for i in range(180):
    img[i, :, 0] = i

for i in range(256):
    img[:, i, 1] = i

cv.imshow('window', img)
cv.createTrackbar('saturation', 'window', 0, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()