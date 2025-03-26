class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        # GPT enhance 
        n = len(s)
        rv = s[::-1]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            prev = 0  # Like dp[j-1] from the previous row
            for j in range(1, n + 1):
                temp = dp[j]
                if s[i - 1] == rv[j - 1]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = temp

        return dp[n]
        """
        """
        # LCS version
        rv = s[::-1]
        n = len(s)

        prev, curr = [0]*(n+1), [0]*(n+1)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == rv[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(curr[j-1], prev[j])
            curr, prev = prev, curr
        
        return prev[n]
        """
        # memo version enhance by GPT
        n = len(s)

        @lru_cache(maxsize=None)
        def dp(i, j):
            if j < i:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return 2 + dp(i + 1, j - 1)
            return max(dp(i + 1, j), dp(i, j - 1))

        return dp(0, n - 1)

        """
        # Memoization version
        dp = {}
        n = len(s)

        # i - start, j - end
        def rec(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j < i or i >= n or j < 0:
                return 0
            if i == j:
                return 1

            if s[i] == s[j]:
                dp[(i, j)] = 2 + rec(i+1, j-1)
            else:
                dp[(i, j)] = max(rec(i+1, j), rec(i, j-1))
            return dp[(i, j)]

        return rec(0, n-1)
        """
