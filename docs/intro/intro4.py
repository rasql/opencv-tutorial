"""Draw graphic elements to an image."""
from cvlib import *

def nothing(x):
    pass

# Create a black image
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')

# Draw a diagonal blue line with thickness of 5 px
img = cv.line(img,(0,0),(511,511),BLUE,5)
img = cv.rectangle(img,(384,0),(510,128),GREEN,3)
img = cv.circle(img,(447,63), 63, RED, -1)

# create trackbars for color change
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
cv.createButton('Button', nothing)
cv.imshow('image',img)

cv.waitKey(0)
cv.destroyAllWindows()