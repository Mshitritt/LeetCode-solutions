class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10**9 + 7
        n = len(pressedKeys)
        s = pressedKeys
        dp = [0] * (n + 1)
        # dp[i] = number of text for s[i-1]
        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            curr = s[i-1]
            press = 4 if curr in "79" else 3

            for j in range(i-1, max(-1, i-press-1), -1):
                if s[j] == curr:
                    dp[i] += dp[j] % MOD
                else:
                    dp[i] += dp[i-1] if not dp[i] else 0
                    break
        return dp[n] % MOD


        