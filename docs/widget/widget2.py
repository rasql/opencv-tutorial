"""Display text."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Window()
        Text.options.update(dict(fontScale=1, thickness=1, color=RED))

        fonts = cv_dir('FONT_HERSHEY.*')
        print(fonts)

        for font in fonts:
            type = eval('cv.'+font)
            Text(font, fontType=type, gap=(0, 0))

if __name__ == '__main__':
    Demo().run()