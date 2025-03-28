class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        flavors = {}
        for f in candies:
            if f not in flavors:
                flavors[f] = 1
            else:
                flavors[f] += 1
        
        r = 0
        res = 0
        for r in range(k):
            f = candies[r]
            flavors[f] -= 1
            if flavors[f] == 0:
                del flavors[f]

        res = len(flavors)
        for r in range(k, len(candies)):
            flavors[candies[r]] -= 1
            if flavors[candies[r]] == 0:
                del flavors[candies[r]]

            oldF = candies[r-k]
            if oldF not in flavors:
                flavors[oldF] = 1
                res = max(res, len(flavors))
            else:
                flavors[oldF] += 1
        return res
        

            

        
        
        """
        # Prefix approach
        if len(candies) == k:
            return 0
        prefix = [0]*len(candies)
        prefix[0] = 1
        flavors = set([candies[0]])
        for i in range(1, len(candies)):
            f = candies[i]
            if f not in flavors:
                prefix[i] = prefix[i-1]+1
                flavors.add(f)
            else:
                prefix[i] = prefix[i-1]
        
        res = prefix[k-1]
        for i in range(k+1, len(candies)):
            res = max(res, prefix[i]- prefix[i-k-1])
        
        return res
        """

