# Add an overlay
import cv2 as cv

file = 'messi.jpg'
img = cv.imread(file, cv.IMREAD_COLOR)

cv.imshow('window', img)
text = f'file name: {file}\n\
        width: {img.shape[1]}\n\
        height: {img.shape[0]}\n\
        channels: {img.shape[2]}'

cv.displayOverlay('window', text)

cv.waitKey(0)
cv.destroyAllWindows()