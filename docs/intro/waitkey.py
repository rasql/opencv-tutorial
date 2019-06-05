"""Show the difference between waitKey and waitKeyEx.
There seems to be none (Mac OS)."""
import cv2 as cv
import numpy as np

img = np.zeros((200, 600, 3), np.uint8)
img[:] = 100

cv.imshow('image', img)

while True:
    k = cv.waitKey()
    print('waitKey', k)
    k = cv.waitKeyEx()
    print('waitKeyEx', k)
    
cv.destroyAllWindows()