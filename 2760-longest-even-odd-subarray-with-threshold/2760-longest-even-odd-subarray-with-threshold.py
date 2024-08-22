class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        subArray = 0
        c = 0
        for l in range(len(nums)):
            if c > subArray:
                subArray = c
            if nums[l] % 2 == 0 and nums[l] <= threshold:
                c = 1

                for r in range(l + 1, len(nums)):
                    if nums[r - 1] % 2 == 0:
                        if nums[r] % 2 == 1 and nums[r] <= threshold:
                            c += 1
                        else:
                            break
                    else:
                        if nums[r] % 2 == 0 and nums[r] <= threshold:
                            c += 1
                        else:
                            break
        if c > subArray:
            subArray = c
        return subArray
                        
                        





        