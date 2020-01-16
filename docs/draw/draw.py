import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (0, 0, 255)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

CYAN = (255, 255, 0)
MAGENTA = (255, 0, 255)
YELLOW = (0, 255, 255)

colors = (RED, GREEN, BLUE, MAGENTA, CYAN, YELLOW, WHITE)

p0 = 0, 0
p1 = 0, 0
d = 1
color = WHITE
img0 = np.zeros((200, 500, 3), np.uint8)

# Trackbar callback functions
def trackbar(x):
    return

    color = colors[x]
