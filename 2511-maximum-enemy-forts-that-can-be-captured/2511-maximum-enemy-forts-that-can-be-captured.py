class Solution:
    def captureForts(self, forts: List[int]) -> int:
        l = 0
        r = l + 1
        captures = 0
        tempCaptures = 0
        while r < len(forts):
            # tempCaptures = 0
            # l += 1
            # r = l + 1
            if forts[l] == 1:
                while r < len(forts) and forts[r] == 0:
                    tempCaptures += 1
                    r += 1
                if r < len(forts) and forts[r] == -1:
                    captures = max(tempCaptures, captures)
            elif forts[l] == -1:
                while r < len(forts) and forts[r] == 0:
                    tempCaptures += 1
                    r += 1
                if r < len(forts) and forts[r] == 1:
                    captures = max(tempCaptures, captures)
            else:
                pass
                
        return captures



