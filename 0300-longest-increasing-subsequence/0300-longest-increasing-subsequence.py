class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [[0]*n for _ in range(n+1)]
        result = 1

        for i in range(1, n+1):
            for j in range(i):
                if j == 0:
                    # Starting a new subsequence explicitly at i-1
                    dp[i][i-1] = max(dp[i][i-1], 1)
                else:
                    if nums[i-1] > nums[j-1]:
                        # Explicitly extending previous subsequence ending at j-1
                        dp[i][i-1] = max(dp[i][i-1], dp[j][j-1] + 1)

                # Explicitly carry forward previous state if not picking current element
                dp[i][j] = max(dp[i][j], dp[i-1][j])

        # Explicitly finding global optimal
        result = 0
        for j in range(len(nums)):
            result = max(result, dp[n][j])
        
        return result