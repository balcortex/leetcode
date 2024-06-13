class Solution:
    def reorderSpaces(self, text: str) -> str:
        # Separate the text into words, deleting all spaces between words
        words = text.strip().split()
        # Need the number of spaces in the actual string
        num_spaces = text.count(" ")

        # Corner case, just 1 word exists
        # Add all the present spaces at the end (including none)
        if len(words) == 1:
            return "".join(words) + " " * num_spaces

        # Calculate the gap length between words
        # And take into account any extra spaces (the number is not divisible)
        gap, extra_space = divmod(num_spaces, len(words) - 1)

        # Return the words with a gap of `gap` spaces between
        # And a possibly extra spaces at the end
        return (" " * gap).join(words) + " " * extra_space


sol = Solution()

text = "  this   is  a sentence "
output = sol.reorderSpaces(text)
expected = "this   is   a   sentence"
assert output == expected

text = " practice   makes   perfect"
output = sol.reorderSpaces(text)
expected = "practice   makes   perfect "
assert output == expected
