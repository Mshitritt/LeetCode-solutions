class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = defaultdict(int)
        dp[arr[0]] = 1
        res = 1

        for num in arr[1:]:
            rem = num - difference
            if rem in dp:
                dp[num] = max(dp[num], dp[rem] + 1)
                res = max(res, dp[num])
            else:
                dp[num] = 1
        return res
