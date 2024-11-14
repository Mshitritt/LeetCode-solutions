class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0]*len(nums)
        right = [0]*len(nums)
        for i in range(1, len(nums)):
            left[i] = left[i-1] + nums[i-1]
        
        for i in range(-2, -len(nums)-1, -1):
            right[i] = right[i+1] + nums[i+1]

        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = abs(left[i] - right[i])
        
        return ans
