class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        minVal = float('inf')
        negative = 0
        zero = 0
        n = len(matrix)

        for r in range(n):
            for c in range(n):
                total += abs(matrix[r][c])
                minVal = min(minVal, abs(matrix[r][c]))
                if matrix[r][c] < 0:
                    negative += 1
                if matrix[r][c] == 0:
                    zero += 1
        
        if negative == 0 or negative % 2 ==0 or (negative+zero)%2 == 0:
            return total
        
        return total - minVal*2