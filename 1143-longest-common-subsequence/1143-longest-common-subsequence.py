class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Memoization 
        dp = {}
        n1, n2 = len(text1), len(text2)
        def rec(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == n1 or j == n2:
                    return 0
            
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + rec(i+1, j+1)
            else:
                dp[(i, j)] = max(rec(i+1, j), rec(i, j+1))
            return dp[(i, j)]
        
        
        return rec(0, 0)
                

        
        


