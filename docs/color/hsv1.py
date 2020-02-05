# Compose an RGB color with 3 trackbars
import cv2 as cv
import numpy as np

v = np.fromfunction(lambda i, j: i, (256, 256), dtype=np.uint8)
h = np.fromfunction(lambda i, j: j, (256, 256), dtype=np.uint8)
z = np.ones((256, 256), dtype=np.uint8) * 255

img = cv.merge([h, v, z])
bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow('window', bgr)

img = cv.merge([h, z, v])
bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
cv.imshow('window2', bgr)

cv.waitKey(0)
cv.destroyAllWindows()