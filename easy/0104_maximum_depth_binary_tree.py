from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Default case, if the node is empty, return 0
        if not root:
            return 0

        # Recursively get the left and right depth
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Return the maximum of both sides
        # The +1 counts the parent node
        return max(left_depth, right_depth) + 1


sol = Solution()

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert sol.maxDepth(root) == 3

root = None
assert sol.maxDepth(root) == 0

root = TreeNode(1, None, TreeNode(2))
assert sol.maxDepth(root) == 2
