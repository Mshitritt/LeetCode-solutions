class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for num, val in freq.items():
            heapq.heappush(heap, (-val, num))
        
        res = []
        while k:
            val, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        return res