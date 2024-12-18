class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        newS, newE = newInterval
        for i in range(len(intervals)):
            # found place & no overlapping
            if newE < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # no found place & no overlap
            elif newS > intervals[i][1]:
                res.append(intervals[i])
            else:
                # have overlapping
                s = min(intervals[i][0], newInterval[0])
                e = max(intervals[i][1], newInterval[1])
                newInterval = [s, e]
        
        # edge case - newInterval insert in the end
        res.append(newInterval)
        return res
                

        

        

            
            
            
            

            

        
                





        