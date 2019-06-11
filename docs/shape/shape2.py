"""Draw random lines."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Window()
        TextNode('Random lines')

        for i in range(10):
            col = random.choice([RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA])
            p0 = (random.randint(10, 590), random.randint(10, 190))
            p1 = (random.randint(10, 590), random.randint(10, 190))
            d = random.randint(1, 5) 
            Line(p0, p1, thickness=d, color=col)
            
if __name__ == '__main__':
    Demo().run()