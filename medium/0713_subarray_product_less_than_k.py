from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # We will use two pointers to create a sliding window
        left = 0  # left of the sliding window
        prod = 1  # variable to store the product of the current window
        count = 0  # number of subarrays that met the conditions

        # Loop through all the elements in the array
        # right is the index that defines the end of the window
        for right, num in enumerate(nums):
            prod *= num  # add the current number to the accumulated product

            # If the product is greater than k, we increment the left index by 1
            # Also we must make sure the left index is not bigger than the right
            while prod >= k and left <= right:
                prod /= nums[left]  # remove the left-most item from the product
                left += 1

            # This is the trickiest part
            # Every time we add a number to the sliding window that meets the
            # requirements, we also want to add the subarrays of this window.
            # Example:
            # Suppose the sliding window is [5, 2, 6], being 6 the last added,
            # Then, if [5, 2, 6] is smaller than K, that means that [2, 6] and
            # [6] is also smaller than K. So in this case we want to add 3 to
            # the subarray count.
            count += right - left + 1

        return count


sol = Solution()

nums = [10, 5, 2, 6]
k = 100
expected = 8
output = sol.numSubarrayProductLessThanK(nums, k)
assert expected == output


nums = [1, 2, 3]
k = 0
expected = 0
output = sol.numSubarrayProductLessThanK(nums, k)
assert expected == output
