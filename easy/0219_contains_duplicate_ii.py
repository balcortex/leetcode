from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Store seen nums and their indices
        dic = {}

        # Loop through all the numbers in the list
        for i, num in enumerate(nums):
            # If the num is already in the dic (is already seen it before)
            # and the distance between the current index and the index of the
            # same number the last time seen is less or equal to k, return True
            # Note: we do not need abs() because the current index will always
            # be bigger than the index of the lastly seen number.
            if num in dic and (i - dic[num]) <= k:
                return True

            # If it is the first time we see the number, add it to the dic
            dic[num] = i

        # If we pass the for cycle without finding a duplicate, that means
        # there isn't one.
        return False


sol = Solution()
assert sol.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3) is True
assert sol.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1) is True
assert sol.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2) is False
