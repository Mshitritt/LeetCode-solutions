class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        
        for house in range(1, len(costs)):
            for color in range(len(costs[0])):
                minVal = float('inf')
                for prev in range(len(costs[0])):
                    if color != prev:
                        minVal = min(minVal, costs[house-1][prev])
                costs[house][color] += minVal
        return min(costs[-1])
                
