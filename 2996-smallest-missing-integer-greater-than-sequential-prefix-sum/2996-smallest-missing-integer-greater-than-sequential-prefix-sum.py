class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix = nums[0]
        prev = nums[0]
        i = 1
        
        while i < len(nums) and nums[i] == prev+1:
            prefix += nums[i]
            prev = nums[i]
            i += 1
        
        
        unique = set(nums)

        while True:
            if prefix not in unique:
                return prefix
            prefix += 1
            

       
