class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rotten = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append([r, c])
        
        dist = {}
        q = deque()
        for rot in rotten:
            dist[tuple(rot)] = 0
            q.append(rot)
        
        while q:
            curr = q.popleft()

            for dr, dc in directions:
                r_idx = curr[0] + dr
                c_idx = curr[1] + dc

                if 0 <= r_idx < rows and 0 <= c_idx < cols and grid[r_idx][c_idx] == 1 and (r_idx, c_idx) not in dist:
                    dist[(r_idx, c_idx)] = dist[(curr[0], curr[1])] + 1
                    grid[r_idx][c_idx] = 0
                    q.append([r_idx, c_idx])
                    res = max(res, dist[(r_idx, c_idx)])
        
        for row in grid:
            if 1 in row:
                return -1
        
        return res
        



