class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = abs(sum(nums))
        
        # no have solution
        if ((target + total) % 2) or total < target:
            return 0
        
        plus = (target + total) // 2
        dp = [0] * (plus + 1)
        dp[0] = 1   # plus == 0

        for num in nums:
            for p in range(plus, num-1, -1):
                dp[p] += dp[p - num]
        
        return dp[plus]


