from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # We'll use two pointers, one for each list
        idx1 = idx2 = 0

        # Variables to store the current number in the loop
        m1 = m2 = 0

        n1 = len(nums1)
        n2 = len(nums2)

        # Iterate until we have covered the combined half of both arrays
        for _ in range((n1 + n2) // 2 + 1):
            # We need to store the previous value in case the length of the
            # combined array is odd
            m2 = m1

            # If both indices are smaller than the correspondent lengths,
            # check the values on both lists
            if idx1 < n1 and idx2 < n2:

                # If the value of list1 is smaller than list2
                # save the value and increment the pointer 1
                if nums1[idx1] < nums2[idx2]:
                    m1 = nums1[idx1]
                    idx1 += 1
                # In other case, increment the pointer on list 2 and save that value
                else:
                    m1 = nums2[idx2]
                    idx2 += 1

            # If we don't have more values on list 1, work only with the list 2
            elif idx1 == n1:
                m1 = nums2[idx2]
                idx2 += 1
            # and viceversa
            else:
                m1 = nums1[idx1]
                idx1 += 1

        # If the length of the combined list is odd, we just need to return the
        # value in the middle (a.k.a. m1)
        if (n1 + n2) % 2 == 1:
            return m1 * 1.0
        # Else, the length is even, so we need the two middle values (m1 and m2)
        return (m1 + m2) / 2.0


sol = Solution()
nums1 = [1, 3]
nums2 = [2]
expected = 2.0
assert sol.findMedianSortedArrays(nums1, nums2) == expected

nums1 = [1, 2]
nums2 = [3, 4]
expected = 2.5
assert sol.findMedianSortedArrays(nums1, nums2) == expected
