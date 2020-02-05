# threshold to zero
import cv2 as cv
import numpy as np

def trackbar(x):
    """Trackbar callback function."""
    text = f'threshold={x}, mode=TOZERO, TOZERO_INV'
    cv.displayOverlay('window', text, 1000)
    
    ret, img1 = cv.threshold(img, x, 255, cv.THRESH_TOZERO)
    ret, img2 = cv.threshold(img, x, 255, cv.THRESH_TOZERO_INV)
    cv.imshow('window', np.hstack([img, img1, img2]))

img = cv.imread('eye.jpg')
cv.imshow('window', img)
cv.createTrackbar('threshold', 'window', 100, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()