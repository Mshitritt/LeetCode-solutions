class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Solving by LCS algorithem 
        take s and reverse s and run LCS
        """
        dp = {}

        def LCS(i1, i2):
            if i1 >= n or i2 >= n:
                return 0
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            
            if s1[i1] == s2[i2]:
                dp[(i1, i2)] = LCS(i1+1, i2+1) + 1
                return dp[(i1, i2)]
            else:
                lcs1 = LCS(i1+1, i2)
                lcs2 = LCS(i1, i2+1)
                dp[(i1, i2)] = max(lcs1, lcs2)
                return dp[(i1, i2)]
        
        n = len(s)
        s1 = s
        s2 = s[::-1]
        return LCS(0, 0)
