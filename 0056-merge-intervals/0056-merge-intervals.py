class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        interval_sorted = sorted(intervals, key=lambda x: x[0])
        res = []
        n = len(intervals)
        i = 1
        start = interval_sorted[0][0]
        end = interval_sorted[0][1]

        while i < n:
            curr = interval_sorted[i]
            if curr[0] <= end:
                # overlapped interval
                if curr[1] > end:
                    end = curr[1]
                i += 1
            else:
                res.append([start, end])
                start = curr[0]
                end = curr[1]
                i += 1
        res.append([start, end])
        return res
            


            
            

        