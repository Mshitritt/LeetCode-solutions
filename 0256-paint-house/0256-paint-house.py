class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = {} # (color_0, color_1, color_2)
        dp[0] = (costs[0][0], costs[0][1], costs[0][2])
        def dfs(n):
            if n == 0:
                return dp[0]
            dfs(n-1)
            
            c0 = costs[n][0] + min(dp[n-1][1], dp[n-1][2])
            c1 = costs[n][1] + min(dp[n-1][0], dp[n-1][2])
            c2 = costs[n][2] + min(dp[n-1][1], dp[n-1][0])
            dp[n] = (c0, c1, c2)
            return dp[n]

        dfs(len(costs)-1)    
        return min(dp[len(costs)-1])
        """
        # Brute force
        def rec(n, prev):
            if n < 0:
                return 0
            res = float('inf')
            for c in range(3):
                if c != prev:
                    res = min(res, costs[n][c] + rec(n-1, c))
            return res
        n = len(costs)-1
        return min(rec(n, 0), rec(n, 1), rec(n, 2))
        """

