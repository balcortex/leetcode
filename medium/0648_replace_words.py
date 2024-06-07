from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # Sort the words by length (from the smallest to the longest)
        dictionary.sort(key=len)

        # Store the current word
        out = []

        # For each word in the sentence
        for s in sentence.split(" "):
            # Check against the words in the dictionary
            for t in dictionary:
                # If there's  match, append the word in the dictionary
                # and continue to the next word in the sentence
                if s.startswith(t):
                    out.append(t)
                    break
            # If no words were found in the dictionary, append the actual word
            else:
                out.append(s)

        return " ".join(out)


sol = Solution()

dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
out = sol.replaceWords(dictionary, sentence)
expected = "the cat was rat by the bat"
assert out == expected

dictionary = ["a", "b", "c"]
sentence = "aadsfasf absbs bbab cadsfafs"
out = sol.replaceWords(dictionary, sentence)
expected = "a a b c"
assert out == expected
