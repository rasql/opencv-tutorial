import cv2 as cv
import numpy as np

RED = (0, 0, 255)
p0 = (10, 100)

font = cv.FONT_HERSHEY_SIMPLEX
img = np.zeros((200, 500, 3), np.uint8)
cv.putText(img,'OpenCV', p0, font, 4, RED, 2, cv.LINE_AA)
cv.imshow('window', img)

cv.waitKey(0)
cv.destroyAllWindows()