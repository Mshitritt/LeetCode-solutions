class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # Sort by start time
        
        max_end = max(map(lambda x: x[1], intervals))
        sweep = [0]*(max_end + 2)

        for s, e in intervals:
            sweep[s] += 1
            sweep[e] -= 1

        res = sweep[0]
        prefix = sweep[0]
        for i in range(1, max_end + 1):
            prefix += sweep[i]
            res = max(res, prefix)
        
        return res
                
