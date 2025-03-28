class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        idx = {}
        
        res = 2
        
        for i in range(n):
            idx[arr[i]] = i
            for j in range(i):
                k = arr[i] - arr[j]
                if k in idx and idx[k] < j:
                    k_idx = idx[k]
                    dp[j][i] = max(dp[j][i], dp[k_idx][j] + 1)
                    res = max(res, dp[j][i])
        return res if res >= 3 else 0

        