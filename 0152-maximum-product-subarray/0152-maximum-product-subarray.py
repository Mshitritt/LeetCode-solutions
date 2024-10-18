class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_positive = [0]*len(nums)
        dp_negative = [0]*len(nums)

        dp_positive[0] = nums[0]
        dp_negative[0] = nums[0]

        prod = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            dp_positive[i] = max(num*dp_positive[i-1], num, num*dp_negative[i-1])
            dp_negative[i] = min(num*dp_positive[i-1], num, num*dp_negative[i-1])
            prod = max(prod, dp_positive[i], dp_negative[i])
        return prod