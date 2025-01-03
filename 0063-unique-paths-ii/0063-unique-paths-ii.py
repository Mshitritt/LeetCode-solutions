class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if r == c == 0:
                    obstacleGrid[r][c] = 1
                else:
                    if obstacleGrid[r][c] == 1:
                        obstacleGrid[r][c] = 0
                    else:
                        left = obstacleGrid[r][c-1] if c-1>=0 else 0
                        up = obstacleGrid[r-1][c] if r-1 >=0 else 0
                        obstacleGrid[r][c] = left + up
        return obstacleGrid[-1][-1]
