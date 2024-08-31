class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merge = ""
        while i < min(len(word1), len(word2)):
            merge += word1[i] + word2[i]
            i += 1

        if word1[i:]:
            merge += word1[i:]
        else:
            merge += word2[i:]
        return merge