class Solution:
    
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        d_queue = []
        r_queue = []
        for i in range(n):
            if senate[i] == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        while d_queue and r_queue:
            d = d_queue.pop(0)
            r = r_queue.pop(0)
            if d < r:
                # d won
                d_queue.append(d+n)
            else:
                r_queue.append(r+n)
                




        if d_queue:
            return "Dire"
        else:
            return "Radiant"


                
