class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        valid_end = set()

        # Check if each subarray of size k is strictly increasing
        for start in range(n - k + 1):
            strictly_increasing = True
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    strictly_increasing = False
                    break
            if strictly_increasing:
                if (start-1) in valid_end:
                    return True
                valid_end.add(start+k-1)

        

        return False