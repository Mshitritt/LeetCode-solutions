class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        # Helper function to perform DFS and collect cells in the current region
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O' or visited[x][y]:
                return
            visited[x][y] = True
            region.append((x, y))  # Collect the cell in the current region
            # Perform DFS in all four directions
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        # Iterate through the board to find regions of 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    region = []  # Collect cells in the current region
                    dfs(i, j)
                    
                    # Check if the region touches the boundary
                    is_surrounded = True
                    for x, y in region:
                        if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                            is_surrounded = False
                            break
                    
                    # If the region is surrounded, turn all 'O's in the region to 'X'
                    if is_surrounded:
                        for x, y in region:
                            board[x][y] = 'X'
                
                    

        