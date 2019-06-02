"""Open an image and display it with Matplotlib."""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load an color image in grayscale
# img = cv2.imread('messi.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.imread('messi.jpg', cv2.IMREAD_COLOR)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()