class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(1+len(word1))] for _ in range(1+len(word2))]
        rows, cols = len(word2), len(word1)
        
        for c in range(1, cols+1):
            dp[0][c] = dp[0][c-1] + 1
        for r in range(1, rows+1):
            dp[r][0] = dp[r-1][0] + 1
        
        for r in range(1, rows+1):
            for c in range(1, cols+1):
                w1, w2 = word1[c-1], word2[r-1]
                if w1 == w2:
                    dp[r][c] = dp[r-1][c-1]  # No operation needed, take diagonal value
                else:
                    op1 = 1 + dp[r][c-1]    # insert
                    op2 = 1 + dp[r-1][c]    # delete
                    op3 = 1 + dp[r-1][c-1]  # replace
                    dp[r][c] = min(op1, op2, op3)
                            
        return dp[rows][cols]
                    


