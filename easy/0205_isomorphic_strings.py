class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Make a mapping dictionary
        dic = dict(zip(list(s), list(t)))

        # Different characters cannot map to the same value,
        # so we remove the keys with the same value by swapping
        # the key,values into another dictionary
        dic2 = {v: k for k, v in dic.items()}

        # Get the original dictionary again, without duplicate values
        dic = {v: k for k, v in dic2.items()}

        # Map the string `s` to a new string, using the mapping
        mapped = "".join(dic.get(ch, " ") for ch in s)

        # Check if the result string is the same as the string `t`
        return mapped == t


sol = Solution()
assert sol.isIsomorphic("egg", "add") is True
assert sol.isIsomorphic("foo", "bar") is False
assert sol.isIsomorphic("paper", "title") is True
assert sol.isIsomorphic("badc", "baba") is False
