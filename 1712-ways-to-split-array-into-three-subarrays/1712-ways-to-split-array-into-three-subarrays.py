class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        res = 0
        n = len(nums)

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        # [0:i], [i:j], [j:]
        for i in range(len(nums)-2):
            left = prefix[i]
            j = max(i + 1, bisect_left(prefix, 2 * left, i + 1, n - 1))
            k = bisect_right(prefix, (prefix[-1] + left) // 2, i + 1, n - 1) - 1
            if j <= k:
                res += (k - j + 1)
                res %= MOD
            
                
        return res

        
        
            
            