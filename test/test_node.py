from cvlib import Node

n0 = Node(1)
n1 =    Node(1)
n2 =        Node(1)
n3 =        Node()
n4 =    Node(-1)
n5 =    Node()

n0.print_tree()

def test_node():
    assert  n0.children == [n1, n4, n5]
    assert  n1.children == [n2, n3]

def test_node_parent():
    assert  n2.parent == n1
    assert  n4.parent == n0
    assert  n5.parent == n0
    assert  n2.parent.parent == n0

def test_node_name():
    assert str(n0) == 'node0'
    assert str(n5) == 'node5'

def test_node_id():
    assert n0.id == 0
    assert n5.id == 5

def test_nodes():
    assert Node.nodes == [n0, n1, n2, n3, n4, n5]
    assert Node.sep == '/'
    assert n0.is_root()

def test_path():
    assert n3.get_path() == [n0, n1, n3]
    assert n5.get_path() == [n0, n5]
