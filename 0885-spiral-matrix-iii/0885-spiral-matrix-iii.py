class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []

        
        l, r = cStart, cStart+1
        t, b = rStart, rStart+1
        while len(res) < rows * cols:
            # top row
            for i in range(l, r):
                if 0 <= t < rows and 0 <= i < cols:
                    res.append([t, i])
            l -= 1
            # right col
            for i in range(t, b):
                if 0 <= i < rows and 0 <= r < cols:
                    res.append([i, r])
            t -= 1
            # buttom column
            for i in range(r, l-1, -1):
                if 0 <= b < rows and 0 <= i < cols:
                    res.append([b, i])
            
            # left col
            for i in range(b-1, t, -1):
                if 0 <= i < rows and 0 <= l < cols:
                    res.append([i, l])
            b += 1
            r += 1
            


            

        return res