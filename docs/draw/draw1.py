"""Template for making OpenCV apps."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super(Demo, self).__init__()
        img = cv.imread('intro/messi.jpg', cv.IMREAD_COLOR)

        win = Window('image', img)
        win.objects.append(Rectangle(img, (20, 20), (100, 100), YELLOW, -1))
        win.objects.append(Rectangle(img, (420, 20), (200, 100), CYAN, 5))
        win.objects.append(Line(img, (20, 20), (200, 100), BLUE, 5))
        win.objects.append(Line(img, (420, 20), (200, 100), GREEN, 5))
        
        win2 = Window('image2', img)
        p0 = 300, 100        
        win2.objects.append(Circle(img, p0, 200, YELLOW, 1))
        win2.objects.append(Ellipse(img, p0, (100, 50), MAGENTA, 1))
        pts = np.array([[50, 50], [500, 20], [150, 190]], np.int32)
        win2.objects.append(Polygon(img, pts, MAGENTA, 4))
        win2.objects.append(Text(img, 'OpenCV', (100, 100), WHITE))

if __name__ == '__main__':
    Demo().run()