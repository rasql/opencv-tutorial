# Compose an RGB color with 3 trackbars
import cv2 as cv
import numpy as np

v = np.fromfunction(lambda i, j: i, (256, 256), dtype=np.uint8)
h = np.fromfunction(lambda i, j: j, (256, 256), dtype=np.uint8)
z = np.zeros((256, 256), dtype=np.uint8)

img = cv.merge([z, h, v])
cv.imshow('window', img)

cv.waitKey(0)
cv.destroyAllWindows()