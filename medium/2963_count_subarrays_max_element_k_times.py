from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # We will use a sliding windows with two pointers
        left = 0
        max_n = max(nums)
        count = 0
        num_arrays = 0

        for num in nums:
            count += num == max_n
            while count >= k:
                count -= nums[left] == max_n
                left += 1

            num_arrays += left

        return num_arrays


sol = Solution()

nums = [1, 3, 2, 3, 3]
k = 2
expected = 6
output = sol.countSubarrays(nums=nums, k=k)
assert expected == output
