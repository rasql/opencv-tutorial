"""scale an image using the trackbar."""
import cv2 as cv

def trackbar(scale):
    M = cv.getRotationMatrix2D(center, 0, scale/10)
    rotated = cv.warpAffine(img, M, (w, h))
    cv.imshow('window', rotated)

img = cv.imread('fish.jpg')
h, w = img.shape[:2]
center = w//2, h//2

cv.imshow('window', img)
cv.createTrackbar('scale', 'window', 10, 30, trackbar)

cv.waitKey(0)
cv.destroyAllWindows()