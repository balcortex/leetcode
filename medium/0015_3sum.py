from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the numbers to use the two-pointer approach
        nums.sort()

        n = len(nums)  # length of the nums list
        triplets = []  # store the triplets here

        for left in range(n):
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            mid = left + 1  # mid starts one index to the right of `left`
            right = n - 1  # right starts at the end

            # Move both indices until they meet
            while mid < right:
                sum_ = nums[left] + nums[mid] + nums[right]

                # If the sum == 0, add the numbers to the triplet
                if sum_ == 0:
                    triplets.append([nums[left], nums[mid], nums[right]])
                    # Avoid checking repeated numbers
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    mid += 1
                    right -= 1

                # If the sum > 0, move `right`` one position to the left
                # Remember that the nums list is sorted
                if sum_ > 0:
                    right -= 1

                # If the sum < 0, move `mid` one position to the right
                if sum_ < 0:
                    mid += 1

        # The solution requires a list of lists as output
        return triplets


sol = Solution()

nums = [-1, 0, 1, 2, -1, -4]
output = sol.threeSum(nums)
expected = [[-1, -1, 2], [-1, 0, 1]]
assert output.sort() == expected.sort()

nums = [0, 1, 1]
output = sol.threeSum(nums)
expected = []
assert output.sort() == expected.sort()

nums = [0, 0, 0]
output = sol.threeSum(nums)
expected = [[0, 0, 0]]
assert output.sort() == expected.sort()
