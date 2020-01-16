# Select end point with the mouse
import cv2 as cv
import numpy as np

GREEN = (0, 255, 0)
p0, p1 = (100, 30), (400, 90)

def mouse(event, x, y, flags, param):
    if flags == 1:
        p1 = x, y
        cv.displayOverlay('window', f'p1=({x}, {y})')
        img[:] = 0
        cv.line(img, p0, p1, GREEN, 10)
        cv.imshow('window', img)

img = np.zeros((100, 500, 3), np.uint8)
cv.line(img, p0, p1, GREEN, 10)
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()