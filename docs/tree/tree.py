import numpy as np

class Node:
    """Create a basic node for a tree structure."""
    id = 0
    sep = '/'
    nodes = []
    path = []
    
    def __init__(self, parent=0, children=[]):
        """Create a node.
        parent = None (root)
        parent = Node()
        parent = 1 (level increase, child to last)
        parent = 0 (same level, sibling to last)
        parent = -1 (level decrease, oncle to last)
        """
        
        if Node.id == 0:
            self.parent = None
            Node.path = [self]
        elif isinstance(parent, int):
            if parent == 1:
                self.parent = Node.path[-1]
            else:
                self.parent = Node.path[-2+parent]
                Node.path = Node.path[:-1+parent]
            Node.path.append(self)
        else:
            self.parent = parent
            Node.path = parent.get_path()

        self.children = []
        
        if self.parent != None:
            self.parent.children.append(self)

        self.id = Node.id
        Node.id += 1
        Node.nodes.append(self)

    def __str__(self):
        return 'node{}'.format(self.id)
        
    def print_tree(self, level=0):
        """Print a tree view."""
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

    def is_root(self):
        return self.parent == None

    def walk(self, i=0):
        print(self)
        if i < len(self.children):
            walk(self.children[i], 0)
        else:
            walk(self)
              # TO 
    def get_breadth_first_nodes(self):
        """Get breath-first nodes."""
        nodes = []
        stack = [self]
        while stack:
            n0 = stack.pop(0)
            nodes.append(n0)
            stack.extend(n0.children)
        return nodes

    def get_depth_first_nodes(self):
        """Get depth-first nodes."""
        nodes = []
        stack = [self]
        while stack:
            n0 = stack.pop(0)
            nodes.append(n0)
            stack = n0.children + stack
        return nodes

    def get_path(node):
        path = []
        while node != None:
            path.insert(0, node)
            node = node.parent
        return path
        
if __name__ == '__main__':
    root = Node()

    Node(1)
    Node(1)
    Node()
    Node()
    
    Node(root)
    Node(1)
    Node()
    Node()

    Node(1)
    Node()
    Node()

    Node(root)
    Node(1)
    Node()
    Node()

    root.print_tree()

for n in root.get_breadth_first_nodes():
    print(n)
    
    



