import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('messi.jpg',0)
# img = cv2.imread('messi.jpg', cv2.IMREAD_COLOR)

cv2.imshow('image',img)
k = cv2.waitKey(0)

print('key', k)

cv2.imwrite('messigray.png',img)
cv2.destroyAllWindows()