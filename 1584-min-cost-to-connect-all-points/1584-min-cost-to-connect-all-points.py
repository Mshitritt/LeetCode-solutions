class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # -- Prime's Algorithm --
        def getCost(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)

        heap = [(0, points[0],)]   # (cost, val)
        seen = set()
        
        res = 0

        while heap:
            cost, p = heapq.heappop(heap)
            
            while heap and tuple(p) in seen:
                cost, p = heapq.heappop(heap)

            res += cost
            seen.add(tuple(p))

            if len(seen) == len(points):
                break
  
            for p1 in points:
                if tuple(p1) not in seen and tuple(p) != tuple(p1):
                    heapq.heappush(heap, (getCost(p, p1), p1))
            

            
            
            
        

        return res
