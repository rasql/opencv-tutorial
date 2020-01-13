# Add a trackbar
import cv2 as cv

def trackbar(x):
    """Trackbar callback function."""
    text = f'Trackbar: {x}'
    cv.displayOverlay('image', text, 1000)
    cv.imshow('image', img)

img = cv.imread('messi.jpg', cv.IMREAD_COLOR)
cv.imshow('image', img)
cv.createTrackbar('x', 'image', 100, 255, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()