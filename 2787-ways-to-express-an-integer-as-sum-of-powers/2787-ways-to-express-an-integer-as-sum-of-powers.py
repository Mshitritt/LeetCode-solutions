class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7

        # Compute the largest base such that base^x <= n
        maxBase = 1
        while maxBase**x <= n:
            maxBase += 1
        maxBase -= 1  # Adjust to the largest valid base

        # Initialize DP table
        dp = [[0] * (2) for _ in range(n + 1)]
        dp[0][0] = 1
        dp[0][1] = 1

        # Fill DP table
        for base in range(1, maxBase + 1):
            power = base**x
            for total in range(n + 1):
                # Exclude current base
                dp[total][1] = dp[total][0]
                # Include current base if possible
                if total >= power:
                    dp[total][1] = (dp[total][1] + dp[total - power][0]) % MOD
            
            # prepare dp for next iteration 
            for i in range(n+1):
                dp[i][0] = dp[i][1]

        for r in dp:
            print(r)
        return dp[n][0]

