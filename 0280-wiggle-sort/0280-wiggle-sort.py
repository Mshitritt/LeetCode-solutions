class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if i%2 == 1:
                if nums[i-1] <= nums[i]:
                    continue
                else:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
            else:
                if nums[i-1] >= nums[i]:
                    continue
                else:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
        