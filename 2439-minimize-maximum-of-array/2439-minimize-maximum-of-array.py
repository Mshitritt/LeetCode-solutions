class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        minVal = nums[0]
        for i in range(1, len(nums)):
            if nums[i] >= dp[i-1]:
                gap = (nums[i] - dp[i-1])//2
                if gap >= i:
                    dp[i] = nums[i] - gap
                else:
                    dp[i] = dp[i-1]

            else:
                dp[i] = dp[i-1]
        
        return dp[-1]
            

        


        