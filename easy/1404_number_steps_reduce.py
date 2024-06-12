class Solution:
    def numSteps(self, s: str) -> int:

        # Convert the binary number to decimal
        num = int(s, 2)

        steps = 0
        while num != 1:
            if num % 2 == 0:
                num //= 2  # Use the integer division to avoid rounding errors
            else:
                num += 1
            steps += 1

        return steps


sol = Solution()

assert sol.numSteps("1101") == 6
assert sol.numSteps("10") == 1
assert sol.numSteps("1") == 0
assert sol.numSteps("1111011110000011100000110001011011110010111001010111110001") == 85
