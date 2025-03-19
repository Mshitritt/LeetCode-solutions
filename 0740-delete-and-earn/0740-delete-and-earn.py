class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
                
        freq = Counter(nums)
        nums = list(freq.keys())
        if len(nums) == 1:
            return nums[0] * freq[nums[0]]

        nums.sort()           
        dp = [0] * len(nums)
        dp[0] = nums[0] * freq[nums[0]]
        dp[1] = nums[1] * freq[nums[1]]
        if nums[0] + 1 != nums[1]:
            dp[1] += dp[0]
        else:
            dp[1] = max(dp[0], dp[1])

        for i in range(2, len(nums)):
            num = nums[i]
            curr = num * freq[num]
            prev_1 = nums[i-1]
            prev_2 = nums[i-2]

            if prev_1 + 1 != num:
                dp[i] = curr + dp[i-1]
            else:
                dp[i] = max(
                    curr + dp[i-2], dp[i-1]
                )
        return dp[-1]
        
            

            




