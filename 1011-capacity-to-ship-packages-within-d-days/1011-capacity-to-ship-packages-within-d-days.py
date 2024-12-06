class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(w):
            count = 1
            temp = 0
            for i in range(len(weights)):
                if temp + weights[i] <= w:
                    temp += weights[i]
                
                else:
                    count += 1
                    temp = weights[i]
                    if count > days:
                        return False
            return True

        
        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = (l+r)//2
            if isValid(mid):
                r = mid-1
            else:
                l = mid+1
        return l
