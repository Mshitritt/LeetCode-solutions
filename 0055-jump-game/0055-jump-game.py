class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Explenation- 
        we are loop over array and for each element we keep the maxumum position 

        """
        n = len(nums)
        max_pos = 0
        for i in range(n):
            # out of maximum step
            if i > max_pos:
                return False
            
            max_pos = max(max_pos, i + nums[i])
            if max_pos >= n-1:
                return True
            



