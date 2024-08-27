class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) <= 1:
            return None
        
        l = 0
        r = l + 1
        
        while r <= len(nums)-1:
            if nums[l] == 0 and nums[r] != 0:
                # swap
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp

                l += 1
                r += 1
            elif nums[l] == 0 and nums[r] == 0:
                r += 1
            elif nums[l] != 0 and nums[r] == 0:
                l += 1
            else:
                # nums[l] != 0 and nums[r] != 0
                l += 1
                r += 1
                
        return None 

        