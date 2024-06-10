from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Start by storing the first element as the max
        res = max_prod = min_prod = nums[0]

        # Traverse all the elements of nums, starting at the second index
        for i, num in enumerate(nums[1:]):
            # We have 3 cases where a new maximum can be obtained:
            # a) The product is positive and the next number is positive
            # b) The product is negative and the next number is negative
            # c) The product is zero and the next number is positive

            # Calculate the new maximum based on the 3 cases above
            max_temp = max(num, max_prod * num, min_prod * num)
            # Calculate the new minimum based on the 3 cases above
            min_prod = min(num, min_prod * num, max_prod * num)
            # We need a temp variable to not make use of the new updated max
            max_prod = max_temp

            # Maximum between the current maximum and the possible new maximum
            res = max(max_prod, res)

        return res


sol = Solution()
assert sol.maxProduct([2, 3, -2, 4]) == 6
assert sol.maxProduct([-2, 0, -1]) == 0
