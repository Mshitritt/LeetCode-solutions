class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = list(freq.keys())

        nums.sort()           
        dp = [0] * len(nums)
        res = 0
        for i in range(len(nums)):
            num = nums[i]
            curr = num * freq[num]
            dp[i] = curr
            for j in range(i):
                if nums[j] + 1 != num:
                    dp[i] = max(dp[i], dp[j] + curr)
            res = max(res, dp[i])
        return res

            




