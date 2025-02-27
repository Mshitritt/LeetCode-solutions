class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = 0
        res = abs(nums[0])
        prefixMin, prefixMax = min(nums[0], 0), max(nums[0], 0)
        for num in nums:
            prefix += num
            res = max(abs(res), abs(prefix - prefixMin), abs(prefix - prefixMax))
            prefixMin, prefixMax = min(prefix, prefixMin), max(prefix, prefixMax)
        return res
                
