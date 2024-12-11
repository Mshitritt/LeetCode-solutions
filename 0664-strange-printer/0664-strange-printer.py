class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single character substrings
        for i in range(n):
            dp[i][i] = 1
        
        # Process substrings of increasing length
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                dp[l][r] = dp[l+1][r] + 1  # Initial case: print s[l] separately
                for k in range(l + 1, r + 1):
                    if s[l] == s[k]:
                        dp[l][r] = min(dp[l][r], dp[l+1][k-1] + dp[k][r])
        
        return dp[0][n-1]

        

