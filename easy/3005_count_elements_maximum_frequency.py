from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = Counter(nums)
        max_ = dic[max(dic, key=dic.get)]

        return sum(v for k, v in dic.most_common() if v == max_)


sol = Solution()
assert sol.maxFrequencyElements([1, 2, 2, 3, 1, 4]) == 4
assert sol.maxFrequencyElements([1, 2, 3, 4, 5]) == 5
