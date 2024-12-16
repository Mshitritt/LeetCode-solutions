class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        s = set()
        for x, y in points:
            s.add((x, y))
        
        res = float('inf')
        for x, y in points:
            for dx, dy in s:
                if dx > x and dy > y:
                    # found diagonal 
                    if (x, dy) in s and (dx, y) in s:
                        # found rectangle
                        res = min(res, abs(x-dx)*abs(y-dy))



        return res if res != float('inf') else 0
        
        