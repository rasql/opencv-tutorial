# Extract an object from HSV color space with the mouse
import cv2 as cv
import numpy as np

img = cv.imread('legos.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

def mouse(event, x, y, flags, param):
    global hsv
    hue = hsv[y, x, 0]
    lower = (hue, 30, 30)
    upper = (hue+5, 250, 250)

    print(hsv.dtype, hsv.shape)

    mask = cv.inRange(hsv, lower, upper)
    # TypeError: Expected Ptr<cv::UMat> for argument '%s'

    img2 = cv.bitwise_and(img, img, mask=mask)

    cv.imshow('window', np.hstack([img, img2]))
    cv.displayStatusBar('window', f'hue={hue}')

cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()