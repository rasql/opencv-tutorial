"""Add a button."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Button('Help', help)
        Button('SHIFT', App.win.toggle_shift)
        Button()

if __name__ == '__main__':
    Demo().run()