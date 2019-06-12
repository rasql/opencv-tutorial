"""Add a button."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        fonts = cv_dir('FONT_H.*')

        Listbox()
        Listbox(fonts, pos=(200, 20), gap=(0, 0))
        
if __name__ == '__main__':
    Demo().run()