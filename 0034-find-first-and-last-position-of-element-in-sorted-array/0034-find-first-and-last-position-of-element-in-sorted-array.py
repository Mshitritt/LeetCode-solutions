class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            # Check if the left index is valid and matches the target
            return left if left < len(nums) and nums[left] == target else -1

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            # Check if the right index is valid and matches the target
            return right if right >= 0 and nums[right] == target else -1

        left_index = findLeft(nums, target)
        if left_index == -1:
            return [-1, -1]  # Target not found
        right_index = findRight(nums, target)
        return [left_index, right_index]