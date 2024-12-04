class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        minVal_1, minVal_2 = float('inf'), float('inf')
        minCol_1, minCol_2 = -1, -1

        for i in range(len(costs[0])):
            currCost = costs[0][i]
            if currCost < minVal_1:
                minVal_2 = minVal_1
                minCol_2 = minCol_1

                minVal_1 = currCost
                minCol_1 = i
            elif currCost < minVal_2:
                minVal_2 = currCost
                minCol_2 = i

        

        for house in range(1, len(costs)):
            nxtCost_1, nxtCost_2 = float('inf'), float('inf')
            nxtCol_1, nxtCol_2 = -1, -1

            for color in range(len(costs[0])):
                if color == minCol_1:
                    costs[house][color] += minVal_2
                else:
                    costs[house][color] += minVal_1
                
                # prepare for next iteration 
                currCost = costs[house][color]

                if currCost < nxtCost_1:
                    nxtCost_2 = nxtCost_1
                    nxtCol_2 = nxtCol_1

                    nxtCost_1 = currCost
                    nxtCol_1 = color
                elif currCost < nxtCost_2:
                    nxtCost_2 = currCost
                    nxtCol_2 = color
                
            minVal_1, minVal_2 = nxtCost_1, nxtCost_2
            minCol_1, minCol_2 = nxtCol_1, nxtCol_2

                    

        
        return minVal_1
                
