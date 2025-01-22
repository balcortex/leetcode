from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeros = nums.count(0)

        while zeros > 0:
            nums.remove(0)
            nums.append(0)
            zeros -= 1


sol = Solution()

nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)
expected = [1, 3, 12, 0, 0]
assert nums == expected

nums = [0]
sol.moveZeroes(nums)
expected = [0]
assert nums == expected
