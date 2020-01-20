# Blurring
import cv2 as cv

def trackbar(x):
    x = cv.getTrackbarPos('blur x','window')
    y = cv.getTrackbarPos('blur x','window')
    blurred = cv.blur(img, (x, y))
    cv.imshow('window', blurred)
    cv.displayOverlay('window', f'blur = ({x}, {y})')

img = cv.imread('lego.png')
cv.imshow('window', img)
cv.createTrackbar('blur x', 'window', 0, 4, trackbar)
cv.createTrackbar('blur y', 'window', 0, 4, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()