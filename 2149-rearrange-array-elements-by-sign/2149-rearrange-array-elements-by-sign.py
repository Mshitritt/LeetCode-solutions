class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 2:
            if nums[0] > nums[1]:
                return nums
            else:
                nums[0], nums[1] = nums[1], nums[0]
            
        
        pos, neg = [], []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        
        
        for i in range(0, n-1, 2):
            nums[i], nums[i+1] = pos[i//2], neg[i//2]
        
        return nums
