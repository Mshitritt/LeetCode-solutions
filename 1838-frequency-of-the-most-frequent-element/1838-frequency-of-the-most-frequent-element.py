class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        res = 1
        for i in range(1, len(nums)):
            if 0 <= nums[i] - nums[i-1] <= k:
                if nums[i] > nums[i-1]:
                    k -= nums[i] - nums[i-1]
                    nums[i] = nums[i-1] + (nums[i] - nums[i-1])
                res += 1
        return res
                   
            