from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], cur: int = 0) -> int:
        # Base case: if root is empty, return 0
        if not root:
            return 0

        # Shift the previous value one position to the left (on the decimal system)
        # and add the value of the current node
        cur = cur * 10 + root.val

        # If the current node is a leaf, return the cumulative sum (cur)
        if not root.left and not root.right:
            return cur

        # Check both the left and right nodes
        return self.sumNumbers(root.left, cur) + self.sumNumbers(root.right, cur)


# # Iterative
# class Solution:
#     def sumNumbers(self, root: Optional[TreeNode]) -> int:
#         # Add to the stack the root and the cumulative number (starting at zero)
#         stack = [(root, 0)]
#         total_sum = 0

#         # While we have elements left in the stack
#         while stack:
#             # Retrieve the last node added and the cumulative value
#             root, cur = stack.pop()

#             # Each time we advance to a child, move the cumulative value one
#             # position to the left (multiply by 10) and add the value of the node
#             cur = cur * 10 + root.val

#             # If we reach a leaf, add the cumulative value to the total_sum
#             if not root.left and not root.right:
#                 total_sum += cur

#             # If the node has a left child, add this child to the stack
#             # and the current cumulative value
#             if root.left:
#                 stack.append((root.left, cur))

#             # Same with the right children
#             if root.right:
#                 stack.append((root.right, cur))

#         return total_sum


sol = Solution()

root = TreeNode(1, TreeNode(2), TreeNode(3))
assert sol.sumNumbers(root) == 25

root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
assert sol.sumNumbers(root) == 1026

root = TreeNode(0)
assert sol.sumNumbers(root) == 0
