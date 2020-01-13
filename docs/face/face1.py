import cv2 as cv

print(cv.__version__)

img = cv.imread('faces.jpg')
cv.imshow('Faces', img)
cv.waitKey(0)