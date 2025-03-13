class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        half = total // 2
        dp = [False] * (half + 1)
        dp[0] = True
        for i in range(len(nums)):
            num = nums[i]
            for h in range(half, num-1, -1):
                dp[h] = dp[h-num] or dp[h]
                
        return dp[half]

        
