class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # lps
        n = len(s)
        lps = [0]*n
        j = 0  # length of previous longest prefix suffix
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
                lps[i] = j
        return True if lps[-1] > 0 and n % (n - lps[-1]) == 0 else False