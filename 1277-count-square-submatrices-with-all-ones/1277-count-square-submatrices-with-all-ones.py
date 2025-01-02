class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0

        for r in range(rows):
            res += matrix[r][0]
        for c in range(1, cols):
            res += matrix[0][c]

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c]:
                    square = min(matrix[r-1][c-1], matrix[r-1][c], matrix[r][c-1])
                    matrix[r][c] = square+1
                    res += matrix[r][c]
        return res

                