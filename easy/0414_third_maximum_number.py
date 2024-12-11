from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        return nums[2] if len(nums) > 2 else nums[0]


sol = Solution()

assert sol.thirdMax([3, 2, 1]) == 1
assert sol.thirdMax([1, 2]) == 2
assert sol.thirdMax([2, 2, 3, 1]) == 1
