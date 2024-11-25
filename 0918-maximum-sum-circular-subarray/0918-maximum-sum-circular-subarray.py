class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        dp = [[0 for _ in range(len(nums))] for _ in range(3)]
        # dp[0] - maxSum
        # dp[1] - minSum
        # dp[2] - total-minSum
        total = sum(nums)
        max_sum = nums[0]
        dp[0][0], dp[1][0] = nums[0], nums[0]
        dp[2][0] = total-dp[1][0]
        globalMax = nums[0]
        globalMin = nums[0]
        for i in range(1, len(nums)):
            # maxSum
            dp[0][i] = max(nums[i], dp[0][i-1] + nums[i])
            # minSum
            dp[1][i] = min(nums[i], dp[1][i-1] + nums[i])
            # total-minSum
            dp[2][i] = total-dp[1][i]
            
            globalMax = max(globalMax, dp[0][i])
            globalMin = min(globalMin, dp[1][i])
        for r in dp:
            print(r)
        if total-globalMin:
            return max(globalMax, total-globalMin)
        return globalMax
