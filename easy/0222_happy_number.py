class Solution:
    def isHappy(self, n: int) -> bool:
        memory = set()

        while n not in memory:
            memory.add(n)
            n = sum(int(s) ** 2 for s in list(str(n)))

        return 1 in memory


sol = Solution()
assert sol.isHappy(19) is True
assert sol.isHappy(2) is False
