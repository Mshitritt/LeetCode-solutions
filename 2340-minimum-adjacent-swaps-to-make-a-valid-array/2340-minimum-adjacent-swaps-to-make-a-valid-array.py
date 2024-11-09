class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        idx_max = 0
        val_max = nums[0]
        
        idx_min = 0
        val_min = nums[0]

        for i in range(len(nums)):
            if nums[i] >= val_max:
                idx_max = i
                val_max = nums[i]
            
            if nums[i] < val_min:
                idx_min = i
                val_min = nums[i]
        
        if idx_min == idx_max or (idx_min == 0 and idx_max == len(nums)-1):
            return 0
        if idx_min < idx_max:
            return idx_min + (len(nums)-1 - idx_max)
        
        # idx_min > idx _max
        return (len(nums) - idx_max) + idx_min - 2

    