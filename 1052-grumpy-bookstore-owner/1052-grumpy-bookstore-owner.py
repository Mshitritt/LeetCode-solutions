class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        clients = [0]*len(customers)
        for i, cust in enumerate(customers):
            gru = grumpy[i]
            if gru == 0:
                clients[i] = cust
        total = sum(clients)
        extra = sum(clients[:minutes])
        for i in range(minutes):
            if grumpy[i] == 1:
                extra += customers[i]
            else:
                extra -= customers[i]
        res = total+extra

        for r in range(minutes, len(customers)):
            l = r - minutes
            if grumpy[r] == 1:
                extra += customers[r]
            
            
            if grumpy[l] == 1:
                extra -= customers[l]
            
            res = max(res, total+extra)
        
        return res
            
