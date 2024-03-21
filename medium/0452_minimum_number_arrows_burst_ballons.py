from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # Sort by second item
        points_sort = sorted(points, key=lambda pair: pair[1])

        # Start by shooting an arrow and save the position of the last element
        arrows = 1
        cur_last = points_sort[0][1]

        # Loop through all the pairs
        for first, last in points_sort:
            # If the first element of the current pair is less or equal to
            # our current last element, that means the balloon is already
            # popped, so skip to the next ballon.
            if first <= cur_last:
                continue

            # If the first element is greater than our current last element,
            # we need a new arrow. And to store the last position as our new
            # current last.
            arrows += 1
            cur_last = last

        return arrows


sol = Solution()
assert sol.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 16]]) == 2
assert sol.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
assert sol.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
