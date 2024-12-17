class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0

        nums = sorted(nums)
        res = float('inf')
        op1 = nums[-4] - nums[0]    # 3 larget
        op2 = nums[-1] - nums[3]    # 3 smallest
        op3 = nums[-3] - nums[1]    # 2 largest, 1 smallest
        op4 = nums[-2] - nums[2]    # 1 largest, 2 smallest
        return min(op1, op2, op3, op4)
        