from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sorted(nums, key=nums.copy().count)[0]


sol = Solution()
assert sol.singleNumber([2, 2, 1]) == 1
assert sol.singleNumber([4, 1, 2, 1, 2]) == 4
assert sol.singleNumber([1]) == 1
