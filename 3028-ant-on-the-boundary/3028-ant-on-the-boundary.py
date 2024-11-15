class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        prefix = 0
        res = 0
        for num in nums:
            prefix += num
            if prefix == 0:
                res += 1
        return res
