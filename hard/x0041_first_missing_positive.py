# This solution doesn't meet the requiere constraint of using O(1) space.

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # In worst-case scenario, the smallest positive integer that
        # is not present in nums would be n + 1, so we just need to
        # store n boolean values.
        n = len(nums)
        seen = [False] * n

        # For each number in the list, check whether the number is
        # greater than 0 (we don't care about negative values) or smaller than n (we don't care about big numbers either).
        for num in nums:
            if 0 < num <= n:
                # The index starts at 0, so we must subtract 1
                seen[num - 1] = True

        # Go through the seen list, and return the index of the first
        # unseen number
        for i, s in enumerate(seen):
            if not s:
                # Remember the index starts at zero, so we must add 1
                return i + 1

        # If all numbers in the list were seen, return the following
        # number that should be in the list (n + 1)
        return n + 1


sol = Solution()
nums = [1, 2, 0]
expected = 3
output = sol.firstMissingPositive(nums)
assert expected == output

nums = [3, 4, -1, 1]
expected = 2
output = sol.firstMissingPositive(nums)
assert expected == output

nums = [7, 8, 9, 11, 12]
expected = 1
output = sol.firstMissingPositive(nums)
assert expected == output

nums = [5, 1, 2, 3, 4]
expected = 6
output = sol.firstMissingPositive(nums)
assert expected == output
