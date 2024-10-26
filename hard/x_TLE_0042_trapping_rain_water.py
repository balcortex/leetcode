from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # The water at height[i] can be calculated as:
        # min(max_left_height, max_right_height) - height[i]

        water = 0  # Store the accumulated water here
        n = len(height)  # Don't calculate this over and over again

        # Traverse all the elements, for each element find its correspondent
        # max_left_height and max_right_height
        for cur in range(n):

            # - - - Find maximum left - - - - - - - - - - - - - - - - -
            # If no maximum is found, let the max_left be the current idx
            # This way, the equation will end up giving 0 for the current idx
            max_left = cur
            for left in range(cur - 1, -1, -1):  # From cur to 0, steps of -1
                # If a new max_left_height is found, store the idx
                if height[left] > height[max_left]:
                    max_left = left
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

            # - - - Find maximum right - - - - - - - - - - - - - - - - -
            # If no maximum is found, let the max_right be the current idx
            max_right = cur
            for right in range(cur, n):  # From the cur idx until the end
                # If a new max_right_height is found, store the idx
                if height[right] > height[max_right]:
                    max_right = right
            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

            # Accumulate the water at each idx
            water += min(height[max_left], height[max_right]) - height[cur]

        return water


sol = Solution()

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
assert sol.trap(height) == 6

height = [4, 2, 0, 3, 2, 5]
assert sol.trap(height) == 9
