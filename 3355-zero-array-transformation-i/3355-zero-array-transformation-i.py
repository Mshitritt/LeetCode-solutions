class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        util = [0]*(len(nums)+1)
        for l, r in queries:
            util[l] += 1
            util[r+1] -= 1
        
        prefix_util = [0] * (len(nums)+1)
        prefix_util[0] = util[0]
        for i in range(1, len(nums)+1):
            prefix_util[i] = prefix_util[i-1] + util[i]

        for i in range(len(nums)):
            if nums[i] > prefix_util[i]:
                return False
        
        return True
        

