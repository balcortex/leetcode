from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Get the number (casted to int) from the list
        # and increase it by 1
        num = int("".join(map(str, digits))) + 1

        # Return a list of ints
        return [int(c) for c in str(num)]


sol = Solution()

digits = [1, 2, 3]
output = sol.plusOne(digits)
expected = [1, 2, 4]
assert output == expected

digits = [4, 3, 2, 1]
output = sol.plusOne(digits)
expected = [4, 3, 2, 2]
assert output == expected

digits = [9]
output = sol.plusOne(digits)
expected = [1, 0]
assert output == expected
