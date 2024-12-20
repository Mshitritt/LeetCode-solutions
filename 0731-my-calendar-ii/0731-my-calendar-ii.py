class MyCalendarTwo:
    def __init__(self):
        self.inter = []  # Tracks all booked intervals
        self.double_booked = []  # Tracks double-booked intervals

    def book(self, startTime: int, endTime: int) -> bool:
        # Check if the new interval causes a triple booking
        for d_start, d_end in self.double_booked:
            if max(startTime, d_start) < min(endTime, d_end):  # Overlap with double-booked intervals
                return False
        
        # Update double-booked intervals based on overlaps with single-booked intervals
        for s_start, s_end in self.inter:
            if max(startTime, s_start) < min(endTime, s_end):  # Overlap with single-booked intervals
                self.double_booked.append((max(startTime, s_start), min(endTime, s_end)))
        
        # Add the new interval to single bookings
        self.inter.append((startTime, endTime))
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)