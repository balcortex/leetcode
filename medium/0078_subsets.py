from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Start with a list of lists
        # Every set (even an empty one) has an empty one as a subset
        sets = [[]]

        # For each number in the `nums` list
        for num in nums:
            # Take each subset already in the `sets` variable, and add to it
            # the current number
            new_subsets = [set_ + [num] for set_ in sets]

            # Then, add these new subsets to the `sets` variable
            sets += new_subsets

        return sets


sol = Solution()
nums = [1, 2, 3]
output = sol.subsets(nums)
expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
assert output == expected
