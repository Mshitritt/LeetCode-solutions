class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        prefix = [0]
        n = len(sentence)
        for i in range(1, n):
            if sentence[i] == ' ' and i+1 < n:
                prefix.append(i+1)
        
        words = 1
        for p in prefix:
            i = 0
            pi = p
            while pi < n and i < len(searchWord) and sentence[pi] == searchWord[i]:
                i += 1
                pi += 1
            if i == len(searchWord):
                return words
            else:
                words += 1
        return -1

            