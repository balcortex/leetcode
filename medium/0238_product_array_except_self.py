from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for n in nums:
            prod *= n

        a = [prod / n if n != 0 else prod for n in nums]
        print(a)
        return [prod / n if n != 0 else prod for n in nums]


sol = Solution()
assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
