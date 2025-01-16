class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        bisect_left(nums, nums[i]-1, 0, i)
        """
 
        nums.sort()
        n = len(nums)
        if n == 1:
            return
        sml, lrg = 0, n//2
        while nums[sml] == nums[lrg]:
            lrg += 1

        for i in range(1, n):
            if i % 2 == 0:
                # num[i] is small
                if nums[i-1] < nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                elif nums[i-1] == nums[i]:
                    # find small value
                    j = bisect_right(nums, nums[i]+1, i+1, n-1)
                    nums[j], nums[i] = nums[i], nums[j]
            else:
                #  num[i] is larg
                if nums[i-1] > nums[i]:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                elif nums[i-1] == nums[i]:
                    # find large value
                    j = bisect_right(nums, nums[i]+1, i+1, n-1)
                    nums[j], nums[i] = nums[i], nums[j]
                

        