class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # bfs solution 

        """
        # Valid - can do better 
        cols = len(grid[0])
        rows = len(grid)
        dp = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]
        directions = [(-1, 0), (0, -1)]
        def rec(m, n):
            if m == 0 and n == 0:
                return dp[0][0]
            else:
                for dr, dc in directions:
                    r = m + dr
                    c = n + dc
                    if 0 <= r < rows and 0 <= c < cols:
                        if dp[r][c] == float('inf'):
                            dp[m][n] = min(dp[m][n], grid[m][n] + rec(r, c))
                        else:
                            dp[m][n] = min(dp[m][n], grid[m][n] + dp[r][c])
                return dp[m][n]
                    
        
        rec(rows-1, cols-1)
        for r in dp:
            print(r)
        return dp[rows-1][cols-1]
        """
        dp = [0 for _ in range(len(grid[0]))]
        print(dp)
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[j] = grid[i][j] + dp[j + 1]
                elif j == len(grid[0]) - 1 and i != len(grid) - 1:
                    dp[j] = grid[i][j] + dp[j]
                elif i != len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[j] = grid[i][j] + min(dp[j], dp[j + 1])
                else:
                    dp[j] = grid[i][j]
            print(dp)
        return dp[0]
        

