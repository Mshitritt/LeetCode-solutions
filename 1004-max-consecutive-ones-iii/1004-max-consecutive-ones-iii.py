class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        nums = [1,1,1,(0),(0),1,1,1,0], k=0 --> 8
        nums = [1,1,1,0,0,0,0,(0),1,1,1,1,(0)], k = 2 --> 6
        """
        l = 0
        r = 0
        zeros = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            r += 1
        return r-l
                
        

            
                

            
