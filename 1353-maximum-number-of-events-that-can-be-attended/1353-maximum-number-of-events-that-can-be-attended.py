class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by start day
        events.sort()
        min_heap = []
        i, res, day = 0, 0, 0
        n = len(events)

        while i < n or min_heap:
            # Advance to the next day with events or in the heap
            if not min_heap:
                day = events[i][0]
            
            # Add all events starting on the current day to the heap
            while i < n and events[i][0] <= day:
                heappush(min_heap, events[i][1])  # Push the end day
                i += 1

            # Remove events that have already ended
            while min_heap and min_heap[0] < day:
                heappop(min_heap)

            # Attend the event that ends the earliest
            if min_heap:
                heappop(min_heap)
                res += 1  # Increment count of attended events

            # Move to the next day
            day += 1

        return res


                

                

            
            


        