class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(points[0]))] for _ in range(3)]
        # dp[0] = val
        # dp[1] = left
        # dp[2] = right
        dp[0] = points[0].copy()

        for r in range(1, len(points)):
            # fill left 
            for c in range(len(points[0])):
                if c == 0:
                    dp[1][c] = dp[0][c]
                else:
                    dp[1][c] = max(dp[1][c-1]-1, dp[0][c])
            
            # fill right 
            for c in range(len(points[0])-1, -1, -1):
                if c == len(points[0])-1:
                    dp[2][c] = dp[0][c] 
                else:
                    dp[2][c] = max(dp[2][c+1]-1, dp[0][c])
                
                # fill val 
                dp[0][c] = max(dp[1][c], dp[2][c]) + points[r][c]
        return max(dp[0])
