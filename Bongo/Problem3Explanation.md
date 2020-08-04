# Python-Code-Test

#### Algorithm:

1) Create a recursive function that takes a node and the two values node1 and node2.
2) If the current node is null then return none value as lca.
3) If the value of the current node is equal to both node1 and node2, then return the current node as lca.
4) Call the recursive function for the left subtree.
5) Call the recursive function for thr right subtree.
6) If left and right subtree both exist then return the current node as lca.
7) Return left subtree as lca if left subtree exist otherwise return right subtree as lca.

#### Complexity Analysis:

Time Complexity: Θ(n).
The time Complexity of the solution is Θ(n), where n is the height of the tree.
Space Complexity: O(1).
If recursive stack space is ignored, the space complexity of the above solution is constant.
