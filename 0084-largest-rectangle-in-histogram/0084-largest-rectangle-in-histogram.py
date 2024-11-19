class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = heights[0]
        stack = []  # (high, index)
        

        for i, h in enumerate(heights):
            
            area = 0
            colI = i
            while stack and stack[-1][0] >= h:
                colH, colI = stack.pop()
                width = i - colI
                area = colH * width
                res = max(res, area)
            
            stack.append([h, colI])
            
            
        while stack:
            colH, colI = stack.pop()
            width = len(heights) - colI
            area = colH * width
            res = max(res, area)
        
        return res

