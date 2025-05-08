class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prevEnd = intervals[0][1]
        res = 0
        # count overlapping 
        for s, e in intervals[1:]:
            if s < prevEnd:
                res += 1
            else:
                prevEnd = e
        
        return res