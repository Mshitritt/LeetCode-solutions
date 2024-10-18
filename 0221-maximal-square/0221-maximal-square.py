class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for c in range(len(matrix[0]))] for r in range(len(matrix))]
        larger = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0 or c == 0:
                    dp[r][c] = int(matrix[r][c])
                else:
                    if matrix[r][c] == "1":
                        dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
                    else:
                        dp[r][c] = 0
                larger = max(larger, int(dp[r][c]))
        
        return larger*larger

