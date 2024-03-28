from typing import List
from collections import Counter


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # We are going to use two pointers (sliding window)
        left = 0
        counter = Counter()  # Count the frequency of each item
        max_ = 0  # Store the length of the longest sub-array

        # Go through all the elements in nums
        for right, num in enumerate(nums):
            counter[num] += 1  # increment the frequency of the current

            # If the frequency of current element is bigger than K
            while counter[num] > k:
                # Decrement the frequency of the left-most item
                # and move the left index one element to the right
                counter[nums[left]] -= 1
                left += 1

            # Check whether we have a new maximum
            # (right - left + 1) is the length of the current window
            max_ = max(max_, right - left + 1)

        return max_


sol = Solution()

nums = [1, 2, 3, 1, 2, 3, 1, 2]
k = 2
output = sol.maxSubarrayLength(nums=nums, k=k)
expected = 6
assert output == expected

nums = [1, 2, 1, 2, 1, 2, 1, 2]
k = 1
output = sol.maxSubarrayLength(nums=nums, k=k)
expected = 2
assert output == expected


nums = [5, 5, 5, 5, 5, 5, 5]
k = 4
output = sol.maxSubarrayLength(nums=nums, k=k)
expected = 4
assert output == expected
