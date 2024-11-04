class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        min_heap = []
        n1Sum = 0
        res = 0
        count = 0
        for n1, n2 in pairs:
            count += 1
            n1Sum += n1
            heapq.heappush(min_heap, n1)
            if count > k:
                n = heapq.heappop(min_heap)
                n1Sum -= n
                count -= 1
            if count == k:
                res = max(res, n1Sum * n2)
        return res



        return res
