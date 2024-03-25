from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # The numbers can only appear once or twice, and the range of the numbers
        # is guaranteed to be between 1 <= nums[i] <= length(nums).
        # So we can use the numbers as the index and the same list to store
        # the information.

        duplicates = []

        # We loop over all the items (indices) and change the number at index
        # [n-1] (include index 0) to its negative.
        # If the number at this index is already negative, the index number (n+1)
        # has appeared twice already.
        for num in nums:
            n = abs(num)  # The number might be already negative, take the absolute

            # If the number at this index is negative, we know we have seen it twice
            if nums[n - 1] < 0:
                duplicates.append(n)

            nums[n - 1] = -nums[n - 1]

        return duplicates


sol = Solution()

lst = [4, 3, 2, 7, 8, 2, 3, 1]
expected = [2, 3]
output = sol.findDuplicates(lst)
assert expected == output

lst = [1, 1, 2]
expected = [1]
output = sol.findDuplicates(lst)
assert expected == output

lst = [1]
expected = []
output = sol.findDuplicates(lst)
assert expected == output
