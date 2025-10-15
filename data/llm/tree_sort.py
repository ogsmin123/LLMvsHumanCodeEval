class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # If the tree is empty, set the root to the new node
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        # Insert value in the left subtree if it's less than the current node's value
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        # Insert value in the right subtree if it's greater than the current node's value
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)
        # If the value is equal, we do nothing to avoid duplicates

    def in_order_traversal(self):
        # Perform an in-order traversal to get values in sorted order
        result = []
        self._in_order_traversal_recursively(self.root, result)
        return result

    def _in_order_traversal_recursively(self, node, result):
        if node is not None:
            # Traverse the left subtree first
            self._in_order_traversal_recursively(node.left, result)
            # Visit the current node
            result.append(node.value)
            # Traverse the right subtree
            self._in_order_traversal_recursively(node.right, result)

def tree_sort(values):
    bst = BinarySearchTree()
    for value in values:
        bst.insert(value)
    return bst.in_order_traversal()

# The tree_sort function can be used to sort an array of numbers by inserting them into a BST
# and then performing an in-order traversal to retrieve them in sorted order. This approach
# handles duplicates by ignoring them during insertion, which is a common trade-off in BSTs.