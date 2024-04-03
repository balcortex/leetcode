from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Return early if root is empty
        if not root:
            return True

        # Else, call the helper function with the left and right nodes as args
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        # If both left and right are empty, return True
        if not left and not right:
            return True

        # If one is empty and the other not, return False
        if left and not right or right and not left:
            return False

        # If both have values
        # First, compare if both values are equal
        # Second, compare the outer nodes (left.left and right.right)
        # and the inner nodes (left.right, right.left), calling recursively
        # the function.
        return (
            left.val == right.val
            and self.isMirror(left.left, right.right)
            and self.isMirror(left.right, right.left)
        )


sol = Solution()

root = TreeNode(
    1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))
)
assert sol.isSymmetric(root) is True

root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
assert sol.isSymmetric(root) is False
