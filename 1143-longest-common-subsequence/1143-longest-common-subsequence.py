class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom Up - Optimized space 
        n1, n2 = len(text1), len(text2)
        if n2 < n1:
            text1, text2 = text2, text1
        # text1 - the short one 
        prev = [0]*(len(text1) + 1)
        curr = [0]*(len(text1) + 1)

        for j in range(1, len(text2) + 1):
            for i in range(1, len(text1) + 1):
            
                if text1[i-1] == text2[j-1]:
                    curr[i] = 1 + prev[i-1]
                else:
                    curr[i] = max(curr[i-1], prev[i])
            curr, prev, = prev, curr
        
        return prev[len(text1)]

        
        


