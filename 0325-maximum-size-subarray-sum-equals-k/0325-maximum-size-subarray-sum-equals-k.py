class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        res = 0 
        prefix = {nums[0]: 0}
        pre = 0
        
        for i in range(len(nums)):
            pre += nums[i]
            if pre not in prefix:
                prefix[pre] = i
            
            if pre == k:
                res = i+1
            else:
                d = pre - k
                if d in prefix:
                    res = max(res, i - prefix[d])
        return res
            