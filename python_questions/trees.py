"""
trees are a type of data structure used to represent hierarchical relationships among elements.
A tree is composed of nodes, where one node is the root, and the others are connected to it as children in a hierarchical manner.

Key Terminology:
Root: The top node of the tree.
Node: A basic unit of a tree containing a value and references to its children.
Edge: A connection between a parent node and a child node.
Parent: A node that has child nodes.
Child: A node that descends from another node (its parent).
Leaf: A node with no children.
Depth: The number of edges from the root to a node.
Height: The number of edges in the longest path from a node to a leaf.
Subtree: A tree formed by a node and its descendants.

"""

class TreeNode():
    def __init__(self,value):
        self.value = value
        self.children = []
    def add_child(self,child_node):
        self.children.append(child_node)
    def __repr__(self):
        return f"TreeNode({self.value})"

#Usage Example
root = TreeNode('A')
child1 = TreeNode('B')
child2 = TreeNode('C')

root.add_child(child1)
root.add_child(child2)

child1.add_child(TreeNode('D'))
child1.add_child(TreeNode('E'))

print(f"Root is {root.value}")
print(f"Roots children are {[i.value for i in root.children]}")
print(f"Child's children are {[i.value for i in child1.children]}")


"""
Types of Trees
Binary Tree: Each node has at most two children (left and right).
Binary Search Tree (BST): A binary tree where the left child contains values less than the parent, and the right child contains values greater than the parent.
AVL Tree: A self-balancing binary search tree.
N-ary Tree: A tree where each node can have at most N children.
Trie: A tree used for storing strings, often used in searching and auto-completion.
"""

#Example - Binary Tree Implementation
class BinaryTreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    def __repr__(self):
        return f"Binary Tree Node {self.value}"

root = BinaryTreeNode(10)
root.left = BinaryTreeNode(5)
root.right = BinaryTreeNode(12)

root.left.left = BinaryTreeNode(3)
root.left.right = BinaryTreeNode(7)

"""
Traversing a Tree
Tree traversal algorithms visit all nodes in a tree in a specific order:

Pre-order: Visit the root, then left subtree, and then right subtree.
In-order: Visit the left subtree, then the root, and then the right subtree.
Post-order: Visit the left subtree, then the right subtree, and finally the root.
Level-order (BFS): Visit nodes level by level (breadth-first traversal).

"""

#Example - Inorder traversal of a Binary Tree
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value,end="")
        in_order_traversal(node.right)

in_order_traversal(root)

"""
Use Cases of Trees
Hierarchical data: Representing file systems, organizational charts, etc.
Search algorithms: Binary Search Tree, Trie for string search.
Parsing expressions: Abstract Syntax Trees (ASTs) in compilers.
Machine learning: Decision trees, Random Forests.
Trees are a versatile structure for solving hierarchical or recursive problems efficiently.

"""
