class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)  # Calculate the total sum of the array
        left_sum = 0  # Initialize the left sum to 0

        for i in range(len(nums)):
            # Calculate right sum as total_sum - left_sum - nums[i]
            if left_sum == (total_sum - left_sum - nums[i]):
                return i
            left_sum += nums[i]  # Update the left sum for the next iteration

        return -1  # Return -1 if no pivot index is found
