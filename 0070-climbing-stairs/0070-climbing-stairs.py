class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        memo = [1] * n
        i = 1
        while i < n:
            memo[i] = memo[i-1] + memo[i-2]
            i += 1
        return memo[n-1]
        