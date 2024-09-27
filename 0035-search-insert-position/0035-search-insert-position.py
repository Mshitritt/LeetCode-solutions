class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = 0
        # if target place is first
        if target < nums[low]:
            return low 
        # if target place is last
        if target > nums[high]:
            return high + 1

        if target == nums[high]:
            return high

        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[low] < target < nums[high] and low+1 == high:
                return low + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        
        return mid