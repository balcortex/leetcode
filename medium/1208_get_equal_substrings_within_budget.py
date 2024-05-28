class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # We will use a sliding window approach

        left = 0  # Left index of the window
        cur_cost = 0  # Cumulative cost of converting the substring
        max_len = 0  # Maximum length of the possible substring

        # Iterate over the indices of the string
        for right in range(len(s)):
            # Add the cost of converting the char at pos[i]
            cur_cost += abs(ord(s[right]) - ord(t[right]))

            # If the cost is greater, delete the leftmost element
            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1

            # Keep track of the maximum and the window length
            max_len = max(max_len, right - left + 1)

        return max_len


sol = Solution()
assert sol.equalSubstring("abcd", "bcdf", maxCost=3) == 3
assert sol.equalSubstring("abcd", "cdef", maxCost=3) == 1
assert sol.equalSubstring("abcd", "acde", maxCost=0) == 1
