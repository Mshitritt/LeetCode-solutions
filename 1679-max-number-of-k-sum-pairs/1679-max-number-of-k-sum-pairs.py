from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums.sort()
        l = 0
        r = len(nums)-1
        counter = 0
        while l < r:
            # 1,3,3,3,4 -- k =6
            summ = nums[l] + nums[r]
            if summ == k:
                counter += 1
                l += 1
                r -= 1
            else:
                if summ < k:
                    l += 1
                else:
                    r -= 1
        return counter
            


                