class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxConsecutiveAncestorDiff(root: TreeNode):
    # Variable to store the maximum difference and the respective nodes
    max_diff = 0
    ancestor_value, descendant_value = None, None

    def helper(node):
        nonlocal max_diff, ancestor_value, descendant_value

        # If node is None, simply return
        if not node:
            return

        # Check the difference with the left child (if exists)
        if node.left:
            diff = abs(node.value - node.left.value)
            if diff > max_diff:
                max_diff = diff
                ancestor_value, descendant_value = node.value, node.left.value
            helper(node.left)

        # Check the difference with the right child (if exists)
        if node.right:
            diff = abs(node.value - node.right.value)
            if diff > max_diff:
                max_diff = diff
                ancestor_value, descendant_value = node.value, node.right.value
            helper(node.right)

    # Start the helper function with the root node
    helper(root)

    # Print the result
    if ancestor_value is not None and descendant_value is not None:
        print(f"Maximum difference: {max_diff} between nodes with values {ancestor_value} and {descendant_value}")
    else:
        print("Tree has no consecutive nodes to compare.")

# Example usage:
# Construct a sample binary tree
#        8
#       / \
#      3   10
#     / \    \
#    1   6    14
#       / \   /
#      4   7 13
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

# Calculate max consecutive ancestor difference
maxConsecutiveAncestorDiff(root)
