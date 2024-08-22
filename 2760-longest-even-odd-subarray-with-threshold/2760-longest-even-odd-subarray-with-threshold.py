class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        max_len = 0
        current_len = 0

        for i in range(len(nums)):
            # Only start counting if the first element is even and within the threshold
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                current_len = 1  # Start a new valid subarray
                
                # Expand the subarray while meeting the conditions
                for j in range(i + 1, len(nums)):
                    if nums[j] > threshold:
                        break
                    if nums[j] % 2 == nums[j - 1] % 2:  # If parity does not alternate
                        break
                    
                    current_len += 1
                
                max_len = max(max_len, current_len)

        return max_len




        