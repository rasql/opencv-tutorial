import cv2 as cv
import numpy as np

img = img = np.zeros((100, 600, 3), np.uint8)
cv.imshow('RGB', img)

gray_img = np.zeros((100, 600), np.uint8)
cv.imshow('Gray', gray_img)

cv.waitKey(0)
cv.destroyAllWindows()