"""Draw blue circles upon mouse double click."""
from cvlib import *

w, h = 600, 300

# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 50, BLUE, -1)

# Create a black image, a window and bind the function to window
img = np.zeros((h, w, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while(1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()