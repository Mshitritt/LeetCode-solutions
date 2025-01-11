class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]
        
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2

            # check from left side
            if m+1 < len(nums) and nums[m] > nums[m+1]:
                return nums[m+1]
            
            # check from right side 
            if m-1 >= 0 and nums[m-1] > nums[m]:
                return nums[m]

            if nums[m] > nums[0]:
                # right side
                l = m + 1
            else:
                # left side
                r = m - 1
        
        return nums[0]

            