from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Make a list of number of trusts for each person
        # The first person starts at index 1, so use a length of (n + 1)
        trusted = [0] * (n + 1)

        # For each pair, decrease the trust of the first person
        # and increase the trust of the second person
        # (the judge is trusted by everybody except himself)
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1

        # Traverse the trusted list, started from the second element
        for i, t in enumerate(trusted[1:], start=1):
            # If any person has a trust of n - 1 (all the people except himself)
            # He is the judge, so return its index
            if t == (n - 1):
                return i

        # If nobody is found, return -1
        return -1


sol = Solution()
assert sol.findJudge(2, [[1, 2]]) == 2
assert sol.findJudge(3, [[1, 3], [2, 3]]) == 3
assert sol.findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1
assert sol.findJudge(1, []) == 1
