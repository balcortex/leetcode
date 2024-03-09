from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        intersect = set(nums1) & set(nums2)
        return min(intersect) if intersect else -1
