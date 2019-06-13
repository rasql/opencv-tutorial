"""Executing commands when clicking in nodes."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Node()
        Node(level=1)
        Node(level=1)
        Node(level=1)
        Node(level=-1)
        Node(level=-1)
        Node(level=-1)

if __name__ == '__main__':
    Demo().run()