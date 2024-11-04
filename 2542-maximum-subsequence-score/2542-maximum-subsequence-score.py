class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        min_heap = []
        n1Sum = 0
        res = 0
        for n1, n2 in pairs:
            n1Sum += n1
            heapq.heappush(min_heap, n1)
            if len(min_heap) > k:
                n = heapq.heappop(min_heap)
                n1Sum -= n
            if len(min_heap) == k:
                res = max(res, n1Sum * n2)
        return res
