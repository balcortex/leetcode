class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return (
            len(set(pattern))
            == len(set(s.split()))
            == len(set(zip(pattern, s.split())))
        ) and len(pattern) == len(s.split())


sol = Solution()

assert sol.wordPattern("abba", "dog cat cat dog") is True
assert sol.wordPattern("abba", "dog cat cat fish") is False
assert sol.wordPattern("aaaa", "dog cat cat dog") is False
assert sol.wordPattern("abba", "dog dog dog dog") is False
assert sol.wordPattern("aba", "cat cat cat dog") is False
assert sol.wordPattern("aba", "dog cat cat") is False
