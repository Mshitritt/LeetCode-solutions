class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0
        minVal = nums[0]
        for num in nums:
            total += num
            minVal = min(minVal, total)
        
        if minVal <= 0:
            return 1 - minVal
        return minVal
        