class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0 
        dp = [0]*(len(s)+1)
        # base case
        prev_2, prev_1 = 1, 1 # 1-last index, 2 - two last indices
        res = 0
        for i in range(2, len(s)+1):
            l = s[i-1]
            if l != '0':
                # dp[i] = dp[i-1]
                res = prev_1
            if 10 <= int(s[i-2]+l) <= 26: 
                # dp[i] += dp[i-2]
                res += prev_2
            prev_2, prev_1 = prev_1, res
            res = 0
        
        return prev_1
            
