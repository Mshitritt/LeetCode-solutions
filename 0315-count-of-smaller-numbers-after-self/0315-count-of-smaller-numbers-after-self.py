class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        numsSorted = [nums[n-1]]
        for i in range(n-2, -1, -1):
            idx = bisect_left(numsSorted, nums[i])
            res[i] = idx
            numsSorted.insert(idx, nums[i])
        return res
