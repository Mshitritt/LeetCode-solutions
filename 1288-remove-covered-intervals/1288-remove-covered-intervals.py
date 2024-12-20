class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # Sort by start time
        prevS, prevE = intervals[0][0], intervals[0][1]
        res = len(intervals)
        for s, e in intervals[1:]:
            if prevS <= s <= prevE and prevS <= e <= prevE:
                # cover
                res -= 1
            elif s <= prevS <= e and s <= prevE <= e:
                # cover
                res -= 1
                prevS, prevE = s, e
            else:
                prevS, prevE = s, e
            
            
        return res