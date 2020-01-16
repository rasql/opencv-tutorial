# Select line color with a trackbar
import cv2 as cv
import numpy as np

RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
CYAN = (255, 255, 0)
MAGENTA = (255, 0, 255)
YELLOW = (0, 255, 255)
WHITE = (255, 255, 255)

colors = (RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, WHITE)
p0, p1 = (100, 30), (400, 90)

def trackbar(x):
    color = colors[x]
    cv.displayOverlay('window', f'color={color}')
    img[:] = 0 
    cv.line(img, p0, p1, color, 10)
    cv.imshow('window', img)

img = np.zeros((100, 500, 3), np.uint8)
cv.line(img, p0, p1, RED, 10)
cv.imshow('window', img)
cv.createTrackbar('color', 'window', 0, 6, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()