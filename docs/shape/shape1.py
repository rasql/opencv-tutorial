"""Add markers with a mouse click."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Window()
        TextNode()

if __name__ == '__main__':
    Demo().run()