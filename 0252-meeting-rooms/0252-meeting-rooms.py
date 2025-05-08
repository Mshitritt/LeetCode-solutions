class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x:x[1])
        for i in range(1, len(intervals)):
            currS, _ = intervals[i]
            _, prevE = intervals[i-1]
            if currS < prevE:
                return False
        return True