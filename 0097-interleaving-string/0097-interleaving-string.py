class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        n1, n2 = len(s1), len(s2)
        if n1 + n2 != len(s3):
            return False
        
        dp = [[False for _ in range(n2+1)] for _ in range(n1 + 1)]
        
        for i1 in range(n1 + 1):
            for i2 in range(n2 + 1):
                if i1 == i2 == 0:
                    dp[0][0] = True
                elif i1 == 0:
                    # letters from s2 only
                    if s2[i2-1] == s3[i1 + i2 - 1] and dp[i1][i2-1]:
                        dp[i1][i2] = True
                    else:
                        dp[i1][i2] = False
                elif i2 == 0:
                    if s1[i1-1] == s3[i1 + i2 - 1] and dp[i1-1][i2]:
                        dp[i1][i2] = True
                    else:
                        dp[i1][i2] = False
                else:
                    if (s1[i1-1] == s3[i1 + i2 - 1] and dp[i1-1][i2]) or (s2[i2-1] == s3[i1 + i2 - 1] and dp[i1][i2-1]):
                        dp[i1][i2] = True
                    else:
                        dp[i1][i2] = False
        return dp[n1][n2]





        
            

        
        
                    
            