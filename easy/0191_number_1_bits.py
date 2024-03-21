class Solution:
    def hammingWeight(self, n: int) -> int:
        return format(n, "b").count("1")


sol = Solution()
assert sol.hammingWeight(11) == 3
assert sol.hammingWeight(3) == 2
assert sol.hammingWeight(4) == 1
