class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = [float('inf')]*n
        steps[0] = 0
        for i in range(n):
            for j in range(1, nums[i]+1):
                if i + j < n:
                    steps[i+j] = min(steps[i+j], steps[i]+1)
        return steps[n-1]
            