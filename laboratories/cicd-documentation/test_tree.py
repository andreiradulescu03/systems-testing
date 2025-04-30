import unittest
from tree import Tree

class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()
        for value in [3, 1, 4, 0, 2]:
            self.tree.add(value)

    def test_find_existing_node(self):
        node = self.tree.find(2)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 2)

    def test_find_nonexistent_node(self):
        node = self.tree.find(99)
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
