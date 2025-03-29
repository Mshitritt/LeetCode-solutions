class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [float('inf')]*(n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(i):
                sub = s[j: i]
                if sub in dictionary:
                    dp[i] = min(dp[i], dp[j])
                else:
                    dp[i] = min(dp[i], dp[j] + i - j)
        return dp[n]
        
                
            


        