class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Calculate the effective range
        min_val = min(nums) - k
        max_val = max(nums) + k
        
        # Create a frequency array
        freq = [0] * (max_val - min_val + 1)
        
        # Populate the frequency array
        for num in nums:
            freq[num - min_val] += 1
        
        # Sliding window on the frequency array
        max_beauty = 0
        window_sum = 0
        window_size = 2 * k + 1
        
        for i in range(len(freq)):
            # Add the current frequency to the window
            window_sum += freq[i]
            
            # Shrink the window if it exceeds the size
            if i >= window_size:
                window_sum -= freq[i - window_size]
            
            # Update the maximum beauty
            max_beauty = max(max_beauty, window_sum)
        
        return max_beauty
        
        """
        nums.sort()
        l = 0
        res = 0

        for r in range(len(nums)):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            res = max(res, r - l + 1)

        return res
        """