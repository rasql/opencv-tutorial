"""Object Oriented Programming (OOP)."""
from cvlib import *

class App:
    def __init__(self):
        img = cv.imread('messi.jpg', cv.IMREAD_COLOR)
        Window('image', img)
        Window('image2', img)

    def run(self):
        """Run the main event loop."""
        k=0
        while k != ord('q'):
            k = cv.waitKey(0)
            print(k, chr(k))
        
        cv.destroyAllWindows()

if __name__ == '__main__':
    App().run()