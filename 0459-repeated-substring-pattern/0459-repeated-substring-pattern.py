class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # lps
        n = len(s)
        lps = [0]*n
        j = 0
        i = 1
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
        return True if lps[-1] > 0 and n % (n - lps[-1]) == 0 else False