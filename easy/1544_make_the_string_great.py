class Solution:
    def makeGood(self, s: str) -> str:
        # Will use a list to keep track of 'good' characters
        good = []

        # Go through all characters in the string
        for char in s:
            # If the current character is the same character at the tail of
            # the list, with swapped case, then remove both from the list
            if good and char.swapcase() == good[-1]:
                good.pop()
                continue

            # If both the current and the last characters are good, add the
            # current to the list
            good.append(char)

        # Return a string from the `good` list
        return "".join(good)


sol = Solution()

s = "leEeetcode"
expected = "leetcode"
assert sol.makeGood(s) == expected

s = "s"
expected = "s"
assert sol.makeGood(s) == expected

s = "abBAcC"
expected = ""
assert sol.makeGood(s) == expected
