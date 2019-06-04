"""Object Oriented Programming (OOP)."""
import cv2 as cv

class Window:
    """Create a window with an image."""
    def __init__(self, win, img):
        self.win = win
        self.img = img
        cv.imshow(win, img)

class App:
    def __init__(self):
        img = cv.imread('messi.jpg', cv.IMREAD_GRAYSCALE)
        Window('image', img)

    def run(self):
        """Run the main event loop."""
        k=0
        while k != ord('q'):
            k = cv.waitKey(0)
            print(k, chr(k))
        
        cv.destroyAllWindows()

if __name__ == '__main__':
    App().run()