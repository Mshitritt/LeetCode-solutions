class Solution:
    def longestPalindrome(self, s: str) -> str:
        # LIS 
        rev = s[::-1]
        res = [0, 0]    # l, r
        n = len(s)
        
        dp = [[0]*n for _ in range(n)]

        # intionlaiz
        # base case - single char
        for i in range(n):
            dp[i][i] = 1
        
        # base case - 2 chars
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                res = [i, i+1]

        # fill
        for diff in range(3, n+1):
            for l in range(n-diff+1):
                r = l + diff -1
                if s[l] == s[r]:
                    dp[l][r] = dp[l+1][r-1]
                    if dp[l][r]:
                        res = [l, r]

        
        l, r = res
        return s[l:r+1]
            



        
        """
        # LCS -- > find SUBSEQUENCE, not SUBSTRING --> Wrong
        rev = s[::-1]
        n = len(s)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == rev[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # recover solution
        res = []
        i, j = n, n
        while i > 0 and j > 0 and dp[i][j]:
            if s[i-1] != rev[j-1]:
                if dp[i-1][j] > dp[i][j-1]:
                    i -= 1
                else:
                    j -= 1
            else:
                res.append(s[i-1])
                i -= 1
                j -= 1
        
        return "".join(res)
        """