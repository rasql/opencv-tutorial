# image gradient - Laplacian
import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE)
img1 = cv.Canny(img, 100, 200)
cv.imshow('window', np.hstack([img, img1]))

cv.waitKey(0)
cv.destroyAllWindows()