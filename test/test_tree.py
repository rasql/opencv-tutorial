from tree import Node
import pytest

n0 = Node(1)
n1 =    Node(1)
n2 =        Node(1)
n3 =        Node()
n4 =    Node(-1)
n5 =    Node()

def test_node():
    assert  n0.children == [n1, n4, n5]

def test_node_children2():
    assert  n1.children == [n2, n3]

def test_node_parent():
    assert  n2.parent == n1
    assert  n4.parent == n0
    assert  n5.parent == n0
