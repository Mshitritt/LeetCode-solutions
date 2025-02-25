class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        heap = [] # (val, idx)

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        temp = []
        while heap:
            temp.append(heapq.heappop(heap))
        
        for num in temp:
            heapq.heappush(heap, -num)
        
        while k:
            val = heapq.heappop(heap)
            val *= -1
            res += val
            heapq.heappush(heap, -math.ceil(val/3))
            k -= 1
        return res