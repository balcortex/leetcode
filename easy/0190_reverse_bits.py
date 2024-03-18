class Solution:
    def reverseBits(self, n: int) -> int:
        # First convert to binary and add padding to left
        # The string must be 32 bits
        bin_ = format(n, "b").zfill(32)

        # Reverse the bits and convert it to int
        return int(bin_[::-1], 2)


sol = Solution()
assert sol.reverseBits(43261596) == 964176192
assert sol.reverseBits(4294967293) == 3221225471
