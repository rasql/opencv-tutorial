# Add a trackbar
import cv2 as cv

def trackbar(x):
    """Trackbar callback function."""
    text = f'Trackbar: {x}'
    cv.displayOverlay('window', text, 1000)
    cv.imshow('window', img)

img = cv.imread('messi.jpg', cv.IMREAD_COLOR)
cv.imshow('window', img)
cv.createTrackbar('x', 'window', 100, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()