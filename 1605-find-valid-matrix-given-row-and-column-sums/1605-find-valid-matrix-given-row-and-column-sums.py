class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        mat = [[0 for _ in range(cols)] for _ in range(rows)]

        # initionlaize 
        for i in range(rows):
            mat[i][0] = rowSum[i]

        # fill the rest of mat
        for c in range(cols-1):
            # sum all cols
            have = 0
            for r in range(rows):
                have += mat[r][c]
            
            remove = have - colSum[c]

            # move numbers into right col
            if remove > 0:
                for r in range(rows):
                    curr = mat[r][c]
                    maxRemove = min(remove, curr)
                    mat[r][c] -= maxRemove
                    mat[r][c+1] = maxRemove
                    remove -= maxRemove
        return mat

            
            
                