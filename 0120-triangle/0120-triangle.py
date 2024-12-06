class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for curr in range(1, len(triangle)):
            for j in range(len(triangle[curr])):
                if j == 0:
                    triangle[curr][j] += triangle[curr-1][0]
                elif j == len(triangle[curr])-1:
                    triangle[curr][j] += triangle[curr-1][j-1]
                else:
                    triangle[curr][j] += min(triangle[curr-1][j], triangle[curr-1][j-1])
                
                
        return min(triangle[-1])
