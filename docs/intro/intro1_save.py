import cv2 as cv

img = cv.imread('messi.jpg')
cv.imshow('window', img)

cv.imwrite('messi.png', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite('messi_gray.png', gray)

cv.waitKey(0)
cv.destroyAllWindows()