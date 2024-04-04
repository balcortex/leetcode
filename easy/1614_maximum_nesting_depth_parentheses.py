class Solution:
    def maxDepth(self, s: str) -> int:
        # We use a dic to directly perform the operation on the counter
        # without using nested conditionals
        dic = {"(": 1, ")": -1}

        # Store the maximum and the current count
        max_ = 0
        count = 0

        # Go through all elements in the string
        for char in s:
            # If the char is not in dict, we add a zero to the counter
            # If we encounter a '(' we increment by one
            # If we encounter a ')' we decrement by one
            count += dic.get(char, 0)

            # Check if we have a new max
            max_ = max(max_, count)

        return max_


sol = Solution()

s = "(1+(2*3)+((8)/4))+1"
assert sol.maxDepth(s) == 3

s = "(1)+((2))+(((3)))"
assert sol.maxDepth(s) == 3
