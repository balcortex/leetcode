class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])


sol = Solution()

s = "Hello World"
assert sol.lengthOfLastWord(s) == 5

s = "   fly me   to   the moon  "
assert sol.lengthOfLastWord(s) == 4

s = "luffy is still joyboy"
assert sol.lengthOfLastWord(s) == 6
