class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for c in range(n)] for r in range(n)]
        start = 0
        end = 0

        # main diagonal
        for i in range(n):
            dp[i][i] = 1

        # Palindrome in length 2
        for r in range(1, n):
            c = r - 1
            if s[r] == s[c]:
                dp[r][c] = 1
                start = c
                end = r

        # Palindrome in length grater than 2
        for l in range(3, n+1):
            for c in range(n - l + 1):
                r = c + l - 1

                if s[r] == s[c] and dp[r-1][c+1]:
                    dp[r][c] = 1
                    start = c
                    end = r

        return ''.join(s[start: end+1])
        