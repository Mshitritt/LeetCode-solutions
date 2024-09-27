class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSet = set(nums)
        # if missing is in middl 
        for i in range(len(nums)):
            if i not in numsSet:
                return i

        # if missing in the end 
        return len(nums)
         