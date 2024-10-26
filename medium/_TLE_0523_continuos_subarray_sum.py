from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Using a sliding window approach, start with leftmost element
        for left in range(len(nums) - 1):
            # Add the leftmost element to the sum
            sum_ = nums[left]

            # Iterate over the left of the list starting at [left + 1]
            for right in range(left + 1, len(nums)):
                # Add each element to the sum
                sum_ += nums[right]

                # If the sum is divisible by k, return True
                if sum_ % k == 0:
                    return True

        # If no sub-array divisible by k was found, return False
        return False


sol = Solution()

nums = [23, 2, 4, 6, 7]
k = 6
output = sol.checkSubarraySum(nums, k)
expected = True
assert output == expected

nums = [23, 2, 6, 4, 7]
k = 6
output = sol.checkSubarraySum(nums, k)
expected = True
assert output == expected

nums = [23, 2, 6, 4, 7]
k = 13
output = sol.checkSubarraySum(nums, k)
expected = False
assert output == expected
