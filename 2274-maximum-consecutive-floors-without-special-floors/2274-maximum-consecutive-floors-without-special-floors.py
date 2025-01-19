class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        if not special:
            return top - bottom + 1
        special.sort()
        res = special[0] - bottom if special[0] >= bottom else 0

        for i in range(1, len(special)):
            if bottom <= special[i-1] < special[i] <= top:
                res = max(res, special[i] - special[i-1] - 1)
        
        if special[-1] <= top:
            res = max(res, top - special[-1])
        return res


        
        """
        # got LTE error due to the constrains 
        special = set(special)
        res = 0
        tempRes = 0
        for i in range(bottom, top+1):
            if i not in special:
                tempRes += 1
            else:
                res = max(res, tempRes)
                tempRes = 0
        
        res = max(res, tempRes)
        return res
        """