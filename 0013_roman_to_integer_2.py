class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        sum_ = 0

        for a, b in zip(s, s[1:]):
            a, b = roman[a], roman[b]
            value = a if a >= b else -a
            sum_ += value

        return sum_ + roman[s[-1]]


solution = Solution()
solution.romanToInt("MCMXCIV")
