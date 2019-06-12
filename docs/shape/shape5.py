"""Draw  an ellipse."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Window()
        Text('Ellipse')

        Ellipse((200, 100), (200, 30))

        for i in range(10):
            col = random.choice([RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, WHITE])
            p0 = (random.randint(10, 590), random.randint(10, 190))
            p1 = (random.randint(10, 590), random.randint(10, 190))
            a = random.randint(0, 360)
            Ellipse(p0, p1, thickness=2, angle=a, color=col)
            
if __name__ == '__main__':
    Demo().run()