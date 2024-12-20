class MyCalendar:

    def __init__(self):
        self.inter = []
        
    

    def book(self, startTime: int, endTime: int) -> bool:
        # Find the position to insert the new interval
        pos = bisect_left(self.inter, (startTime, endTime))

        # Check overlap with the previous interval
        if pos > 0:
            prev_start, prev_end = self.inter[pos - 1]
            if prev_end > startTime:  # Overlap condition
                return False

        # Check overlap with the next interval
        if pos < len(self.inter):
            next_start, next_end = self.inter[pos]
            if endTime > next_start:  # Overlap condition
                return False

        # Insert the new interval
        self.inter.insert(pos, (startTime, endTime))
        return True
        
                




        
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)