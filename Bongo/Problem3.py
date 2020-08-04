class Node:

    def __init__(self, parent):
        self.parent = parent
        self.left = None
        self.right = None

def lca(root, node1, node2):

    if root is None:
        return None

    if root.parent == node1 or root.parent == node2:
        return root

    left_lca = lca(root.left, node1, node2)
    right_lca = lca(root.right, node1, node2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca

def binaryTree():

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)

    return root

if __name__ == '__main__':
    root = binaryTree()
    node1 = 8
    node2 = 5
    findLCA = lca(root, node1, node2)
    print("LCA of %d and %d is %d" % (node1, node2, findLCA.parent))

