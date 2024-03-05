class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        numbers = []
        idx = -1
        for num in [
            number,
        ] * number.count(digit):
            idx = num.find(digit, idx + 1)
            a = list(num)
            a.pop(idx)
            numbers.append(int("".join(a)))

        return str(max(numbers))


sol = Solution()
print(sol.removeDigit("123", "3"))
print(sol.removeDigit("1231", "1"))
print(sol.removeDigit("551", "5"))
