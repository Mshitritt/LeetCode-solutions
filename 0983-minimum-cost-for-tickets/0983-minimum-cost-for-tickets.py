class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf')] * (days[-1]+1)
        dp[0] = 0
        # dp[i] = min cost for day i-1
        travel = set(days)
        
        for d in range(1,days[-1] + 1):
            for t, c in zip([1, 7, 30], costs):
                if d in travel:
                    if d-t >= 0:
                        dp[d] = min(dp[d], c + dp[d-t])
                    else:
                        dp[d] = min(dp[d], c)
                else:
                    dp[d] = dp[d-1]

        return dp[days[-1]]
