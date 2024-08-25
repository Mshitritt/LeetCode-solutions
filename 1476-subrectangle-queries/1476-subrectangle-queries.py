class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        colNum = len(rectangle[0])
        rowNum = len(rectangle)
        """
        Pay attention to differences:
            1. mat = [[0] * colNum] * rowNum
            2. mat = [[0 for _ in range(colNum)] for _ in range(rowNum)]
            in first method all the rows are duplicate of each other
                so if you change the value mat[0][0] all the values with index row=0 will be changed 
            in second method the matrix creates row by row separately 
        """
        self.mat = [[0 for _ in range(colNum)] for _ in range(rowNum)]
        for r in range(rowNum):
            for c in range(colNum):
                self.mat[r][c] = rectangle[r][c]

        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                self.mat[r][c] = newValue
        return None 
        

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        return self.mat[row][col]
        


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)