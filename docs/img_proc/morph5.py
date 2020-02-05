# morphological gradiant: difference between diation and erosion
import cv2 as cv
import numpy as np

def trackbar(x):
    n = 2*x + 1
    kernel = np.ones((n, n), np.uint8)

    img1 = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
    cv.imshow('window', np.hstack([img, img1]))

    text = f'morphological gradiant, kernel={n}x{n}'
    cv.displayOverlay('window', text)

img = cv.imread('j.png')
trackbar(2)
cv.createTrackbar('kernel', 'window', 2, 5, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()