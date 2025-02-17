class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        rows, cols = len(grid), len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    tempRes = 0
                    grid[r][c] = 0
                    q.append([r, c])
                    while q:
                        tempRes += 1
                        cur_r, cur_c = q.pop()

                        for dr, dc in directions:
                            new_r, new_c = cur_r + dr, cur_c + dc
                            if 0 <= new_r < rows and 0 <= new_c < cols:
                                if grid[new_r][new_c] == 1:
                                    q.append([new_r, new_c])
                                    grid[new_r][new_c] = 0
                    res = max(res, tempRes)
        return res

