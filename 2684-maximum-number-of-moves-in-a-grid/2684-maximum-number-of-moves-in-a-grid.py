class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        #directions = [(1, -1), (0, -1), (-1, -1)]
        directions = [(-1, 1), (0, 1), (1, 1)]
        memo = {}

        def rec(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            max_moves = 0
            for dr, dc in directions:
                new_r, new_c = i+dr, j+dc
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if grid[new_r][new_c] > grid[i][j]:
                        max_moves = max(max_moves, 1 + rec(new_r, new_c))
            memo[(i, j)] = max_moves
            return memo[(i, j)]
        
        for i in range(rows):
            #memo[(i, 0)] = 0
            res = max(res, rec(i, 0))
        return res
            


                
                    

