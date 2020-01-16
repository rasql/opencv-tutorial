import cv2 as cv
import numpy as np
from draw import *

def mouse(event, x, y, flags, param):
    text = f'Mouse {event} at ({x}, {y}), flags={flags}, param={param}'
    cv.displayOverlay('window', text, 1000)

    global p0, p1

    if event == cv.EVENT_LBUTTONDOWN:
        p0 = x, y
    elif event == cv.EVENT_MOUSEMOVE and flags == 1:
        p1 = x, y
        img = img0.copy()
        cv.rectangle(img, p0, p1, RED, 1)
        cv.imshow('window', img)

    elif event == cv.EVENT_LBUTTONUP:
        p1 = x, y
        cv.rectangle(img, p0, p1, RED, 1)
        cv.imshow('window', img)

img = img0.copy()
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()