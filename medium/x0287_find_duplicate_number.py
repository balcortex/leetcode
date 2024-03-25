from collections import Counter
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]


sol = Solution()
assert sol.findDuplicate([1, 3, 4, 2, 2]) == 2
assert sol.findDuplicate([3, 1, 3, 4, 2]) == 3
assert sol.findDuplicate([3, 3, 3, 3, 3]) == 3
