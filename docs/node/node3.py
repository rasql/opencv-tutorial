"""Embedded nodes."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Node()
        Node(level=1)
        Node()
        Node()
        Node(level=-1, dir=(1, 0))
        Node(level=1, dir=(0, 1))
        Node()
        Node()
        Node().parent.enclose_children()

if __name__ == '__main__':
    Demo().run()