class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        mapp = {}   # rows dictionary
        pairs = 0   # pairs counter

        # row counting
        for r in range(len(grid)):
            key = ""
            for c in range(len(grid[r])):
                key += str(grid[r][c])+','

            
            mapp.setdefault(key, 0)
            mapp[key] += 1
            
        # column counting
        for r in range(len(grid)):
            key = ""
            for c in range(len(grid)):
                key += str(grid[c][r])+','

            if key in mapp:
                pairs += mapp[key]
    
        return pairs

            