"""Executing commands when clicking in nodes."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Node(cmd=help)
        Node(cmd=App.win.toggle_visible)
        Node(cmd=Text)

if __name__ == '__main__':
    Demo().run()