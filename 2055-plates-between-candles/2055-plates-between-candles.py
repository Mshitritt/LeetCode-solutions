class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [0]*len(s)
        left_close = [-1]*len(s)
        right_close = [-1]*len(s)
        res = []
        candles = set()
        
        if s[0] == '*':
            prefix[0] = 1
        for i in range(1, len(s)):
            if s[i] == "*":
                prefix[i] = prefix[i-1]+1
            else:
                candles.add(i)
                prefix[i] = prefix[i-1]
        
        idx = -1
        for i in range(len(s)):
            if s[i] == '|':
                left_close[i] = i
                idx = i
            else:
                left_close[i] = idx

        idx = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] == '|':
                right_close[i] = i
                idx = i
            else:
                right_close[i] = idx
            

        for l, r in queries:
            left = right_close[l]
            right = left_close[r]
            if left != -1 and right != -1 and left < right:
                res.append(prefix[right] - prefix[left])
            else:
                res.append(0)

        return res
        

            
       
       
       
        
        
