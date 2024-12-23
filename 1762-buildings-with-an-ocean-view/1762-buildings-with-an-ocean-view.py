class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        q = [len(heights)-1]
        currMax = heights[-1]
        for i in range(len(heights)-2, -1, -1):
            if heights[i] > currMax:
                q.append(i)
                currMax = max(currMax, heights[i])
        res = []
        while q:
            res.append(q.pop())
        return res