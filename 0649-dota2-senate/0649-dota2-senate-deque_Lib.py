class Solution:
    
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        n = len(senate)
        d_queue = deque()
        r_queue = deque()
        for i in range(n):
            if senate[i] == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        while d_queue and r_queue:
            d = d_queue.popleft()
            r = r_queue.popleft()
            if d < r:
                # d won
                d_queue.append(d+n)
            else:
                r_queue.append(r+n)
                
        if d_queue:
            return "Dire"
        else:
            return "Radiant"


                
