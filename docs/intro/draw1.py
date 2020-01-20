import numpy as np
import cv

RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

def track_x(x):
    cv.line(img, (x, 0), (x, h), RED, d)
    cv.line(img, (0, y), (w, y), RED, d)
    cv.imshow('window,img)

def track_y(y):
    cv.line(img, (x, 0), (x, h), RED, d)
    cv.line(img, (0, y), (w, y), RED, d)
    cv.imshow('window,img)


file = 'messi.jpg'

# img = cv.imread(file, cv.IMREAD_GRAYSCALE)
img0 = cv.imread(file, cv.IMREAD_COLOR)
cv.imshow('window,img)

w, h = 800, 600
x, y = 100, 100
d = 1

cv.createTrackbar('x', 'window, x, w, track_x)
cv.createTrackbar('y', 'window, y, h, track_y)
cv.line(img, (x, 0), (x, h), RED, d)
cv.line(img, (0, y), (w, y), RED, d)

cv.imshow('window,img)

k = cv.waitKey(0)

print('key', k)

cv.imwrite('messigray.png',img)
cv.destroyAllWindows()