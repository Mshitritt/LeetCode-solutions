class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        heap = []
        for s in range(n):
            total = 0
            for e in range(s, n):
                total += nums[e]
                heapq.heappush(heap, total)
        
        res = 0
        right -= (left-1)
        while heap and left > 1:
            heapq.heappop(heap)
            left -= 1
        
        while heap and right:
            res += heapq.heappop(heap)
            right -= 1
        
        return res % (10**9 + 7)