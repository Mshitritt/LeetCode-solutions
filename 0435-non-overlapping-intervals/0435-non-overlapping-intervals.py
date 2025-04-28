class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        prevEnd = intervals[0][1]
        for inter in intervals[1:]:
            # check fo overlapping
            s, e = inter
            if s < prevEnd:
                res += 1
                prevEnd = min(prevEnd, e)
            else:
                prevEnd = e
        return res