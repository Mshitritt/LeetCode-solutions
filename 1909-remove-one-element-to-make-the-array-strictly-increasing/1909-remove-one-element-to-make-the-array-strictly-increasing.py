class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        c = 0
        index = -1
        # count how many non-increasing elements have
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                c += 1
                index = i
        # print(f'c = {c}, index = {index}')
        if c > 1:
            return False
        if c == 0:
            return True

        # check where is index point
        if index == 0 or index == len(nums) - 2:
            return True
        else:
            # remove element of index
            if nums[index - 1] < nums[index + 1]:
                return True
            # remove element of index+1
            elif nums[index] < nums[index + 2]:
                return True
            else:
                return False
        