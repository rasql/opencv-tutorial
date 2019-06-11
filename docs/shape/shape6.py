"""Draw  an ellipse."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Window()
        Text('Polygon')

        for j in range(3):
            pts = []
            for i in range(5):
                pt = (random.randint(10, 190), random.randint(10, 190))
                pts.append(pt)
            Polygon(pts)
    
if __name__ == '__main__':
    Demo().run()