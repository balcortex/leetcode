class Solution:
    def checkValidString(self, s: str) -> bool:
        # Will make use of two stacks, one to keep track open parentheses `(`
        # indices, and the other to keep track the star `*` indices.
        stack = []
        star = []

        # Go through all elements in the string `s`
        for index, char in enumerate(s):
            # If we encounter an open parentheses, add the index to the stack
            if char == "(":
                stack.append(index)

            # If we encounter a closing parentheses `)`
            elif char == ")":
                # First check if there is a matching `(`, and if it is,
                # remove the index
                if stack:
                    stack.pop()
                # If we don't have an open parentheses, check for a star
                elif star:
                    star.pop()
                # If we don't have matching pair for the closing
                # parentheses, return False
                else:
                    return False

            # If we encounter an star `*`, add the index to the star list
            else:
                star.append(index)

        # We already matched the closing parentheses `)`, so let's now match
        # the opening ones (if there's any)
        # First we need to check if we have any index of an open parentheses,
        # and any index of star characters
        # (Remember that stars can be used as empty strings, so it does not
        # matter if there are some left in the star list)
        while star and stack:
            # Also, we need to check if the combination is valid (i.e., the
            # opening bracket must be before the star)
            if stack.pop() > star.pop():
                return False

        # If the stack of opening parentheses is empty, return True
        return len(stack) == 0


sol = Solution()

s = "()"
assert sol.checkValidString(s) is True

s = "(*))"
assert sol.checkValidString(s) is True

s = "(*)"
assert sol.checkValidString(s) is True

s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
assert sol.checkValidString(s) is True
