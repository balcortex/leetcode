class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # We'll keep an stack of the indices of open parentheses
        stack_open = []

        # The output list have empty placeholders for each character
        # of the original string
        out_lst = [""] * len(s)

        # Go through all indices and characters of the string
        for index, char in enumerate(s):
            # If we encounter an open parentheses, add its index to
            # the stack
            if char == "(":
                stack_open.append(index)

            # If we encounter a closing parentheses, check if we have
            # a pair (an open parentheses in the stack)
            # If we have a pair, add both at the correspondent index
            elif char == ")":
                if stack_open:
                    out_lst[stack_open.pop()] = "("
                    out_lst[index] = ")"

            # All other characters will be added directly to the list
            else:
                out_lst[index] = char

        # The non-filled empty placeholders will be omitted in the
        # the final result
        return "".join(out_lst)


sol = Solution()

s = "lee(t(c)o)de)"
expected = "lee(t(c)o)de"
assert sol.minRemoveToMakeValid(s) == expected

s = s = "a)b(c)d"
expected = "ab(c)d"
assert sol.minRemoveToMakeValid(s) == expected

s = "))(("
expected = ""
assert sol.minRemoveToMakeValid(s) == expected
