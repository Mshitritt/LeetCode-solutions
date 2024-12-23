class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        max_q = max(queries)
        freq = defaultdict(int)
        heap = []   # min heap

        # initionlaize
        for item in items:
            h = (item[0], item[1])  # (curr_price, curr_beauty)
            heapq.heappush(heap, h)
        
        # process
        maxBeauty = 0
        while heap:
            p, b = heapq.heappop(heap)
            maxBeauty = max(maxBeauty, b)

            while heap and heap[0] == p:
                _, b = heapq.heappop(heap)
                maxBeauty = max(maxBeauty, b)
            freq[p] = maxBeauty
        
        res = []
        prices = list(freq.keys())

        def bs(target):
            l, r = 0, len(prices)-1
            while l < r:
                mid = (l+r)//2
                if prices[mid] == target:
                    return mid
                elif prices[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            return l

        for q in queries:
            # Find the closest price <= q using bisect_right
            idx = bisect.bisect_right(prices, q) - 1
            if idx >= 0:  # If there's a valid price <= q
                res.append(freq[prices[idx]])
            else:  # No price <= q
                res.append(0)
                
        return res 


        
        