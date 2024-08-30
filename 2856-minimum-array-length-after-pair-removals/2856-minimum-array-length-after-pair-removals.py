class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        r = (n+1) // 2
        removals = 0
        while r < n:
            if nums[l] < nums[r]:
                removals += 2
                l += 1
                r += 1
            else:
                r += 1
        return n - removals 
        

        