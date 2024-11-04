class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def sum_of_nodes_without_siblings(root):
    if not root:
        return 0

    queue = deque([root])
    sum_without_siblings = 0

    while queue:
        node = queue.popleft()

        # Check if the node has only one child and add that child's value
        if node.left and not node.right:
            sum_without_siblings += node.left.val
        elif node.right and not node.left:
            sum_without_siblings += node.right.val

        # Add children to the queue for level order traversal
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return sum_without_siblings

# Hardcoded tree structure:
#        1
#       / \
#      2   3
#       \
#        4
#           \
#            5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)

# Calculate the sum of nodes without siblings
result = sum_of_nodes_without_siblings(root)
print("Sum of nodes without siblings:", result)
