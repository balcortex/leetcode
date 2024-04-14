from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # Base case, the root is empty
        if not root:
            return 0

        # The left node is a leaf
        if root.left and not root.left.left and not root.left.right:
            # Check also the right node for left leaves
            return root.left.val + self.sumOfLeftLeaves(root.right)

        # Return the sum of all left leaves in the left node
        # and all the left leaves in the right node
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


sol = Solution()

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
assert sol.sumOfLeftLeaves(root) == 24

root = None
assert sol.sumOfLeftLeaves(root) == 0

root = TreeNode(3, TreeNode(4))
assert sol.sumOfLeftLeaves(root) == 4
