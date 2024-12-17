class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def mxValid(x):
            if x == 0:
                return False
            res = 0
            for c in candies:
                if c >= x:
                    res += c // x
            return res >= k
        
        
        
        l = 0
        r = max(candies)

        while l <= r:
            x = (l+r)//2
            if mxValid(x) or x == 0:
                l = x + 1
            else:
                r = x - 1
        return r if r>=0 else l
        
        