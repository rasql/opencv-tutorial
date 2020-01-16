"""rotation an image using the trackbar."""
import cv2 as cv

def trackbar(angle):
    M = cv.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv.warpAffine(img, M, (w, h))
    cv.imshow('window', rotated)

img = cv.imread('fish.jpg')
h, w = img.shape[:2]
center = w//2, h//2

cv.imshow('window', img)
cv.createTrackbar('angle', 'window', 0, 180, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()