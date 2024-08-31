class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        merge_lst = []
        while i < min(len(word1), len(word2)):
            merge_lst.append(word1[i] + word2[i])
            i += 1

        merge_lst.append(word1[i:])
        merge_lst.append(word2[i:])
        return ''.join(merge_lst)