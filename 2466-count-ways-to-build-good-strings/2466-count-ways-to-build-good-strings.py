class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1

        res = 0
        arr = [zero, one]
        for i in range(1, high + 1):
            dp[i] += dp[i - zero]% MOD if i - zero >= 0 else 0
            dp[i] += dp[i - one]% MOD if i - one >= 0 else 0

            if i >= low:
                res += dp[i]% MOD
        return res% MOD
