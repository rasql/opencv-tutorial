from app import *

class Demo(App):
    def __init__(self):
        super().__init__()

        Window()
        obj1 = Node(App.win, (100, 20), (100,100))

        Node(obj1, (0, 0), (50, 50))
        Node(obj1, (30, 30), (50, 50))

        # Text(color=GREEN)

if __name__ == '__main__':
    Demo().run()