class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prevS, prevE = intervals[0]

        for s, e in intervals:
            if s <= prevE:
                # overlapping 
                prevE = max(prevE, e)
            else:
                # no overlapping
                res.append([prevS, prevE])
                prevS, prevE = s, e
        
        res.append([prevS, prevE])
        return res