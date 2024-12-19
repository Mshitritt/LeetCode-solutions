class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        q = deque() # min queue
        max_room = 0
        for s, e in intervals:
            # overlapping
            while q and q[-1] <= s:
                q.pop()

            q.append(e)
            max_room = max(max_room, len(q))
            
        return max_room
                
