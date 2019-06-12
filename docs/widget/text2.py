"""Display different font types."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Text.options.update(dict(thickness=1, color=RED))

        fonts = cv_dir('FONT_HERSHEY.*')
        for font in fonts:
            type = eval('cv.'+font)
            Text(font, fontFace=type)

if __name__ == '__main__':
    Demo().run()