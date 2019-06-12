"""Multiple embedded nodes."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Node()
        Node(level=1)
        Node(level=1)
        Node(level=1)
        Node(level=-3)
        Node()
        Node()

if __name__ == '__main__':
    Demo().run()