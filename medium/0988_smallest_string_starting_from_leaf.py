from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # The tree only contains lowercase letters, so we use the next char
        # as the upper bound to compare (is a `{` character).
        smallest_string = chr(ord("z") + 1)

        def helper(node: TreeNode, string: str) -> str:
            # We are referring to the variable outside this function
            nonlocal smallest_string

            # Every time the function is called, we travel one node down,
            # so we concatenate the value of the current node and prev string
            string = chr(node.val + ord("a")) + string

            # If we reach a leaf, perform a comparison
            if not node.left and not node.right:
                smallest_string = min(smallest_string, string)

            # If there are more children, call recursively
            if node.left:
                helper(node.left, string)
            if node.right:
                helper(node.right, string)

        # Start with the root node and an empty string
        helper(root, "")

        return smallest_string


sol = Solution()

root = TreeNode(
    0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(3), TreeNode(4))
)
assert sol.smallestFromLeaf(root) == "dba"

root = TreeNode(
    25, TreeNode(1, TreeNode(1), TreeNode(3)), TreeNode(3, TreeNode(0), TreeNode(2))
)
assert sol.smallestFromLeaf(root) == "adz"

root = TreeNode(
    2, TreeNode(2, None, TreeNode(1, TreeNode(0))), TreeNode(1, TreeNode(0))
)
assert sol.smallestFromLeaf(root) == "abc"
