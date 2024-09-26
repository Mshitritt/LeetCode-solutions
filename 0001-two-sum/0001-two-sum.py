class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        left = 0
        right = len(nums)-1
        
        for idx, val in enumerate(nums):
            indices.setdefault(val, []).append(idx)

        nums.sort()
        while left < right:
            sm = nums[left] + nums[right]
            if sm == target:
                break
            elif sm < target:
                left += 1
            else:
                right -= 1


        #resl = []
        resl = indices[nums[left]] + indices[nums[right]]
        if len(resl) > 2:
            return resl[:2]
        return resl

        