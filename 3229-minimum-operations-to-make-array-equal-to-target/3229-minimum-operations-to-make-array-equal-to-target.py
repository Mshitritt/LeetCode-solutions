class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] -= target[i]

        operations = abs(nums[0])

        for i in range(1, len(nums)):
            prev, curr = nums[i-1], nums[i]
            if prev * curr < 0:
                operations += abs(curr)
            else:
                operations += max(abs(nums[i]) - abs(nums[i - 1]), 0)
            
        return operations
            
