class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # Start from the top-right corner
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        
        # While we are within bounds of the matrix
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                # Move left to decrease the value
                col -= 1
            else:
                # Move down to increase the value
                row += 1
        
        return False
                    
        
        

