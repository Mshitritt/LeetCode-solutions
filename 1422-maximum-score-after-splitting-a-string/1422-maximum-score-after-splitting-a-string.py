class Solution:
    def maxScore(self, s: str) -> int:
        
        zeros = [0] * len(s)
        ones = [0] * len(s)
        if s[-1] == '1':
            ones[-1] = 1
        if s[0] == '0':
            zeros[0] = 1
        
        for i in range(1, len(s)):
            if s[i] == '0':
                zeros[i] = zeros[i-1] + 1
            else:
                zeros[i] = zeros[i-1]

        for i in range(-1, -len(s)-1, -1):
            if s[i] == '1':
                ones[i] = ones[i+1] + 1
            else:
                ones[i] = ones[i+1]
        res = 0
        if not len(s) - 2:
            res = ones[0] + zeros[0]
        for i in range(1, len(s)-1):
            res = max(res, zeros[i] + ones[i])
        return res
        """
        n = len(s)
        zeros = 1 if s[0] == '0' else 0
        ones = sum(1 for ch in s[1:] if ch == '1')

        ans = zeros + ones
        for i in range(1, n - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            ans = max(ans, zeros + ones)
        return ans
        """
