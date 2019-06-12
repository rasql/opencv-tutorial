"""Draw random arrows."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Window()
        Text('Arrows')

        for i in range(10):
            col = random.choice([RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, WHITE])
            p0 = (random.randint(10, 590), random.randint(10, 190))
            p1 = (random.randint(10, 590), random.randint(10, 190))
            d = random.randint(1, 5) 
            Arrow(p0, p1, thickness=d, color=col)
            
if __name__ == '__main__':
    Demo().run()