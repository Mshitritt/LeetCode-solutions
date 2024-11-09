class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    if r == 0 and c == 0:
                        if text1[r] == text2[c]:
                            dp[r][c] = 1
                        else:
                            dp[r][c] = 0
                    elif r:
                        # c == 0
                        if text1[r] == text2[c]:
                            dp[r][c] = 1
                        else:
                            dp[r][c] = dp[r-1][c]
                    else:
                        # r == 0
                        # c == 0
                        if text1[r] == text2[c]:
                            dp[r][c] = 1
                        else:
                            dp[r][c] = dp[r][c-1]

                elif text1[r] == text2[c]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r][c-1], dp[r-1][c])
        for r in dp:
            print(r)
        return dp[rows-1][cols-1]
        
        


