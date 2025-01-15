class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def isValid(h):
            # return True if there have at least h citations
            # with number of at least citiations
            res = 0
            for num in citations:
                if num >= h:
                    res += 1
            return res >= h
        
        l, r = 0, max(citations)
        while l <= r:
            h = (l + r)//2
            if isValid(h):
                l = h+1
            else:
                r = h-1
        return r
