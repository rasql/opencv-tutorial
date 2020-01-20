# Window GUI expanded, 
import cv2 as cv
import numpy as np

def trackbar(x):
    print(x)

def button(state, param):
    print(state, param)

win = cv.namedWindow('window', flags=cv.WINDOW_GUI_EXPANDED)
img = np.zeros((100, 500, 3), np.uint8)
cv.imshow('window', img)
cv.createTrackbar('x', 'window', 50, 100, trackbar)
cv.setTrackbarMin('x', 'window', -100)

# These trackbars are created on the properties window
cv.createTrackbar('y', '', 50, 100, trackbar)
cv.createTrackbar('z', '', 50, 100, trackbar)
cv.createButton('Button', button, 0)
cv.createButton('Button1', button, 0)
cv.createButton('Button2', button, 0, cv.QT_RADIOBOX)
cv.createButton('Button3', button, 0, cv.QT_CHECKBOX)
cv.setWindowTitle('window', 'New title')



# retval	=	cv.selectROI(img)

while True:
    k = cv.waitKey(10)
    if k == ord('k'):
        break
    elif k == ord('p'):
        print('hello')

cv.destroyAllWindows()