from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # # SOLUTION 1 - - - - - - - - - - - - - - - - - - - - - - - -
        # # With frequency counter

        # # Count the number of times each number appears in arr1
        # freq = Counter(arr1)

        # # Create an empty an array
        # arr3 = []
        # # Traverse trough the items in 2 (in the given order)
        # for n in arr2:
        #     # Extend the arr3 array with a list containing the number n
        #     # repeated freq[n] times
        #     arr3.extend([n] * freq[n])

        # # Finally add the (sorted) items that don't appear in arr2
        # return arr3 + sorted(n for n in arr1 if n not in arr2)
        # # - - - - - - - - - - - - - - - - - - - - - - - - - - -

        # # SOLUTION 2 - - - - - - - - - - - - - - - - - - - - - - - -
        # # Sorting with k

        # Create a dict containing the number and the index at which appear
        dic = {k: v for v, k in enumerate(arr2)}

        # Sort the arr1 array using the dic created above
        # If the dictionary contains the key (the number is present in arr2),
        # return its position on the arr2.
        # If the item is not in the dict (the number is not in arr2),
        # return a big number plus the actual number.
        # For example 7 will return 1007, and 9 will return 1009,
        # maintaining the ascending order.
        arr1.sort(key=lambda a: dic.get(a, 1000 + a))
        return arr1
        # # - - - - - - - - - - - - - - - - - - - - - - - - - - -


sol = Solution()

arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
output = sol.relativeSortArray(arr1, arr2)
expected = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
assert output == expected

arr1 = [28, 6, 22, 8, 44, 17]
arr2 = [22, 28, 8, 6]
output = sol.relativeSortArray(arr1, arr2)
expected = [22, 28, 8, 6, 17, 44]
assert output == expected
