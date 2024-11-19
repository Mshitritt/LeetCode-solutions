class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        is_increasing = [False] * (n - k + 1)

        # Check if each subarray of size k is strictly increasing
        for start in range(n - k + 1):
            strictly_increasing = True
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    strictly_increasing = False
                    break
            is_increasing[start] = strictly_increasing

        # Check for two consecutive True values in is_increasing
        for i in range(len(is_increasing)-k):
            if is_increasing[i] and is_increasing[i + k]:
                return True

        return False
