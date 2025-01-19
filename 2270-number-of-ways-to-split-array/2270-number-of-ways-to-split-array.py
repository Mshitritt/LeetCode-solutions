class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        res = 0

        for i in range(len(nums)-1):
            left += nums[i]
            right = total - left

            if left >= right:
                res += 1
        
        return res
