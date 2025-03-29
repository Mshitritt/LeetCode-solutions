class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ee, eo, oe, oo = 0, 0, 0, 0

        for curr in nums:
            if curr % 2 == 0:
                ee += 1
                oe = eo + 1
            else:
                oo += 1
                eo = oe + 1
        return max(ee, eo, oe, oo)
            
            