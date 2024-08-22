class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        w = max(nums)
        nums.remove(w)
        x = max(nums)
        nums.remove(x)
        y = min(nums)
        nums.remove(y)
        z = min(nums)
        return (w * x)-(y * z)