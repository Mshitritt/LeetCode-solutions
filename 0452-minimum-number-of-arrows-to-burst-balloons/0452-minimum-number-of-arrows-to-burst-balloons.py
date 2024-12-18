class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 1
        prevS, prevEnd = points[0]
        for inter in points[1:]:
            # check fo overlapping
            s, e = inter
            if s <= prevEnd:
                prevEnd = min(prevEnd, e)
            else:
                prevS, prevEnd = inter
                res += 1
        return res