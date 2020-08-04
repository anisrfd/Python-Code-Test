import unittest
import Bongo.Problem3 as lca

root = lca.binaryTree()
class TestLca(unittest.TestCase):

    def test_node8_5(self):
        self.assertEqual(lca.lca(root, 8, 5).parent, 2)

    def test_node6_7(self):
        self.assertEqual(lca.lca(root, 6, 7).parent, 3)

    def test_node3_7(self):
        self.assertEqual(lca.lca(root, 3, 7).parent, 3)

    
if __name__ == '__main__':
    unittest.main()