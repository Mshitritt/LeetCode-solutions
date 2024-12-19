class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Min-heap to track end times
        import heapq
        heap = []

        for start, end in intervals:
            # Step 3: Remove meetings that have ended
            if heap and heap[0] <= start:
                heapq.heappop(heap)

            # Step 4: Add current meeting's end time
            heapq.heappush(heap, end)

        # Step 5: The size of the heap is the number of rooms required
        return len(heap)
