# The task is to implement binary tree traversal methods. We'll implement three common types of traversal: 
# in-order, pre-order, and post-order. These methods will be implemented as part of a BinaryTree class.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def in_order_traversal(self, node, visit):
        """Perform in-order traversal of the tree.
        
        In-order traversal visits the left subtree, the root, and then the right subtree.
        This traversal is useful for retrieving data in sorted order from a binary search tree.
        """
        if node is not None:
            self.in_order_traversal(node.left, visit)
            visit(node.value)
            self.in_order_traversal(node.right, visit)

    def pre_order_traversal(self, node, visit):
        """Perform pre-order traversal of the tree.
        
        Pre-order traversal visits the root, then the left subtree, and finally the right subtree.
        This traversal is useful for creating a copy of the tree or getting a prefix expression of the tree.
        """
        if node is not None:
            visit(node.value)
            self.pre_order_traversal(node.left, visit)
            self.pre_order_traversal(node.right, visit)

    def post_order_traversal(self, node, visit):
        """Perform post-order traversal of the tree.
        
        Post-order traversal visits the left subtree, the right subtree, and then the root.
        This traversal is useful for deleting the tree or evaluating a postfix expression of the tree.
        """
        if node is not None:
            self.post_order_traversal(node.left, visit)
            self.post_order_traversal(node.right, visit)
            visit(node.value)

# Example usage:
# tree = BinaryTree(TreeNode(1))
# tree.root.left = TreeNode(2)
# tree.root.right = TreeNode(3)
# tree.root.left.left = TreeNode(4)
# tree.root.left.right = TreeNode(5)
# tree.root.right.left = TreeNode(6)
# tree.root.right.right = TreeNode(7)

# result = []
# tree.in_order_traversal(tree.root, lambda x: result.append(x))
# print(result)  # Output: [4, 2, 5, 1, 6, 3, 7]

# result = []
# tree.pre_order_traversal(tree.root, lambda x: result.append(x))
# print(result)  # Output: [1, 2, 4, 5, 3, 6, 7]

# result = []
# tree.post_order_traversal(tree.root, lambda x: result.append(x))
# print(result)  # Output: [4, 5, 2, 6, 7, 3, 1]