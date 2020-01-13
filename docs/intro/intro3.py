"""Catch mouse events and write to statusbar."""
import cv2 as cv

def mouse(event, x, y, flags, param):
    """Mouse callback function."""
    text = f'mouse at ({x}, {y}), flags={flags}, param={param}'
    cv.displayOverlay('window', 'Overlay: ' + text, 1000)

img = cv.imread('messi.jpg')
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()