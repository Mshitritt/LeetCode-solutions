class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        rLen = len(grid)
        cLen = len(grid[0])
        
        # Directions for moving up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = "0"  # Mark as visited (change to water)

            while q:
                ri, ci = q.popleft()  # O(1) with deque

                # Explore all 4 directions
                for dr, dc in directions:
                    new_r, new_c = ri + dr, ci + dc
                    if 0 <= new_r < rLen and 0 <= new_c < cLen and grid[new_r][new_c] == "1":
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = "0"  # Mark as visited

        # Iterate through the grid
        for r in range(rLen):
            for c in range(cLen):
                if grid[r][c] == "1":  # Found an island
                    island_count += 1
                    bfs(r, c)

        return island_count

                        

                    

