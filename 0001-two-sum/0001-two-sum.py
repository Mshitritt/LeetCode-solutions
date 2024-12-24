class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}    # num: idx
        res = []
        for i, num in enumerate(nums):
            k = target - num
            if k in idx:
                return [idx[k], i]
            else:
                idx[num] = i
        return res
            
        

        