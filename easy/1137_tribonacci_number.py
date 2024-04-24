class Solution:
    # Use cache to improve speed
    dic = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        # If we already calculated the `nth` value, return it
        if n in self.dic:
            return self.dic[n]

        # Get and store the `nth` value calling recursively
        self.dic[n] = (
            self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        )

        return self.dic[n]


sol = Solution()
assert sol.tribonacci(4) == 4
assert sol.tribonacci(25) == 1389537
