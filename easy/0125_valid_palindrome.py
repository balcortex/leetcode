class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = [char for char in s.lower() if char.isalnum()]
        return alphanum == alphanum[::-1]


sol = Solution()
assert True == sol.isPalindrome("A man, a plan, a canal: Panama")
assert False == sol.isPalindrome("race a car")
assert True == sol.isPalindrome(" ")
