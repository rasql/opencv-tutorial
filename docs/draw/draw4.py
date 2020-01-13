import cv2 as cv
import numpy as np

BLUE = (255, 0, 0)
center = 200, 50
axes = 100, 30
angle = 15

img = img = np.zeros((100, 600, 3), np.uint8)
cv.ellipse(img, center, axes, angle, 0, 360, BLUE, 2)
cv.imshow('RGB', img)

cv.waitKey(0)
cv.destroyAllWindows()