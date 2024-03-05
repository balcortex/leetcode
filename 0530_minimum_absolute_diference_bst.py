# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder_traversal(root: Optional[TreeNode], lst: List):
            if not root:
                return None
            inorder_traversal(root.left, lst)
            lst.append(root.val)
            inorder_traversal(root.right, lst)

            return lst

        nums = []
        inorder_traversal(root, nums)

        nums.sort()

        return min(num2 - num1 for num1, num2 in zip(nums, nums[1:]))
