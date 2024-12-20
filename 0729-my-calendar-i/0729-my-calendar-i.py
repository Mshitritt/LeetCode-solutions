class MyCalendar:

    def __init__(self):
        self.inter = []
        
    

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.inter:
            self.inter.append([startTime, endTime])
            return True
        else:
            # insert first
            if endTime < self.inter[0][0]:
                self.inter.insert(0, [startTime, endTime])
                return True
            else:
                for s, e in self.inter:
                    # Check for overlap
                    if not (endTime <= s or startTime >= e):
                        return False

                # No overlap; find the correct position to insert
                self.inter.append([startTime, endTime])
                self.inter.sort()  # Keep the intervals sorted
                return True



        
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)