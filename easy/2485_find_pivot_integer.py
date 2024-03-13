class Solution:
    def pivotInteger(self, n: int) -> int:

        for pivot in range(1, n + 1):
            left_sum = sum(range(1, pivot + 1))
            right_sum = sum(range(pivot, n + 1))
            if left_sum == right_sum:
                return pivot

        return -1


sol = Solution()
assert sol.pivotInteger(8) == 6
assert sol.pivotInteger(1) == 1
assert sol.pivotInteger(4) == -1
