from typing import List


def bubble_sort(nums: List[int]):
    n = len(nums)

    count = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            count += 1
            if nums[j] > nums[j + 1]:
                swapped = True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

        if not swapped:
            break

    print(count)
    return nums


nums = [4, 2, 5, 1, 3]
output = bubble_sort(nums)
expected = [1, 2, 3, 4, 5]
assert output == expected

nums = [2, 1, 3, 5, 4]
output = bubble_sort(nums)
expected = [1, 2, 3, 4, 5]
assert output == expected
