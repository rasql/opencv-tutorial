"""Rotate and scale image with mouse."""
import cv2 as cv
import numpy as np

RED = (0, 0, 255)
p0, p1 = (100, 30), (400, 90)

def mouse(event, x, y, flags, param):
    global p0, p1
    
    if event == cv.EVENT_LBUTTONDOWN:
        p0 = x, y
        p1 = x, y

    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        p1 = x, y

    elif event == cv.EVENT_LBUTTONUP:
        p1 = x, y

    
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    angle = -np.degrees(np.arctan2(dy, dx))
    len = np.sqrt(dx**2 + dy**2) / 50
    cv.displayOverlay('window', f'p0={p0}, p1={p1}, angle={angle:.1f}, len={len:.1f}')

    M = cv.getRotationMatrix2D(p0, angle, len)
    img2 = cv.warpAffine(img, M, (w, h))
    cv.line(img2, p0, p1, RED, 2)
    cv.imshow('window', img2)

img = cv.imread('fish.jpg')
h, w = img.shape[:2]
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()