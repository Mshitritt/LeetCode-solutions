class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # Sort by start time
        q = deque()  # stores end times in sorted order
        max_room = 0
        
        for s, e in intervals:
            # Remove meetings that have ended
            while q and q[0] <= s:
                q.popleft()
            
            # Insert end time in sorted order
            i = 0
            while i < len(q) and q[i] < e:
                i += 1
            q.insert(i, e)
            
            max_room = max(max_room, len(q))
            
        return max_room
                
