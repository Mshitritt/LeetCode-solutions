class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        mapp = {}
        pairs = 0 

        # row counting
        for r in range(len(grid)):
            key = ""
            for c in range(len(grid[r])):
                key += str(grid[r][c])

            if mapp.setdefault(key, 0) == 0:
                mapp[key] = 1
            else:
                mapp[key] += 1

        for r in range(len(grid)):
            key = ""
            for c in range(len(grid)):
                key += str(grid[c][r])

            if key in mapp:
                pairs += mapp[key]
            

        # print(mapp)
        # key_max = max(mapp.keys(), key=lambda k: mapp[k])
        return pairs
            