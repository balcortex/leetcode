from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # First we count the occurrences of even characters,
        # (if a character appears 7 times, we only count to 6)
        # And if there's any even character left (we just need one),
        # we add it at the end.

        # We'll use a counter dict to store the frequency
        dic = Counter(s)
        longest = 0

        # Iterate over the characters and their frequency
        for k, v in dic.items():
            # divmod returns the quotient (x // y) and the remainder (x % y)
            quot, rem = divmod(v, 2)
            # We want to count the number of occurrences of even numbers,
            # so we obtain the quotient and multiply by 2
            longest += quot * 2
            # We want to keep track of the remainder to see if there's any odd freq
            dic[k] = rem

        # Return the sum of all even chars + 1 if there's an even char left
        return longest + any(dic.values())


sol = Solution()
assert sol.longestPalindrome("abccccdd") == 7
assert sol.longestPalindrome("a") == 1
