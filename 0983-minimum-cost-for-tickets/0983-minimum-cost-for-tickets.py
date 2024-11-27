class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        
        def rec(i):
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]
            
            dp[i] = float('inf')
            for d, c in zip([1, 7, 30], costs):
                nxtDay = days[i] + d
                j = i
                while j < len(days) and days[j] < nxtDay:
                    j += 1
                dp[i] = min(dp[i], c + rec(j))
                    
            return dp[i]
        
        return rec(0)

            
        