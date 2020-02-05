# adaptive thresholding
import cv2 as cv
import numpy as np

print(cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY)

def trackbar(x):
    """Trackbar callback function."""
    text = f'threshold={x}'
    cv.displayOverlay('window', text, 1000)
    
    ret, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
    img2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    # img2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    cv.imshow('window', np.hstack([img, img1, img2]))

img = cv.imread('eye.jpg')
cv.imshow('window', img)
cv.createTrackbar('threshold', 'window', 100, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()