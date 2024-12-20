class MyCalendarThree:
    def __init__(self):
        self.timeline = defaultdict(int)  # Tracks changes at specific times

    def book(self, startTime: int, endTime: int) -> int:
        # Increment count at the start and decrement at the end
        self.timeline[startTime] += 1
        self.timeline[endTime] -= 1
        
        # Sweep line to calculate maximum overlap
        active = 0
        max_k = 0
        for time in sorted(self.timeline.keys()):
            active += self.timeline[time]
            max_k = max(max_k, active)
        
        return max_k


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)