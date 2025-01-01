class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        s = pressedKeys
        MOD = 10**9 + 7
        res = 0
        dp = [0] * (len(s)+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, len(s)+1):
            dp[i] = dp[i - 1]  # Initialize dp[i] with the value from the previous key

            curr = s[i - 1]
            max_presses = 4 if curr in "79" else 3  # Max presses depend on the key

            for j in range(2, max_presses + 1):  # Start from 2 because 1 is already handled
                if i - j >= 0 and s[i - j] == curr:
                    dp[i] += dp[i - j]
                    dp[i] %= MOD  # Apply modulo here to avoid overflow
                else:
                    break  # Stop if keys do not match


        return dp[len(s)] % MOD
      


