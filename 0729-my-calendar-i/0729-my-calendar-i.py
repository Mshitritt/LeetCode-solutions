class MyCalendar:

    def __init__(self):
        self.inter = []
        
    

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.inter:
            self.inter.append([startTime, endTime])
            return True
        else:
            for i, (s, e) in enumerate(self.inter):
                # check for overlapping
                if startTime < e and endTime > s:
                    return False
                
                # check if found place
                if endTime <= s:
                    self.inter.insert(i, [startTime, endTime])
                    return True
            
            self.inter.append([startTime, endTime])
            return True
                




        
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)