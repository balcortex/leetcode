from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: if the list is empty, return None
        if not nums:
            return None

        # Get the middle index
        mid = len(nums) // 2

        # The root is the element at middle index
        # Call recursively for both left and right children
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])

        return root


def identicalTrees(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return (
            (a.val == b.val)
            and identicalTrees(a.left, b.left)
            and identicalTrees(a.right, b.right)
        )

    return False


sol = Solution()

nums = [-10, -3, 0, 5, 9]
expected = TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5)))
assert identicalTrees(sol.sortedArrayToBST(nums), expected) is True

nums = [1, 3]
expected = TreeNode(3, TreeNode(1))
assert identicalTrees(sol.sortedArrayToBST(nums), expected) is True
