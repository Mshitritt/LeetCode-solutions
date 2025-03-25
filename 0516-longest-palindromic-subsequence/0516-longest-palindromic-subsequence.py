class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        Solving by LCS algorithem 
        take s and reverse s and run LCS
        """
        rv = s[::-1]
        n = len(s)

        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        for r in range(1, n + 1):
            l1 = s[r-1]
            for c in range(1, n + 1):
                l2 = rv[c-1]
                if l1 == l2:
                    dp[r][c] = 1 + dp[r-1][c-1]
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        return dp[n][n]
