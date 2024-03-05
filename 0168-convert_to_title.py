class Solution:
    def convertToTitle(self, number: int) -> str:
        title = ""

        while number:
            number -= 1
            rem = number % 26
            title += chr(rem + 65)
            number = number // 26

        return title[::-1]


s = Solution()
assert s.convertToTitle(1) == "A"
assert s.convertToTitle(26) == "Z"
assert s.convertToTitle(27) == "AA"
assert s.convertToTitle(28) == "AB"
assert s.convertToTitle(701) == "ZY"
