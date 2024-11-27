class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def rec(nums):
            if len(nums) == 0:
                return [[]]
            perm = rec(nums[1:])
            res = []
            for p in perm:
                for i in range(len(p)+1):
                    p_copy = p.copy()
                    p_copy.insert(i, nums[0])
                    res.append(p_copy)
            return res
        
        ans = rec(nums)
        return ans
