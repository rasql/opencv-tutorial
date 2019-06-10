"""Display a listbox object."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Window()
        Listbox()
        Button()

if __name__ == '__main__':
    Demo().run()