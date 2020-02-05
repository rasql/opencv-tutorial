# binary thresholding
import cv2 as cv
import numpy as np

def trackbar(x):    
    ret, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
    ret, img2 = cv.threshold(img, x, 255, cv.THRESH_BINARY_INV)
    cv.imshow('window', np.hstack([img, img1, img2]))

    text = f'threshold={x}, mode=BINARY, BINARY_INV'
    cv.displayOverlay('window', text, 1000)

img = cv.imread('eye.jpg')
trackbar(100)
cv.createTrackbar('threshold', 'window', 100, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()