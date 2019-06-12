"""Place shapes inside nodes."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        pts = ((20, 20), (200, 30), (100, 100))
        
        Node3()
        Node3((50, 50), level=1)
        Node3((10, 50), (100, 10))
        Node3((20, 100), (500, 120), (250, 180), level=-1)

if __name__ == '__main__':
    Demo().run()