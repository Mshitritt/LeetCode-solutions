class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 1
        e = s + k -1
        summ = sum(nums[:k])
        avg = summ/k
        
        while e < len(nums):
            summ = summ - nums[s-1] + nums[e]
            avg = max(avg, summ/k)
            s += 1
            e += 1

        return avg