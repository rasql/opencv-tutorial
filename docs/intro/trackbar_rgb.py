# Compose an RGB color with 3 trackbars
import cv2 as cv
import numpy as np

def rgb(x):
    """Trackbar callback function."""
    r = cv.getTrackbarPos('red','window')
    g = cv.getTrackbarPos('green','window')
    b = cv.getTrackbarPos('blue','window')
    img[:] = [b, g, r]
    cv.displayOverlay('window', f'Red={r}, Green={g}, Blue={b}')
    cv.imshow('window', img)

img = np.zeros((100, 600, 3), 'uint8')
cv.imshow('window', img)
cv.createTrackbar('red', 'window', 200, 255, rgb)
cv.createTrackbar('green', 'window', 50, 255, rgb)
cv.createTrackbar('blue', 'window', 100, 255, rgb)
rgb(0)

cv.waitKey(0)
cv.destroyAllWindows()