class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        dp = [0]*len(values)
        for j in range(1, len(values)):
            dp[j] = max(values[j-1], dp[j-1]) - 1
        
        res = 0
        for i in range(1, len(values)):
            values[i] += dp[i]
            res = max(res, values[i])
        return res
        
        