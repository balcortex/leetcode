from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1] * n  # prefix sum
        right = [1] * n  # postfix sum

        # Start at second element
        # the first element does not have any numbers to the left
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        # Start at the second element from the end
        for i in range(-2, -n - 1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # The solution is prefix[i] * postfix[i]
        return [l * r for (l, r) in zip(left, right)]


sol = Solution()

assert sol.productExceptSelf([2, 3, 4, 5, 6]) == [360, 240, 180, 144, 120]
assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
