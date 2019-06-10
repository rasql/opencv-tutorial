from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Window()
        Node()

        Node(level=1)
        Node()
        TextNode('Text Node')

        Node(level=-1, dir=(1, 0))
        Node(level= 1, size=(200, 30))
        Node()

        Node(level=-1)

if __name__ == '__main__':
    Demo().run()