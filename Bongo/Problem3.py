class Node:

    def __init__(self, parent):
        self.parent = parent
        self.left = None
        self.right = None

def lca(root, n1, n2):

    if root is None:
        return None

    if root.parent == n1 or root.parent == n2:
        return root

    left_lca = lca(root.left, n1, n2)
    right_lca = lca(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)

node1 = 8
node2 = 5
findLCA = lca(root, node1, node2)
print("LCA of %d and %d is %d" % (node1, node2, findLCA.parent))
