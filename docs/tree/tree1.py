from tree import Node

n = Node()
Node(parent=n)
Node(parent=n)
n2 = Node(parent=n)
Node(parent=n2)
Node(parent=n2)

print(Node.nodes)
n.print_tree()


for i in range(5):
    n2 = n2.sibling()
    print(n)