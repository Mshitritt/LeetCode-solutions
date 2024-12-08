class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        windowSize = sum(nums)
        
        n = len(nums)
        ones = sum(nums[:windowSize])
        res = windowSize - ones

        for i in range(windowSize, 2*n):
            r = i%n
            l = (i-windowSize)%n
            if nums[r] == 1:
                ones += 1
            
            if nums[l] == 1:
                ones -= 1
            res = min(res, windowSize-ones)
        
        return res


        
