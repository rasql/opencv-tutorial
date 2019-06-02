"""Draw graphic elements to an image."""

import numpy as np
import cv2

def nothing(x):
    pass

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)

# Create a black image
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(511,511),BLUE,5)

img = cv2.rectangle(img,(384,0),(510,128),GREEN,3)

img = cv2.circle(img,(447,63), 63, RED, -1)

# create trackbars for color change

cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createButton('Button', nothing)
cv2.imshow('image',img)


k = cv2.waitKey(0)
cv2.destroyAllWindows()