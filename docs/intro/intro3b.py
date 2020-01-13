"""Draw pixels with the mouse."""
import cv2 as cv

def mouse(event, x, y, flags, param):
    text = f'Mouse at ({x}, {y}), flags={flags}, param={param}'
    cv.displayOverlay('window', text, 1000)
    if flags == 1:
        img[y, x] = [0, 0, 255]
    cv.imshow('window', img)

img = cv.imread('messi.jpg')
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

cv.waitKey(0)
cv.destroyAllWindows()