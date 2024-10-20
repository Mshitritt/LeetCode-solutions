class Solution:
    import heapq
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        inter = sorted(intervals, key=lambda x: x[0])
        rooms = 1
        i = 1
        n = len(inter)
        heap = [inter[0][1]]
        while i < n:
            curr = inter[i]
            if curr[0] < heap[0]:
                rooms += 1
                
                
            else:
                if heap:
                    heapq.heappop(heap)
            
            heapq.heappush(heap, curr[1])
            i += 1
        return rooms
        