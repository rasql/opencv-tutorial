import numpy as np

class Node:
    id = 0
    sep = '/'
    nodes = []
    
    def __init__(self, name='', parent=None):
        self.parent = parent
        self.children = []
        self.name = name

        if parent != None:
            self.parent.children.append(self)

        self.id = Node.id
        Node.id += 1
        Node.nodes.append(self)

    def __str__(self):
        return 'node{}'.format(self.id)
        
    def print_tree(self, level=0):
        print('    ' * level + str(self))
        level += 1
        for child in self.children:
            child.print_tree(level)

    def sibling(self, forward=True, wrap=True):
        d = 1 if forward else -1
        n = len(self.parent.children)
        i = self.parent.children.index(self)
        if wrap:
            i = (i+d) % n
        else:
            i = max(0, min(i+d, n-1))
        return self.parent.children[i]

    def walk(self):
        if children != []:
            children[0]
        else:
            pass
            # TO DO
        
if __name__ == '__main__':
    n = Node()
    Node(parent=n)
    Node(parent=n)
    n2 = Node(parent=n)
    Node(parent=n2)
    Node(parent=n2)
    Node(parent=n)
    Node(parent=n)
    

    n2.print_tree()
    for i in range(5):
        n2 = n2.sibling(False, False)
        print(n2)

