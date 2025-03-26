class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom Up - Optimized space - VER 2
        n1, n2 = len(text1), len(text2)
        if n1 > n2:
            text1, text2 = text2, text1
            n1, n2 = n2, n1

        # text1 - the short one 
        dp = [0] * (n1 + 1)
        
        for j in range(1, len(text2) + 1):
            prev = 0
            for i in range(1, len(text1) + 1):
                temp = dp[i]
                if text1[i-1] == text2[j-1]:
                    dp[i] = 1 + prev
                else:
                    dp[i] = max(dp[i-1], dp[i])
                prev = temp
            
        
        return dp[len(text1)]
        """
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
                    curr[i] = 1 + curr[i-1]
                else:
                    curr[i] = max(curr[i-1], prev[i])
            #curr, prev, = prev, curr
            prev = curr.copy()
        
        return prev[len(text1)]
        """
                

        
        


