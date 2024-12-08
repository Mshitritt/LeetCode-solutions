class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        minPos, maxPos, left = -1, -1, -1
        for i in range(len(nums)):
            if nums[i] == minK:
                minPos = i
            if nums[i] == maxK:
                maxPos = i
            if nums[i] < minK or nums[i] > maxK:
                minPos, maxPos, left = -1, -1, i

            
            res += max(0, min(minPos, maxPos)-left)
        return res

