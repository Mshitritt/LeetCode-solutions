class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        minimum = max_score = nums[k]
        i = j = k
        n = len(nums)

        while i > 0 or j < n - 1:
            # Check if we can expand the subarray
            if i > 0 and j < n - 1:
                # Expand the subarray towards the side with the larger neighbor
                if nums[i - 1] >= nums[j + 1]:
                    i -= 1
                else:
                    j += 1
            elif i == 0 and j < n - 1:
                j += 1
            elif j == n - 1 and i > 0:
                i -= 1

            # Update the minimum and the maximum score
            minimum = min(minimum, nums[i], nums[j])
            max_score = max(max_score, minimum * (j - i + 1))
            
        return max_score
                