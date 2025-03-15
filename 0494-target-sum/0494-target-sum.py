class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        self.n = len(nums)

        def rec(idx, currSum):
            if (idx, currSum) in memo:
                return memo[(idx, currSum)]
            
            if idx == len(nums):
                return 1 if currSum == target else 0
            
            plus = rec(idx+1, currSum + nums[idx])
            minus = rec(idx+1, currSum - nums[idx])
            
            memo[(idx, currSum)] = plus + minus
            return memo[(idx, currSum)]
        
        sol = rec(0, 0)
        return sol
