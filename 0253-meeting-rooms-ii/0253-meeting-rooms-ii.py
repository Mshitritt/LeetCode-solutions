class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Sort by start time (not actually needed for line sweep)
        intervals.sort(key=lambda x: x[0])
        
        # Find maximum ending time
        max_end = max(map(lambda x: x[1], intervals))
        sweep = [0] * (max_end + 2)
        
        # Mark start and end points
        for s, e in intervals:
            sweep[s] += 1     # Room needed at start
            sweep[e] -= 1     # Room freed at end (not e+1)
        
        # Track maximum overlapping meetings
        res = sweep[0]    # Start with first value
        curr = sweep[0]   # Current running sum
        
        # Calculate prefix sum
        for i in range(1, max_end + 1):  # Only need to go to max_end
            curr += sweep[i]
            res = max(res, curr)
        
        return res