class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for r in range(1, rows-1):
            for c in range(1, cols-1):
                if board[r][c] == "O":
                    serround = 0
                    for dr, dc in direction:
                        idr = r+dr
                        idc = c+dc
                        if 0 <= idr < rows and 0 <= idc < cols and board[idr][idc] == "X":
                            serround += 2
                    if serround >= 2:
                        board[r][c] = "X"
                        q = deque()
                        q.append((r, c))
                        while q:
                            curr = q.popleft()
                            for dr, dc in direction:
                                idr = curr[0]+dr
                                idc = curr[1]+dc
                                if 0 <= idr < rows and 0 <= idc < cols and board[idr][idc] == "O":
                                    q.append((idr, idc))
                                    board[idr][idc] = "X"


        