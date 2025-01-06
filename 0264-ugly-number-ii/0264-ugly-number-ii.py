class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        heap = [1]
        seen = set([1])

        
        while True:
            curr = heapq.heappop(heap)
            n -= 1
            if n == 0:
                return curr
            
            for i in [2, 3, 5]:
                num = curr*i
                if num not in seen:
                    seen.add(num)
                    heapq.heappush(heap, num)

        
