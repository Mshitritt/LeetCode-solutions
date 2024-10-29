class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        """
        1   2   3   4
        5   6   7   8   
        9   10  11  12
        13  14  15  16

        1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
        """
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        r = 0
        c = 0


        while True:
            # right move
            while c < cols and matrix[r][c] != -200:
                res.append(matrix[r][c])
                matrix[r][c] = -200
                c += 1

            r += 1
            c -= 1
            # down move
            while r < rows and matrix[r][c] != -200:
                res.append(matrix[r][c])
                matrix[r][c] = -200
                r += 1

            c -= 1
            r -= 1
            # left move
            while c >= 0 and matrix[r][c] != -200:
                res.append(matrix[r][c])
                matrix[r][c] = -200
                c -= 1

            r -= 1
            c += 1
            # up move
            while r > 0 and matrix[r][c] != -200:
                res.append(matrix[r][c])
                matrix[r][c] = -200
                r -= 1

            c += 1
            r += 1
            if r >= rows or c >= cols or matrix[r][c] == -200:
                return res
            


