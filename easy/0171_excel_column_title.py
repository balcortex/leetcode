class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # ord(A) = 65, so we need to subtract 64
        transl = {char: ord(char) - 64 for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

        # Add (26 ^ i) to each character to convert from base 26 to decimal.
        # Start from the rightmost (least significant)
        return sum(
            transl[char] * 26**index
            for index, char in enumerate(columnTitle[::-1], start=0)
        )


sol = Solution()
assert sol.titleToNumber("A") == 1
assert sol.titleToNumber("AA") == 27
assert sol.titleToNumber("AB") == 28
assert sol.titleToNumber("ZY") == 701
