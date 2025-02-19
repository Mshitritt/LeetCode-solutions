class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevs = {}
        for i, num in enumerate(nums):
            if target - num in prevs:
                return [prevs[target-num], i]
            prevs[num] = i

            
        