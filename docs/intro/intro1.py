"""Load, show and save an image."""
from cvlib import *

# Load an color image in grayscale
img = cv.imread('messi.jpg', 0)
# img = cv.imread('messi.jpg', cv.IMREAD_COLOR)

cv.imshow('image', img)
k = cv.waitKey(0)
print('key', k)

cv.imwrite('messigray.png', img)
cv.destroyAllWindows()