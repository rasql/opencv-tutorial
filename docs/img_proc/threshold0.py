# Add a trackbar
import cv2 as cv
import numpy as np

img = np.fromfunction(lambda i, j: j, (50, 256), dtype='uint8')

modes = (cv.THRESH_BINARY, 
        cv.THRESH_BINARY_INV,
        cv.THRESH_TRUNC,
        cv.THRESH_TOZERO,
        cv.THRESH_TOZERO_INV)

def trackbar(x):
    """Trackbar callback function."""
    text = f'threshold={x}'
    cv.displayOverlay('window', text, 1000)
    
    ret, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
    ret, img2 = cv.threshold(img, x, 255, cv.THRESH_BINARY_INV)
    ret, img3 = cv.threshold(img, x, 255, cv.THRESH_TRUNC)
    ret, img4 = cv.threshold(img, x, 255, cv.THRESH_TOZERO)
    ret, img5 = cv.threshold(img, x, 255, cv.THRESH_TOZERO_INV)
    
    cv.imshow('window', np.vstack([img, img1, img2, img3, img4, img5]))

cv.imshow('window', img)
trackbar(100)
cv.createTrackbar('threshold', 'window', 100, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()