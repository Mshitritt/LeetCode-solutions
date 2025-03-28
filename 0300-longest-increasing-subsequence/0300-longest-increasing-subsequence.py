class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Create a sorted copy of nums (removing duplicates)
        n = len(nums)
        dp = [1]*n
        res = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    res = max(res, dp[i])
        return res

        
        