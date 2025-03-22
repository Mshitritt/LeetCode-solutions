class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        dp[1] = arr[0]
        currMax = arr[0]

        for i in range(1, n):
            currMax = arr[i]
            for j in range(i, max(-1, i-k), -1):
                currMax = max(currMax, arr[j])
                size = i-j+1
                dp[i+1] = max(dp[i+1], currMax * size + dp[j])
        return dp[n]
        