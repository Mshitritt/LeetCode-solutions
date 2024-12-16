class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        freq = defaultdict(int)
        while r < len(nums):
            freq[nums[r]] += 1
            
            while max(freq) - min(freq) > 2:
                freq[nums[l]] -= 1
                if not freq[nums[l]]:
                    del freq[nums[l]]
                   
                l += 1
            
            res += r-l+1
            r += 1
                
                
        return res
