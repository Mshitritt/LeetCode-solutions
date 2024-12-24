class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = [0]*len(nums)
        hm = {0: 1}
        prefix = 0
        for i, num in enumerate(nums):
            prefix = (prefix + num) % k  
            if prefix in hm:
                res[i] = hm[prefix]
                hm[prefix] += 1
                
            else:
                hm[prefix] = 1
        return sum(res)
    
