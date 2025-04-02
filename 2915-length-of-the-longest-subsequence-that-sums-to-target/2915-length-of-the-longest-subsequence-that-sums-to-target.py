class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        prefix = {0: -1}
        total = 0
        res = -1

        for i, num in enumerate(nums):
            total += num
            if total >= target:
                diff = total - target
                if diff in prefix:
                    res = max(res, i - prefix[diff])
            if total not in prefix:
                prefix[total] = i
        return res


        