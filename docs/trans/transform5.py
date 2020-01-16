"""Flip an image horizontally and vertically using keys."""
import cv2 as cv

RED = (0, 0, 255)
p0 = 0, 0
p1 = 0, 0

def mouse(event, x, y, flags, param):
    text = f'Mouse {event} at ({x}, {y}), flags={flags}, param={param}'
    cv.displayOverlay('window', text, 1000)

    if event == cv.EVENT_LBUTTONDOWN:
        p0 = x, y
    elif event == cv.EVENT_LBUTTONUP:
        p1 = x, y
        cv.rectangle(img, p0, p1, RED, 1)


img = cv.imread('fish.jpg')
cv.imshow('window', img)
cv.setMouseCallback('window', mouse)

while True:
    k = cv.waitKey(0)
    if k == ord('q'):
        break
 
    cv.imshow('window', img)

cv.destroyAllWindows()