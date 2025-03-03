class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for r in range(1, rows+1):
            for c in range(1, cols+1):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r][c-1], dp[r-1][c])
        for r in dp:
            print(r)
        return dp[rows][cols]
        
        


