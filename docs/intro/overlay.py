# Add an overlay
import cv2 as cv

file = 'messi.jpg'
img = cv.imread(file, cv.IMREAD_COLOR)

cv.imshow('window', img)
cv.displayOverlay('window', f'file name: {file}')

cv.waitKey(0)
cv.destroyAllWindows()