class Solution:
    def longestPrefix(self, s: str) -> str:
        # lps 
        n = len(s)
        lps = [0]*n
        i, j = 1, 0

        while i < n:
            if s[i] == s[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j == 0:
                    lps[i] = 0
                    i += 1
                else:
                    j = lps[j-1]
        if lps[-1]:
            return s[:lps[-1]]
        return ""
