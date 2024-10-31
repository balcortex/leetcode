class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        exp = 0
        m = 1  # Start with 2^0 = 1
        while m <= n:
            if m == n:
                return True
            exp += 1
            m = 2**exp
        return False


sol = Solution()

assert sol.isPowerOfTwo(1) is True
assert sol.isPowerOfTwo(16) is True
assert sol.isPowerOfTwo(3) is False
