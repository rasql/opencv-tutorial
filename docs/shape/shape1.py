"""Add markers with a mouse click."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Window()
        TextNode()
        for marker in markers:
            Marker(markerType=marker, dir=(1, 0))

if __name__ == '__main__':
    Demo().run()