from tree import Node

import unittest

n0 = Node()
n1 = Node(0)

class Test_NodeCreation(unittest.TestCase):
    def test_is_root(self):
        self.assertTrue(n0.is_root())
        self.assertFalse(n1.is_root())

    def test_root(self):
        self.assertEqual(n0.parent, None)

    def test_child(self):
        self.assertTrue(n1 in n0.children)
        self.assertFalse(n0 in n1.children)
        self.assertEqual(n1.children, [])

if __name__ == '__main__':
    unittest.main()