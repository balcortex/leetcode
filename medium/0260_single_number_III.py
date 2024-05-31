from typing import List
from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # First apply the XOR to the whole list.
        # The result will be the XOR of the two numbers we are searching for
        num1_xor_num2 = reduce(xor, nums, 0)

        # The mask will give us the bits where the two numbers are different
        # We want to select any bit that is set to 1
        # There is an easy way to obtain the lowest set bit, so we'll use that formula
        mask = num1_xor_num2 & (-num1_xor_num2)

        # Now the mask indicates the first bit where the two numbers are different
        # We can split the original list into two lists:
        # one where the numbers share this set bit, and other where they don't
        # Let's select the former group
        num1 = reduce(xor, [n for n in nums if n & mask != 0], 0)

        # The second number is obtained num1 ^ num1_xor_num2
        return [num1, xor(num1, num1_xor_num2)]


sol = Solution()
nums = [1, 2, 1, 3, 2, 5]
output = sol.singleNumber(nums)
expected = [3, 5]
assert output == expected

nums = [-1, 0]
output = sol.singleNumber(nums)
expected = [-1, 0]
assert output == expected

nums = [0, 1]
output = sol.singleNumber(nums)
expected = [1, 0]
assert output == expected
