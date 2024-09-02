class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the first window of size k
        current_sum = sum(nums[:k])
        max_avg = current_sum / k
        
        # Use a sliding window to find the maximum average
        for i in range(1, len(nums) - k + 1):
            # Update the sum by subtracting the element going out of the window 
            # and adding the element coming into the window
            current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
            max_avg = max(max_avg, current_sum / k)
        
        return max_avg