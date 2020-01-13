"""Acces a slice of the image."""
import cv2 as cv
img = cv.imread('messi.jpg')

img[250:300, 50:550] = (0, 255, 0)
face = img[80:230, 270:390]
img[0:150, 0:120] = face

cv.imshow('window', img)
cv.waitKey(0)
cv.destroyAllWindows()