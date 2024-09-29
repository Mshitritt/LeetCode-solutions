class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        max_total = nums[0]
        curr_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum+nums[i])
            
            
            max_total = max(curr_sum, max_total)
        return max_total 