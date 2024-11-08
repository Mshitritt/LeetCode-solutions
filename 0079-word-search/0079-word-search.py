class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        size_w = len(word)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, w):
            if w == size_w:
                return True
            
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[w]:
                temp = board[r][c]
                board[r][c] = '*'
                for dr, dc in directions:
                    res = dfs(r+dr, c+dc, w+1)
                    if res == True:
                        return True
                    
                board[r][c] = temp
            
            return False


        for r in range(rows):
            for c in range(cols):
                w = 0
                if board[r][c] == word[w]:
                    if dfs(r, c, w):
                        return True
        return False


