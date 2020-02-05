# Trackbar to go through 1 axis
import cv2 as cv
import numpy as np

img = np.zeros((256, 256, 3), dtype=np.uint8)




cv.imshow('window', img)
cv.addTrackbar('window', 'value', 100, 255)

cv.waitKey(0)
cv.destroyAllWindows()