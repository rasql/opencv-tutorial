"""Place shapes inside nodes."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        pts = ((20, 20), (200, 30), (100, 100))
        
        Node()
        # Node3()
        Arrow()
        Line()
        Rectangle()   
        Polygon(*pts) 

if __name__ == '__main__':
    Demo().run()