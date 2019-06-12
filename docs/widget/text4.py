"""Place text inside a node."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Node()
        Text(level=1)
        Text()
        Text()
        
        Node(level=-1, pos=(200, 20))
        Text(level=1)
        Text()
        Text().parent.enclose_children()

if __name__ == '__main__':
    Demo().run()