import cv2 as cv
import numpy as np
from draw import *

pts = []

def draw(x):
    d = cv.getTrackbarPos('thickness', 'window')
    d = -1 if d==0 else d
    i = cv.getTrackbarPos('color', 'window')
    color = colors[i]
    img[:] = img0
    cv.polylines(img, np.array([pts]), True, color, d)
    cv.imshow('window', img)
    text = f'color={color}, thickness={d}'
    cv.displayOverlay('window', text)

def mouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        pts.append((x, y))
        draw(0)

cv.setMouseCallback('window', mouse)
cv.createTrackbar('color', 'window', 0, 6, draw)
cv.createTrackbar('thickness', 'window', 2, 10, draw)
draw(0)

cv.waitKey(0)
cv.destroyAllWindows()