"""Display nodes in different directions."""
from cvlib import *

class Demo(App):
    def __init__(self):
        super().__init__()
        
        for i in range(5):
            Node(dir=(1, 0), size=(20, 20))

        for i in range(5):
            Node(dir=(0, 1))

        for i in range(5):
            Node(dir=(1, -1))

        for i in range(5):
            Node(dir=(1, 1))

if __name__ == '__main__':
    Demo().run()