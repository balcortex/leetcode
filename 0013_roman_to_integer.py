symbol = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    "a": 4,
    "b": 9,
    "c": 40,
    "d": 90,
    "e": 400,
    "f": 900,
}


class Solution:
    def __init__(self) -> None:
        pass

    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "a")
        s = s.replace("IX", "b")
        s = s.replace("XL", "c")
        s = s.replace("XC", "d")
        s = s.replace("CD", "e")
        s = s.replace("CM", "f")

        print(s)

        return sum(int(symbol[c]) for c in s)


solution = Solution()
solution.romanToInt("MCMXCIV")
