"""Catch mouse events and write to overlay and statusbar."""
import cv2 as cv

def trackbar(x):
    """Trackbar callback function."""
    text = 'Trackbar: {}'.format(x)
    cv.displayOverlay('image', text, 1000)
    cv.imshow('image', img)

def mouse(event, x, y, flags, param):
    """Mouse callback function."""
    text = 'mouse at ({}, {})'.format(x, y)
    cv.displayOverlay('image', 'Overlay: ' + text, 1000)
    cv.displayStatusBar('image', 'Statusbar: ' + text, 1000)

img = cv.imread('messi.jpg', cv.IMREAD_COLOR)
cv.imshow('image', img)

cv.setMouseCallback('image', mouse)
cv.createTrackbar('x', 'image', 100, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()