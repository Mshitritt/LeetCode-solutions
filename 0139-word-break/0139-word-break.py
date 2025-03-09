class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*len(s)
        words = set(wordDict)
        idx = [-1]

        for i in range(len(s)):
            for j in idx:
                if s[j+1:i+1] in words:
                    dp[i] = True
                    idx.append(i)
                    break
                
        return dp[-1]
