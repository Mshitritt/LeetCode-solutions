class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2
        
        dp = [False] * (target + 1)
        dp[0] = True
        
        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]
        
       
        for j in range(target, -1, -1):
            if dp[j]:
                return total_sum - 2 * j