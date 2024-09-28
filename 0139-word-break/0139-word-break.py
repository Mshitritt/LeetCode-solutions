class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [0]*n  #dp[i]=1 indicate s[:i] has valid word break 
        
        for j in range(n):
            # if s[:j] is word
            if s[:j] in wordDict:
                dp[j-1] = 1
            else:
                # if s[:j] can be segmented
                for i in range(j):
                    if dp[i] and s[i+1:j+1] in wordDict:
                        dp[j] = 1
                        break
        return dp[n-1] == 1


            

        

        


        
        