class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        def isNear(curr, adj):
            if adj == curr-1 or adj == curr+1:
                return False
            return True

        if len(nums) == 1:
            return nums[0]

        dp = [0]*len(nums)
        # row 0 - with number
        # row 1 - without numbr
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            j = i-1
            while j >= 0 and isNear(nums[i], nums[j]) == False:
                j -= 1
            if j >= 0:
                dp[i] = max(dp[i-1], dp[j] + nums[i])
            else:
                dp[i] = nums[i]

        print(dp)
        return max(dp)
                



        


