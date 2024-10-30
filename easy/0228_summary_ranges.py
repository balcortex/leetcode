from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Check edge case
        if not nums:
            return []

        # Initialize the start of the current range and the result list
        start = 0
        result = []

        # Iterate through the list starting from the second element
        for end in range(1, len(nums)):
            # If the current number is not consecutive from the previous
            if nums[end] != nums[end - 1] + 1:
                # If the range has only one element, add it as a single number
                if start == end - 1:
                    result.append(str(nums[start]))
                # If the range has multiple elements, format it as "start->end"
                else:
                    result.append(f"{nums[start]}->{nums[end - 1]}")

                # Update start to the current position to begin a new range
                start = end

        # Add the last range to the result list
        # If only one number is left, add it as a single number
        if start == len(nums) - 1:
            result.append(str(nums[start]))
        # If multiple numbers are left, format the final range
        else:
            result.append(f"{nums[start]}->{nums[-1]}")

        return result


sol = Solution()

nums = [0, 1, 2, 4, 5, 7]
expected = ["0->2", "4->5", "7"]
assert sol.summaryRanges(nums) == expected

nums = [0, 2, 3, 4, 6, 8, 9]
expected = ["0", "2->4", "6", "8->9"]
assert sol.summaryRanges(nums) == expected

nums = []
expected = []
assert sol.summaryRanges(nums) == expected
