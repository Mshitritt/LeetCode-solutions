class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        # initialaize 
        for i, l in enumerate(word1):
            dp[i+1][0] = dp[i][0] + 1
        
        for i, l in enumerate(word2):
            dp[0][i+1] = dp[0][i] + 1
        
        # process
        for s in range(1, n1+1):
            for e in range(1, n2+1):
                sl, el = word1[s-1], word2[e-1]
                if sl == el:
                    dp[s][e] = dp[s-1][e-1]
                else:
                    dp[s][e] = min(dp[s-1][e] + 1, dp[s][e-1] + 1)
        
        return dp[n1][n2]