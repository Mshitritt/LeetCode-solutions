class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        minNum = float('inf')
        middleNum = float('inf')
        for num in nums:
            if num > middleNum and middleNum > minNum:
                return True
            # num > middleNum > minNum
            else:
                if num > minNum:
                    middleNum = num
                else:
                    minNum = num
        return False


            

        