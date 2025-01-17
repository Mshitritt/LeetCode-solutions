class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [[1, 1] for _ in range(n)]
        # dp[0] - end with small number
        # dp[1] - end with large number

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # increase value --> change the small 
                dp[i][0] = dp[i-1][1] + 1
                dp[i][1] = dp[i-1][1]
            elif nums[i] < nums[i-1]:
                # decrease values --> change the large
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][0] + 1
            else:
                # monotomic values --> no changes 
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]
        
        return max(dp[n-1][0], dp[n-1][1])

        
            




