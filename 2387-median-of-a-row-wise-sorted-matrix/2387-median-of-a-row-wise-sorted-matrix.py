class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        def bs_left(row, target):
            l = 0
            r = len(row)

            while l < r:
                m = (l+r)//2
                if row[m] <= target:
                    l = m+1
                else:
                    r = m
                    
            return l

        
        l = 0
        r = grid[-1][-1]
        mid_pos = (len(grid)*len(grid[0]) + 1)//2

        while l < r:
            mid = (l+r)//2
            count = 0

            for row in grid:
                count += bs_left(row, mid)

            if count < mid_pos:
                l = mid + 1
            else:
                r = mid
        return l


            




