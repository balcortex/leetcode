from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the numbers to use a two-pointer window
        nums.sort()

        n = len(nums)  # length of the nums list
        smallest_sum = 999999999  # the smallest sum found until now
        closest_dif = 999999999  # the difference between the sum and target

        # Loop through all elements (n - 2, because we need two additional idx)
        for left in range(n - 2):
            mid = left + 1  # start one position to the left of `left`
            right = n - 1  # start at the end

            # Until both indices meet
            while mid < right:
                current_sum = nums[left] + nums[mid] + nums[right]
                current_dif = abs(current_sum - target)

                # If the difference is 0, return the current_sum
                if current_dif == 0:
                    return current_sum

                # If we found a closest sum, update the variables
                if current_dif < closest_dif:
                    closest_dif = current_dif
                    smallest_sum = current_sum

                # If the sum is greater than the target, move the `right` idx
                # to the left, remember that the list is sorted
                if current_sum > target:
                    right -= 1

                # If the sum is smaller, move the `mid` idx one position to the right
                if current_sum < target:
                    mid += 1

        return smallest_sum


sol = Solution()

nums = [-1, 2, 1, -4]
target = 1
output = sol.threeSumClosest(nums, target)
expected = 2
assert output == expected

nums = [0, 0, 0]
target = 1
output = sol.threeSumClosest(nums, target)
expected = 0
assert output == expected
