class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        goods = 0
        l = 0
        m = 0
        unique = defaultdict(int)

        for r in range(len(nums)):
            unique[nums[r]] += 1

            while len(unique) > k:
                unique[nums[m]] -= 1
                if unique[nums[m]] == 0:
                    del unique[nums[m]]
                m += 1
                l = m
            
            while unique[nums[m]] > 1:
                unique[nums[m]] -= 1
                m += 1

            if len(unique) == k:
                goods += (m - l + 1)

        return goods
                

                

            
                
                
