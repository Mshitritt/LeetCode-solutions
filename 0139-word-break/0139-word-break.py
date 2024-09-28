class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string is always segmentable
        
        word_set = set(wordDict)  # Convert wordDict to a set for fast lookups
        
        # Iterate through the string
        for i in range(1, n + 1):
            for j in range(i):
                # Check if substring s[j:i] is in the dictionary and dp[j] is True
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]


            

        

        


        
        