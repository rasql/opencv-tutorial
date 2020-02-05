# image gradient - Laplacian
import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE)
img1 = cv.Laplacian(img.copy(), 8)
cv.imshow('window', np.hstack([img, img1]))

cv.waitKey(0)
cv.destroyAllWindows()