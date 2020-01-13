import cv2 as cv
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

CYAN = (255, 255, 0)
MAGENTA = (255, 0, 255)
YELLOW = (0, 255, 255)

p0 = 10, 10
p1 = 300, 90
p2 = 500, 10

img = img = np.zeros((100, 600, 3), np.uint8)
cv.line(img, p0, p1, RED, 2)
cv.line(img, p1, p2, YELLOW, 5)
cv.imshow('RGB', img)

gray_img = np.zeros((100, 600), np.uint8)
cv.line(gray_img, p0, p1, 100, 2)
cv.line(gray_img, p1, p2, 255,5)
cv.imshow('Gray', gray_img)

cv.waitKey(0)
cv.destroyAllWindows()