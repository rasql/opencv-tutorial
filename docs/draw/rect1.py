import cv2 as cv
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

CYAN = (255, 255, 0)
MAGENTA = (255, 0, 255)
YELLOW = (0, 255, 255)

p0 = 100, 10
p1 = 200, 90
p2 = 300, 20    
p3 = 450, 80

img = img = np.zeros((100, 500, 3), np.uint8)
cv.rectangle(img, p0, p1, BLUE, 2)
cv.rectangle(img, p2, p3, GREEN, cv.FILLED)
cv.imshow('RGB', img)

cv.waitKey(0)
cv.destroyAllWindows()