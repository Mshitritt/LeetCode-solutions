class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = 0

        while l < r:
            l_num = nums[l]
            r_num = nums[r]
            
            while l < r and l_num != r_num:
                res += 1
                if l_num > r_num:
                    r -= 1
                    r_num += nums[r]
                else:
                    l += 1
                    l_num += nums[l]
            
            if l_num == r_num:
                l += 1
                r -= 1
            
        return res
                



