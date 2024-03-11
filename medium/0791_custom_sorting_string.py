class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Normal alphabetical order
        rankings = {k: ord(k) for k in "abcdefghijklmnopqrstuvwxyz"}

        # Change the alphabetical order.
        # We must iterate in reverse order so that the first element in the
        # order string has the most negative value
        for index, char in enumerate(order[::-1], start=1):
            rankings[char] -= index * 100

        return "".join(sorted(list(s), key=lambda char: rankings[char]))


sol = Solution()
assert sol.customSortString("cba", "abcd") == "cbad"
assert sol.customSortString("bcafg", "abcd") == "bcad"
