class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = [0]*(len(nums))
        right = [0]*(len(nums))
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] + nums[i-1]
        
        for i in range(-2, -len(nums)-1, -1):
            right[i] = right[i+1] + nums[i+1]

        for i in range(1, len(nums)):
            if left[i] == right[i]:
                return i
        return -1
