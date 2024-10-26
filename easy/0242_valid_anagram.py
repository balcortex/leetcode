from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Use a counter to get the letter count of each string and compare if
        # they are equal
        return Counter(s) == Counter(t)


sol = Solution()

s = "anagram"
t = "nagaram"
expected = True
assert sol.isAnagram(s, t) == expected

s = "rat"
t = "car"
expected = False
assert sol.isAnagram(s, t) == expected

s = "aa"
t = "a"
expected = False
assert sol.isAnagram(s, t) == expected

s = "aacc"
t = "ccac"
expected = False
assert sol.isAnagram(s, t) == expected
