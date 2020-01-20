# Blurring
import cv2 as cv

def trackbar(x):
    x = cv.
    n = 2*x + 1
    blurred = cv.blur(img, (1, n))
    cv.imshow('window', blurred)
    cv.displayOverlay('window', f'blur = ({n}, {n})')

img = cv.imread('lego.png')
cv.imshow('window', img)
cv.createTrackbar('blur x', 'window', 0, 6, trackbar)
cv.createTrackbar('blur y', 'window', 0, 6, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()