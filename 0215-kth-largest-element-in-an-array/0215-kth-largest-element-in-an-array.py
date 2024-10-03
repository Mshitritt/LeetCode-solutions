class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_num = min(nums)
        max_num = max(nums)
        counter = [0]*(max_num - min_num + 1)
        for num in nums:
            idx = num - min_num
            counter[idx] += 1
        
        for i in range(max_num - min_num, -1, -1):
            k -= counter[i]
            if k <= 0:
                return i + min_num
        
