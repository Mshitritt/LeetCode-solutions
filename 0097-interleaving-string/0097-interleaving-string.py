class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        memo = {}
        # rows = s1, cols = s2

        def rec(i1, i2):
            # i1, i2 - indecis of s1 and s2
            # i3 = i1 + i2 - index s3
            if i1 == len(s1) and i2 == len(s2):
                return True
            if (i1, i2) in memo:
                return memo[(i1, i2)]

            if i1 < len(s1) and s1[i1] == s3[i1 + i2] and rec(i1 + 1, i2):
                memo[(i1, i2)] = True
                return True

            if i2 < len(s2) and s2[i2] == s3[i1 + i2] and rec(i1, i2 + 1):
                memo[(i1, i2)] = True
                return True

            memo[(i1, i2)] = False
            return False

        
        return rec(0, 0)
            


        
                    
            