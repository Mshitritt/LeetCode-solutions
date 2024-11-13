class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        gas is how many kilometrs 
        cost is how many kilometrs you get in gas station
        """
        if sum(gas) < sum(cost):
            return -1
        
        for i in range(len(gas)):
            count = len(gas)
            idx = i
            tank = gas[i]
            while count and tank >= cost[idx]:
                count -= 1
                tank -= cost[idx]
                idx += 1
                idx = idx % len(gas)
                tank += gas[idx]
            if count == 0:
                return i
           
        return -1
