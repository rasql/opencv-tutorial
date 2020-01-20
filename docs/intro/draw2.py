"""Draw a cross with a circle."""
from cvlib import *

w, h = 600, 300
d = 1

def cb(event, x, y, flags, param):
    """Mouse callback function."""
    # img = np.zeros((h, w, 3), np.uint8)
    img = img0.copy()
    if event == 1:
        cv.circle(img0, (x, y), 50, BLUE, d)
    cv.line(img, (x, 0), (x, h), RED, d) 
    cv.line(img, (0, y), (w, y), RED, d)
    cv.circle(img, (x, y), 50, GREEN, d)
    str = '({}, {})'.format(x, y)
    cv.putText(img, str, (x, y), font, 1, YELLOW, 2, cv.LINE_AA)

    cv.imshow('window, img)

img0 = np.zeros((h, w, 3), np.uint8)
font = cv.FONT_HERSHEY_SIMPLEX
cv.namedWindow('window)
cv.setMouseCallback('window, cb)
cv.imshow('window,img0)

cv.waitKey(0)
cv.destroyAllWindows()