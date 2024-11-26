class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = 0
        for num in nums:
            if num < 0:
                total -= num
            else:
                total += num
        
        if total < target:
            return 0

        n = len(nums)
        dp = [[0 for _ in range(total*2+1)] for _ in range(n)]
        
       
        # initionlaize 
        dp[0][total+nums[0]] += 1
        dp[0][total-nums[0]] += 1

        # running 
        for i in range(1, n):
            for t in range(-total, total+1):
                if dp[i-1][t+total]:
                    dp[i][t+total+nums[i]] += dp[i-1][t+total]
                    dp[i][t+total-nums[i]] += dp[i-1][t+total]
        
        
        return dp[n-1][total+target]
        