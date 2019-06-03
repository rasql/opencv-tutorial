"""Open an image and display it with Matplotlib."""
from cvlib import *

# Load an color image in grayscale
# img = cv.imread('messi.jpg',cv.IMREAD_GRAYSCALE)
img = cv.imread('messi.jpg', cv.IMREAD_COLOR)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()