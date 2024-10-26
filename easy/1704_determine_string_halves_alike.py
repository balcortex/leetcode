class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Make a hash map to access the vowels
        vow_set = set("aeiouAEIOU")

        # Split the string into two halves the same size
        half1 = s[: len(s) // 2]
        half2 = s[len(s) // 2 :]

        # Count the number of vowels in each one
        count1 = sum(1 for ch in half1 if ch in vow_set)
        count2 = sum(1 for ch in half2 if ch in vow_set)

        return count1 == count2


sol = Solution()

assert sol.halvesAreAlike("book") is True
assert sol.halvesAreAlike("textbook") is False
