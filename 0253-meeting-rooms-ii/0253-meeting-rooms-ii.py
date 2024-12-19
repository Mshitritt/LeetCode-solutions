class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # Sort by start time
        min_heap = []
        max_room = 0
        
        for s, e in intervals:
            # Remove meetings that have ended
            while min_heap and min_heap[0] <= s:
                heapq.heappop(min_heap)
            
            # Insert end time in sorted order
            heapq.heappush(min_heap, e)
            
            max_room = max(max_room, len(min_heap))
            
        return max_room
                
