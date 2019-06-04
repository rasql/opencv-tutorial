"""Load, show and save an image."""
import cv2 as cv

# Load a color image in grayscale
img = cv.imread('messi.jpg', cv.IMREAD_GRAYSCALE)

cv.imshow('image', img)
cv.imwrite('messigray.png', img)

cv.waitKey(0)
cv.destroyAllWindows()