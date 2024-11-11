class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minVal = prices[0]  # indicate for buy
        maxVal = prices[0]  # indicate for sell
        i = 1
        while i < len(prices):
            curr = prices[i]
            if curr < minVal:
                minVal = curr
                # check where sell
                i += 1
                while i < len(prices) and prices[i-1] < prices[i]:
                    i += 1
                if i-1 < len(prices):
                    res += prices[i-1] - minVal
                    if i < len(prices):
                        minVal = prices[i]
                    else:
                        break
            elif curr == minVal:
                i += 1
            else:
                # curr > minVal
                while i + 1 < len(prices) and prices[i+1] > prices[i]:
                    i += 1
                res += prices[i] - minVal
                if i+1 < len(prices):
                    minVal = prices[i+1]
                    i += 1
                else:
                    break
        return res

