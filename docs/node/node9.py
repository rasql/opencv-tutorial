"""Place shapes inside nodes."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        pts = ((20, 20), (200, 30), (100, 100))
        
        Node()
        Node3()
        Line2()
        Node3(pts)
        Line2((50, 50), (250, 100), thickness=3)
        

if __name__ == '__main__':
    Demo().run()