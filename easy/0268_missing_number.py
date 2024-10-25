from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = set(range(len(nums) + 1))
        b = set(nums)

        return list(a - b)[0]


sol = Solution()

nums = [3, 0, 1]
expected = 2
assert sol.missingNumber(nums) == expected

nums = [0, 1]
expected = 2
assert sol.missingNumber(nums) == expected

nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
expected = 8
assert sol.missingNumber(nums) == expected
