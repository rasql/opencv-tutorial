# HSV histogram
from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread('lego.png')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
chans = cv.split(hsv)
colors = 'b', 'g', 'r'


h, s, v = cv.split(hsv)

plt.figure()
plt.title('Flattened color histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

for i in range(3):
    hist = cv.calcHist([chans[i]], [0], None, [256], [0, 255])
    plt.plot(hist, color=colors[i])
    plt.xlim([0, 256])
    plt.ylim([0, 3000])

plt.show()
cv.waitKey(0)