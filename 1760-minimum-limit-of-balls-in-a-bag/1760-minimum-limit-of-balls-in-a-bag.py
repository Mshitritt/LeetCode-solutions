class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def mxValid(x):
            if x == 0:
                return False
            op = 0
            for num in nums:
                if num > x:
                    op += math.ceil(num/x)-1
                    if op > maxOperations:
                        return False
            return True
        
        r = max(nums)
        l = 1
        while l <= r:
            x = (l+r)//2
            if mxValid(x):
                r = x-1
            else:
                l = x+1
        return l
