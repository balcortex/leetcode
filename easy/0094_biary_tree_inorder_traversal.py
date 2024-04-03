from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Use a stack to keep track of nodes
        stack = []
        output = []

        # Traverse all items
        while root or stack:
            # First traverse all items until the first left leaf
            while root:
                stack.append(root)
                root = root.left

            # Once the current node has no left children (root == None),
            # pop the last item in the stack (the last one with a value)
            # and add its value to the list
            root = stack.pop()
            output.append(root.val)

            # Then traverse one node to the right of this node
            root = root.right

        return output


## Recursive
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         return (
#             self.inorderTraversal(root.left)
#             + [root.val]
#             + self.inorderTraversal(root.right)
#             if root
#             else []
#         )


sol = Solution()

root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
expected = [1, 3, 2]
assert sol.inorderTraversal(root) == expected

root = []
expected = []
assert sol.inorderTraversal(root) == expected

root = TreeNode(1, None, None)
expected = [1]
assert sol.inorderTraversal(root) == expected
