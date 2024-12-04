class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7

        # Compute the largest base such that base^x <= n
        maxBase = 1
        while maxBase**x <= n:
            maxBase += 1
        maxBase -= 1  # Adjust to the largest valid base

        # Initialize DP table
        dp = [[0] * (maxBase + 1) for _ in range(n + 1)]
        for base in range(maxBase + 1):
            dp[0][base] = 1  # Base case: 1 way to make sum 0

        # Fill DP table
        for base in range(1, maxBase + 1):
            power = base**x
            for total in range(n + 1):
                # Exclude current base
                dp[total][base] = dp[total][base - 1]
                # Include current base if possible
                if total >= power:
                    dp[total][base] = (dp[total][base] + dp[total - power][base - 1]) % MOD

        for r in dp:
            print(r)
        return dp[n][maxBase]

