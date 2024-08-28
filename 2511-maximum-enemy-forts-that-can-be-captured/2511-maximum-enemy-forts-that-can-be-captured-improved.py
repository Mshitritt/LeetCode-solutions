class Solution:
    def captureForts(self, forts: List[int]) -> int:
        r = 0
        captures = 0
        while r < len(forts):
            tempCaptures = 0
            l = r
            r = l + 1
            # new version
            if forts[l] == 1 or forts[l] == -1 and r < len(forts):
                while r < len(forts) and forts[r] == 0:
                    tempCaptures += 1
                    r += 1
                if r < len(forts) and forts[l] == -forts[r]:
                    captures = max(tempCaptures, captures)
        return captures



