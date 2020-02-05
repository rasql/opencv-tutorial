# color spaces
import cv2 as cv
import numpy as np

color_spaces = [s for s in dir(cv) if s.startswith('COLOR_BGR2')]
color_spaces = ('COLOR_BGR2GRAY', 'COLOR_BGR2HSV', 'COLOR_BGR2HSV_FULL', 'COLOR_BGR2LAB')

n = len(color_spaces)

M = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
size = (640, 360)
cs = 'COLOR_BGR2GRAY'

def trackbar(x):
    global cs
    cs = color_spaces[x]
    cv.displayOverlay('window', f'color space={cs}')

cap = cv.VideoCapture(0)
ret, img = cap.read()
cv.imshow('window', img)
cv.createTrackbar('color space', 'window', 0, n-1, trackbar)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    img = cv.warpAffine(frame, M, size)

    img = cv.cvtColor(img, eval('cv.' + cs))
    
    cv.imshow('window', img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
