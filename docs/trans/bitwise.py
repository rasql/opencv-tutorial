"""Bitwise and, or and xor operation"""
import cv2 as cv
import numpy as np

d = 15
rect = np.zeros((100, 100), np.uint8)
cv.rectangle(rect, (d, d), (100-d, 100-d), 255, -1)

circle = np.zeros((100, 100), np.uint8)
cv.circle(circle, (50, 50), 40, 255, -1)

bit_and = cv.bitwise_and(rect, circle)
bit_or = cv.bitwise_or(rect, circle)
bit_xor = cv.bitwise_xor(rect, circle)

img = np.hstack([rect, circle, bit_and, bit_or, bit_xor])

cv.imshow('window', img)
cv.waitKey(0)
cv.destroyAllWindows()