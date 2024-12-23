class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1 
        n = len(grid)
        res = -1
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]

        q = deque()
        q.append((0, 0, 1)) # (r, c, len)
        visited = set()
        visited.add((0, 0)) # (r, c)

        while q:
            r, c, l = q.popleft()
            if r == c == n-1:
                return l
            for dr, dc in directions:
                newR, newC = r+dr, c+dc
                if 0 <= newR < n and 0 <= newC < n and (newR, newC) not in visited:
                    if grid[newR][newC] == 0:
                        visited.add((newR, newC))
                        q.append((newR, newC, l+1))

        return -1
